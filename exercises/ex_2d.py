import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def ex_2d():
    # Create a grid of points using polar coordinates
    r = np.arange(0, 4, 0.01)
    theta = np.arange(0, 2 * np.pi, 0.01)
    R, Theta = np.meshgrid(r, theta)

    X = R * np.cos(Theta)
    Y = R * np.sin(Theta)

    # Compute the value of the function
    Z = np.sqrt(16 - R**2)

    # Plot the function using surface plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)
    ax.set_aspect('equal')

    # Display plot
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    ex_2d()

