import simpleaudio as sa
import time
import numpy as np
import numba as nb

from NoteNames import *
from Lieder import *

sample_rate = 22050
note_names = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")
note_values = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)


class Sound():
    def __init__(self, sound: np.ndarray) -> None:
        self.sound = sound

    def sumSounds(list_of_sounds: list):
        wave = np.zeros(len(list_of_sounds[0].sound), dtype=np.float32)
        for sound in list_of_sounds:
            wave += sound.sound
        wave = wave.astype(np.int16)
        return Sound(wave)

    def play(self):
        self.play_obj = sa.play_buffer(self.sound, 1, 2, sample_rate)

    def wait(self) -> None:
        self.play_obj.wait_done()

    def is_playing(self) -> bool:
        return self.play_obj.is_playing()


class Note(Sound):
    """
    Eine Klasse, die eine musikalische Note repräsentiert.

    Attributes:
    name (str): Der Name der Note.
    duration (float): Die Dauer der Note in Sekunden.
    note_number (int): Die MIDI-Nummer der Note.
    octave (int): Die Oktave der Note.
    amplitude (int): Die Amplitude der Note.

    Methods:
    create_wave(): Erzeugt die Wellenform der Note.
    play(): Spielt die Note ab.
    wait(): Wartet, bis die Note fertig gespielt ist.
    """

    def __init__(self, name: str = "",
                 duration: float = 1/4.,
                 note: int = 0,
                 octave: int = 4,
                 volume: int = 1000) -> None:
        self.name = name
        self.duration = duration    # in seconds
        self.note = note
        self.octave = octave
        self.volume = volume
        self.frequency = round(
            440 * 2 ** (self.note / 12) * 2 ** (self.octave-4))
        self.create_wave()

    def create_wave(self) -> np.ndarray:
        t = np.linspace(0.0, self.duration*1.0,
                        int(self.duration * sample_rate), False)
        envelope = np.full_like(t, 1.)
        for sample in range((9*len(envelope))//10, len(envelope)):
            envelope[sample] = 1 - (sample - (9*len(envelope))//10) / \
                (len(envelope) - (9*len(envelope))//10)
        for sample in range(0, len(envelope)//20):
            envelope[sample] = sample / (len(envelope)//20)

        float_sound = ((np.sin(2*np.pi*self.frequency*t)           # base frequency
                        + 0.50*np.sin(2*np.pi*self.frequency * \
                                      t*2)   # 2nd harmonic
                        + 0.2*np.sin(2*np.pi*self.frequency*t*3))  # 3rd harmonic
                       * envelope * self.volume)
        self.sound = float_sound.astype(np.int16)
        return self.sound


class Melody(Sound):
    def __init__(self, notes) -> None:
        self.notes = notes
        self.create_wave()

    def create_wave(self) -> np.ndarray:
        self.sound = np.array([], dtype=np.float32)
        for note in self.notes:
            self.sound = np.append(self.sound, note.sound)
        self.sound = self.sound.astype(np.int16)
        return self.sound


class Chord():
    def __init__(self, notes: list = [], duration: float = 1/4., volume: int = 2 ** 16):
        self.notes = notes
        self.duration = duration
        self.volume = volume
        self.create_wave()

    def create_wave(self) -> np.ndarray:
        self.sound = np.zeros(
            int(self.duration * sample_rate), dtype=np.float32)
        for note in self.notes:
            self.sound += note.create_wave()
        self.sound = self.sound.astype(np.int16)
        return self.sound


melodies = []

for i, voice in enumerate([stille_nacht]):
    note_object_list = []
    for note in voice:
        print(note)
        name = note[0]
        duration = 1/note[1]*2
        note_number = notes_to12_all[name[:-1]]
        octave = int(name[-1])
        note = Note(name, 1/duration, note_number, octave, 1000)
        note_object_list.append(note)
    melodies.append(Melody(note_object_list))

# Play one voice at a time
for melody in melodies:
    melody.play()
    melody.wait()

# Play both voices at the same time
multi_track = Sound.sumSounds(melodies)  # Create a MultiTrack object
multi_track.play()  # Play the MultiTrack object
multi_track.wait()  # Wait until the MultiTrack object is done playing
