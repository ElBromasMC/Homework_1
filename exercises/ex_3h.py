import numpy as np
import matplotlib.pyplot as plt

def ex_3h():
    # Define the interval
    x, y = np.meshgrid(np.linspace(-3, 3, 15), np.linspace(-3, 3, 15))
    u, v = 2*y, 0

    # Plot the function
    plt.quiver(x, y, u, v, scale=100, width=0.003)
    plt.title('Campo vectorial: $f(x, y)=(2y, 0)$')
    plt.grid(True)
    plt.gca().set_aspect('equal')

    # Display the plot
    plt.show()

if __name__ == '__main__':
    ex_3h()
