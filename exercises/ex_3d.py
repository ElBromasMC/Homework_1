import numpy as np
import matplotlib.pyplot as plt

def ex_3d():
    # Define the interval
    x, y = np.meshgrid(np.linspace(-1, 1, 25), np.linspace(-1, 1, 25))
    u, v = 3*x*y/(x**2 + y**2)**(5/2), (2 * y**2 - x**2)/(x**2 + y**2)**(5/2)

    # Plot the function
    plt.streamplot(x, y, u, v)
    plt.title('Campo vectorial: $f(x, y)=(3xy/r^5, (2y^2 - x^2)/r^5)$')
    plt.grid(True)
    plt.gca().set_aspect('equal')

    # Display the plot
    plt.show()

if __name__ == '__main__':
    ex_3d()
