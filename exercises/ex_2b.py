import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def ex_2b():
    # Create a grid of points
    x = np.arange(-5, 5, 0.01)
    y = np.arange(-5, 5, 0.01)
    X, Y = np.meshgrid(x, y)

    # Compute the value of the function
    Z = np.reciprocal(np.sqrt(X**2 + (Y - 1)**2)) - np.reciprocal(X**2 + (Y + 1)**2)

    # Plot the function using surface plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)
    ax.set_zlim(-3, 3)

    # Display plot
    plt.show()

if __name__ == '__main__':
    ex_2b()

