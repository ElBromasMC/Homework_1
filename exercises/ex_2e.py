import plotly.graph_objects as go
import numpy as np

def ex_2e():
    # Set the intervals
    x, y, z = np.mgrid[-6:6:50j, -6:6:50j, -6:6:50j]

    # Get the values of the function
    values = x**2 + y**2 + z**2

    # Plot the function
    fig = go.Figure(data=go.Isosurface(
        x=x.flatten(),
        y=y.flatten(),
        z=z.flatten(),
        value=values.flatten(),
        isomin=0,
        isomax=72,
        opacity=0.25,
        surface_count=10
    ))

    # Display the plot
    fig.show()

if __name__ == '__main__':
    ex_2e()
