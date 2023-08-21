import numpy as np
import matplotlib.pyplot as plt

def ex_3l():
    # Define the interval
    x, y = np.meshgrid(np.linspace(-10, 10, 25), np.linspace(-10, 10, 25))
    u, v = np.cos(x), np.sin(y)

    # Plot the function
    plt.quiver(x, y, u, v, scale=20, width=0.002)
    plt.title('Campo vectorial: $f(x, y)=(cos(x), sin(y))$')
    plt.grid(True)
    plt.gca().set_aspect('equal')

    # Display the plot
    plt.show()

if __name__ == '__main__':
    ex_3l()
