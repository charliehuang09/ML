import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# read in Data
df = pd.read_csv('/Users/charlie/ML/AI101/Ecommerce_Customers.csv')
# data basic information
df.info()
# some descriptive statistics
df.describe()
# Exploratory Data Analysis
sns.pairplot(df)
plt.show()
X = df.iloc[:,3:7].values
y = df.iloc[:,7].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
lm = LinearRegression()
lm.fit(X_train, y_train)
print(lm.intercept_)
print(lm.coef_)



