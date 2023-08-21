import numpy as np
import matplotlib.pyplot as plt

def ex_3k():
    # Define the interval
    x, y = np.meshgrid(np.linspace(-6, 6, 30), np.linspace(-6, 6, 30))
    u, v = x*y, -x

    # Plot the function
    plt.streamplot(x, y, u, v)
    plt.title('Campo vectorial: $f(x, y)=(xy, -x)$')
    plt.grid(True)
    plt.gca().set_aspect('equal')

    # Display the plot
    plt.show()

if __name__ == '__main__':
    ex_3k()
