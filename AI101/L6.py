import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, OneHotEncoder
# read in dataset, Data_filled.csv
df = pd.read_csv('/Users/charlie/ML/AI101/Data_Filled.csv')
# X = second and third columns


# 1) numerical data
df['Age'] = StandardScaler().fit_transform(df[['Age']].values)
df['Salary'] =  StandardScaler().fit_transform(df[['Salary']].values)
df['Country'] = LabelEncoder().fit_transform(df['Country'])
df.to_csv('/Users/charlie/ML/AI101/Data_Filled.csv')
# Standardization StandardScaler
#sc1 = StandardScaler()
#df['Age'] = sc1.fit_transform(df['Age'])
#print(df['Age'])
# normalization, MinMaxScaler
#sc2 = MinMaxScaler()
#XNum = sc2.fit_transform(XNum)
#print(XNum)
# visualization
# 2) categorical data, first column

# LabelEncoder, OneHotEncoder
#X_country = df.iloc[:,0]
#print(X_country)
##ec1 = LabelEncoder()
#ec2 = OneHotEncoder()
#X_new3 = ec1.fit_transform(X_country)
#print(X_new3)
#ec2.fit_transform(X_new3)
# save to data_scaled.csv 

