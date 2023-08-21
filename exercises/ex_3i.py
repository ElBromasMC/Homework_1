import numpy as np
import matplotlib.pyplot as plt

def ex_3i():
    # Define the interval
    x, y = np.meshgrid(np.linspace(-6, 6, 30), np.linspace(-6, 6, 30))
    u, v = x**2, y**2

    # Plot the function
    plt.quiver(x, y, u, v, scale=250, width=0.001)
    plt.title('Campo vectorial: f(x, y)=(x^2, y^2)')
    plt.grid(True)

    # Display the plot
    plt.show()

if __name__ == '__main__':
    ex_3i()
