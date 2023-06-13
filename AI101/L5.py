import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('/Users/charlie/ML/AI101/Data.csv')
print(df.isna().sum().sum())

imputer = sklearn.impute.SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(df.iloc[:,1:3])
df.iloc[:,1:3] = imputer.transform(df.iloc[:,1:3])
print(df.isna().sum().sum())

plt.figure(figsize=(10, 4))
plt.subplot(1,2,1)
plt.plot(df['Age'])
plt.subplot(1,2,2)
plt.plot(df['Salary'])

sns.jointplot(x='Age', y='Salary', data=df, kind='reg')

df.to_csv('/Users/charlie/ML/AI101/Data_Filled.csv', index=False)