import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

# create the data with sin function
N = 300
X = np.linspace(0, 2 * np.pi, N)
y = np.sin(X) + np.random.normal(0, 0.2, N)
# Splitting the dataset into the Training set and Test set
plt.scatter(X, y)
plt.show()
X_train, X_test, y_train, y_test = train_test_split(X.reshape(-1, 1), y.reshape(-1, 1), test_size = 0.2)
# build decision tree
r1 = DecisionTreeRegressor(max_depth = 2)
r2 = DecisionTreeRegressor(max_depth = 5)

# train a decision tree
r1.fit(X_train, y_train)
r2.fit(X_train, y_train)
# prediction
p1 = r1.predict(X_test)
p2 = r2.predict(X_test)

# visualization
plt.scatter(y_test, p1, color='blue')
plt.scatter(y_test, p2, color='red')
plt.plot(np.arange(-2, 3), np.arange(-2, 3), lw=2)
plt.show()