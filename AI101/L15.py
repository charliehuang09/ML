import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn import tree
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

for i in range(5):
    plt.imshow(digits.images[i,:,:], cmap='gray')
    plt.show()

X = digits.images.reshape(1797, 64)
y = digits.target.reshape(1797, 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
c1 = DecisionTreeClassifier(max_depth = 5, criterion='entropy')
c2 = DecisionTreeClassifier(max_depth = 10, criterion='entropy')
c1.fit(X_train, y_train)
c2.fit(X_train, y_train)
p1 = c1.predict(X_test)
p2 = c2.predict(X_test)
cm1 = confusion_matrix(y_test, p1)
cm1 = confusion_matrix(y_test, p2)
ac1 = 0
for i in range(10):
    ac1  = ac1 + cm1[i][i]
ac1 = ac1 / np.sum(cm1)

fig = plt.figure(figsize = (30, 15))
tree.plot_tree(c1, fontsize = 14)
plt.show()



