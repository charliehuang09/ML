import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/charlie/ML/AI101/advertising.csv')
X = df.iloc[:, [0,1,2,3,6]]
y = df.iloc[:,9].values
plt.hist(y)
plt.show()

sns.pairplot(df, hue='Clicked on Ad')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

LR = LogisticRegression(max_iter=500)
LR.fit(X, y)
output = LR.predict(X_test)
cm = confusion_matrix(y_test, output)
print(cm)
accuracy = (cm[0][0] + cm[1][1]) / np.sum(cm)
print(LR.intercept_)
print(LR.coef_)