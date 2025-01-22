import seaborn as sns
import matplotlib.pyplot as plt
scores = [65, 70, 72, 75, 80, 85, 88, 90, 95, 98]

# Very basic plotting
sns.boxplot(data = scores)
plt.show()
sns.displot(scores)
plt.show()

