import numpy as np
import matplotlib.pyplot as plt

def ex_1a():
    # Interval from 0 to 2pi
    x = np.arange(0, 2 * np.pi, 0.1)
    
    # Compute the values of both functions
    y1 = np.sin(x)
    y2 = x**2 + 3*x

    # Plot the functions
    plt.plot(x, y1, color='r', label='sin(x)')
    plt.plot(x, y2, color='b', label='x^2 + 3x')

    # Display's options
    plt.title('Ejercicio 1a')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

    # Display the plot
    plt.show()

if __name__ == '__main__':
    ex_1a()

