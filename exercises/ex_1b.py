import numpy as np
import matplotlib.pyplot as plt

def ex_1b():
    # Interval from -10 to 10 with 200 points
    x = np.linspace(-10, 10, 200)
    
    # Compute the values of the function
    y = x**2 + 5*x  - 3

    # Plot the function
    plt.plot(x, y, color='r', linestyle='--', label='x^2 + 5x - 3')

    # Display's options
    plt.title('Ejercicio 1b')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

    # Display the plot
    plt.show()

if __name__ == '__main__':
    ex_1b()

