import numpy as np
import matplotlib.pyplot as plt

def ex_3c():
    # Define the interval
    x, y = np.meshgrid(np.linspace(-1, 1, 20), np.linspace(-1, 1, 20))
    u, v = x/(x**2 + y**2)**(3/2), y/(x**2 + y**2)**(3/2)

    # Plot the function
    plt.quiver(x, y, u, v, scale=100, width=0.005)
    plt.title('Campo vectorial: $f(x, y)=(x/r^3, y/r^3)$')
    plt.grid(True)
    plt.gca().set_aspect('equal')

    # Display the plot
    plt.show()

if __name__ == '__main__':
    ex_3c()
