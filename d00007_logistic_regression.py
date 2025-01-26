###
# Implement Logistic regression on a simple dataset and plot the sigmoid function
# Calculate and interpret accuracy, precision, recall, and F1 score for the model
# Visualize the decision boundary for the logistic regression model
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import sklearn.datasets
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
from sklearn.inspection import DecisionBoundaryDisplay

iris = sklearn.datasets.load_iris()
target = iris.target[np.isin(iris['target'], [0, 1])]
data = iris.data[np.isin(iris['target'], [0, 1])][:, 2:4]
data = StandardScaler().fit_transform(data)
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size= 0.3, random_state= 42)
model = LogisticRegression(C=3)
clf = model.fit(X_train, y_train)
predictions = (clf.predict_proba(X_test)[:, 1] >= 0.3).astype(int)
print(np.sum(predictions == y_test))
print(len(predictions))
cm = confusion_matrix(y_test, predictions)
display_cm = ConfusionMatrixDisplay(confusion_matrix= cm)
display_cm.plot()
plt.show()

print(accuracy_score(y_test, predictions))
print(precision_score(y_test, predictions))
print(recall_score(y_test, predictions))
print(f1_score(y_test, predictions))

DecisionBoundaryDisplay.from_estimator(
    clf, X_train, response_method="predict", grid_resolution=100, alpha=0.5
)
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, edgecolor="k", marker="o", label="Train")
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, edgecolor="k", marker="x", label="Test")
plt.legend()
plt.xlabel("Petal Length (standardized)")
plt.ylabel("Petal Width (standardized)")
plt.title("Logistic Regression Decision Boundary")
plt.show()