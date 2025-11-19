import numpy as np
import matplotlib.pyplot as plt

# Generate some sample data
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 0.8, 0.9, 0.1, -0.8, -1])

# Fit a 2nd-degree polynomial
coefficients = np.polyfit(x, y, 2)
print("Polynomial Coefficients:", coefficients)

# Create a polynomial function from the coefficients
p = np.poly1d(coefficients)

# Generate points for plotting the fitted curve
x_fit = np.linspace(0, 5, 100)
y_fit = p(x_fit)

# Plot the original data and the fitted curve
plt.scatter(x, y, label='Original Data')
plt.plot(x_fit, y_fit, color='red', label='Fitted Polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Fit using numpy.polyfit()')
plt.legend()
plt.grid(True)
plt.show()