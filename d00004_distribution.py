import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Binomial Distribution
sigma = 50
mu = 10
binomial_dist = np.random.binomial(n = 10, p = 0.5, size = 10000)
# Density = Normalizes the area under the curve to sum to 1
plt.hist(binomial_dist, 30, density= True)
plt.show()
# Normal Distribution
norm_dist = np.random.normal(loc = 50, scale = 1, size = 10000)
plt.hist(norm_dist, 30, density= True)
plt.show()

# Normal Distribution 
# kde is a parameter to compute a kernel density estimate to smooth distribution and show the lines
sns.histplot(norm_dist, kde=True, stat = "density")
plt.title("Normal Distribution")
plt.xlabel("x")
plt.ylabel("Density")
plt.show()
