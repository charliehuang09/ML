import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def abline(slope, intercept=0):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')
    
# read in data
df = pd.read_csv('/Users/charlie/ML/AI101/USA_Housing.csv')
# data basic information
df.info()
# some descriptive statistics
df.describe()
# some simple plots to check out the data
sns.pairplot(df)
plt.show()

# Training a Linear Regression Model
# define inpedendent variable X and depedent varaible y 
X = df.iloc[:,:5].values
y = df.iloc[:,5].values
# pre-processing:
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
# initialize a model
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
# train the model
lm.fit(X_train, y_train)
print("============ parameters")
lm.intercept_
lm.coef_
# model evaluation
from sklearn import metrics
predictions = lm.predict(X_test)
print('RMSE:')
print(np.sqrt(metrics.mean_squared_error(y_test, predictions)))
print('R2:')
print(metrics.r2_score(y_test, predictions))
# bonus, least square solution
X = np.insert(X_train, 0, 1, axis=1)
XT = np.transpose(X)
XT_X = np.dot(XT, X)
XT_X_1 = np.linalg.inv(XT_X)
XT_X_1_XT = np.dot(XT_X_1, XT)
coefficients = np.dot(XT_X_1_XT, y_train.reshape(-1, 1))
print("============ least square solution")
print(coefficients[1:])
print("============ sklearn solution")
print(lm.coef_)

plt.scatter(y_test, predictions)
abline(1)