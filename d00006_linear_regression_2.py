import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

combined_data = np.array(list(zip(x, y)))
print(combined_data)

plt.scatter(x, y, label = "Data points")

plt.plot(x, 0.7 * x + 2.2, color = 'red', label = "Regression line")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression Fit")
plt.legend()

y_hat = 0.7 * x + 2.2
residuals = y - y_hat
residual_sum = np.sum(residuals)
print(residual_sum) # -1.5000000000000004

# Draws vertical lines to residuals
plt.vlines(x, y, y_hat, color='g')

# Mean Absolute Error (MAE)
print(np.sum(abs(y - y_hat)) / len(x)) # 0.7400000000000001

# Mean Squared Error (MSE)
print(np.sum((y - y_hat) ** 2) / len(x)) # 0.5900000000000002

# Root Mean Squared Error
print(np.sqrt(np.sum((y - y_hat) ** 2) / len(x))) # 0.768114574786861

plt.show()

# Residual Plot
plt.scatter(x, residuals, color = "red", label = "residuals")
# Plot a straight line
plt.axhline(y=0, color='b', linestyle='-')
plt.title("Residuals")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()