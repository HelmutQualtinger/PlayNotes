import plotly as pl
import numpy as np

import plotly.graph_objects as go
# Generate random data
np.random.seed(0)
x = np.random.randn(50)+10
y = np.random.randn(50)+20
age = np.round(np.random.normal(50, 20, 50))
sex = np.random.choice(["Male", "Female"], 50)

# Assign colors based on sex
colors = ['blue' if s == 'Male' else 'red' for s in sex]

# Create scatter plot
fig = go.Figure(data=go.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker=dict(
        color=colors,  # Use the colors list
        size=age,
    ),
    # Set the hover text with sex and age
    # Format age with two decimal points
    text=['Sex: ' + s + '\n Age: ' + \
          '{:.2f}'.format(a) for s, a in zip(sex, age)],
    # Set the hover template to show the sex and age
    hovertemplate='%{text}<extra></extra>'
))

# Set x-axis and y-axis titles
fig.update_layout(
    xaxis_title="Latitude",
    yaxis_title="Meridian",
    xaxis=dict(visible=True),
    yaxis=dict(visible=True)
)


fig.show()
p
