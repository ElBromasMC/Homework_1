import numpy as np
import matplotlib.pyplot as plt

def ex_3j():
    # Define the interval
    x, y = np.meshgrid(np.linspace(-1, 1, 25), np.linspace(-1, 1, 25))
    u, v = x/np.sqrt(x**2 + y**2), -y/np.sqrt(x**2 + y**2)

    # Plot the function
    plt.streamplot(x, y, u, v)
    plt.title('Campo vectorial: $f(x, y)=(x/r, -y/r)$')
    plt.grid(True)
    plt.gca().set_aspect('equal')

    # Display the plot
    plt.show()

if __name__ == '__main__':
    ex_3j()
