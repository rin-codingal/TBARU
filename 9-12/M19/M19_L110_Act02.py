from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Generate and dataset for Logistic Regression
x, y = make_classification(
    n_samples=100,
    n_features=1,
    n_classes=2,
    n_clusters_per_class=1,
    flip_y=0.03,
    n_informative=1,
    n_redundant=0,
    n_repeated=0
)

#scatterplot
plt.scatter(x, y, c=y, cmap="rainbow")
plt.title("Scatter Plot of Logistic Regression")
plt.show()

# Split the dataset into training and test dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

# Create a Logistic Regression Object, perform Logistic Regression
log_reg = LogisticRegression()
print(log_reg.fit(x_train, y_train))
print()

print(f"coeficient: {log_reg.coef_}")
print()

print(f"intercept: {log_reg.intercept_}")
print()

# Perform prediction using the test dataset
y_pred = log_reg.predict(x_test)
print(f"y_pred: {y_pred}")