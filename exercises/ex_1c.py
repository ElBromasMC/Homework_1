import numpy as np
import matplotlib.pyplot as plt

def ex_1c():
    # Interval from 0 to 6
    x = np.arange(0, 6, 0.1)
    
    # Compute the values of both functions
    y1 = 3 * x * np.exp(x)
    y2 = np.sin(x + 3)

    # Plot the functions
    plt.plot(x, y1, color='b', label='3xe^x')
    plt.plot(x, y2, color='r', linestyle='--', label='sen(x + 3)')

    # Display's options
    plt.title('Ejercicio 1a')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

    # Display the plot
    plt.show()

if __name__ == '__main__':
    ex_1c()

