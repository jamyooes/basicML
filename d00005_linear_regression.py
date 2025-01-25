import numpy as np

"""
Give data points calculate the slop and y-intercept 

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
"""

# Arrays for x and y
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
# print(x, y)

# calculate mean for x and y
x_hat = np.mean(x)
y_hat = np.mean(y)
# print(x_hat, y_hat)

# Formula for slope
slope  = np.sum(((x - x_hat) * (y - y_hat))) / np.sum((x - x_hat) ** 2)
print(slope)

# Formula for slope intercept
intercept = y_hat - slope * x_hat
print(intercept)