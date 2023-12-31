notes_to12_german = {
    'C': 0,
    'C#': 1,      # Cis
    'Db': 1,      # Des (Re bemolle)
    'D': 2,
    'D#': 3,      # Dis
    'Eb': 3,      # Es (Mi bemolle)
    'E': 4,
    'F': 5,
    'F#': 6,      # Fis
    'Gb': 6,      # Ges (Sol bemolle)
    'G': 7,
    'G#': 8,      # Gis
    'Ab': 8,      # As (La bemolle)
    'A': 9,
    'A#': 10,     # Ais
    'Bb': 10,     # B (Si bemolle)
    'B': 10,     # B (Si bemolle)
    'H': 11,      # B (Si)
    'Cb': 11      # Ces (Do bemolle)
}
notes_to12_italian = {
    'Do': 0,
    'Do#': 1,     # Do diesis
    'Re': 2,
    'Re#': 3,     # Re diesis
    'Mi': 4,
    'Fa': 5,
    'Fa#': 6,     # Fa diesis
    'Sol': 7,
    'Sol#': 8,    # Sol diesis
    'La': 9,
    'La#': 10,    # La diesis
    'Si': 11,
    'Mib': 11,    # Mi bemolle
    'Lab': 8      # La bemolle
}
notes_to12_english = {
    'C': 0,
    'C#': 1,      # C sharp
    'Db': 1,      # D flat
    'D': 2,
    'D#': 3,      # D sharp
    'Eb': 3,      # E flat
    'E': 4,
    'F': 5,
    'F#': 6,      # F sharp
    'Gb': 6,      # G flat
    'G': 7,
    'G#': 8,      # G sharp
    'Ab': 8,      # A flat
    'A': 9,
    'A#': 10,     # A sharp
    'Bb': 10,     # B flat
    'H': 11,      # B
    'Cb': 11      # C flat
}

notes_to12_all = {**notes_to12_german,
                  **notes_to12_italian,
                  **notes_to12_english}
