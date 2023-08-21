import numpy as np
import matplotlib.pyplot as plt

def ex_3g():
    # Define the interval
    x, y = np.meshgrid(np.linspace(-6, 6, 30), np.linspace(-6, 6, 30))
    u, v = x/np.sqrt(2), -y/np.sqrt(2)

    # Plot the function
    plt.quiver(x, y, u, v, scale=200, width=0.002)
    plt.grid(True)
    plt.gca().set_aspect('equal')

    # Display the plot
    plt.show()

if __name__ == '__main__':
    ex_3g()
