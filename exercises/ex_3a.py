import numpy as np
import matplotlib.pyplot as plt

def ex_3a():
    # Define the interval
    x, y = np.meshgrid(np.linspace(-6, 6, 30), np.linspace(-6, 6, 30))
    u, v = 3, -5

    # Plot the function
    plt.quiver(x, y, u, v, scale=150, width=0.002)
    plt.title('Campo vectorial: $f(x, y)=(3, -5)$')
    plt.grid(True)
    plt.gca().set_aspect('equal')

    # Display the plot
    plt.show()

if __name__ == '__main__':
    ex_3a()
