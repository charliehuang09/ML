import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

def Normalization(df):
    min = df.min()
    max = df.max()
    return (df - min) / (max - min)
def Standerdization(df):
    mean = df.mean()
    std = df.std()
    return (df - df.mean()) / std

df = pd.read_csv('/Users/charlie/ML/AI101/Data.csv')
print(Normalization(df['Age']))
print(Standerdization(df['Age']))

plt.subplot(1,2,1)
plt.hist(Normalization(df['Age']))
plt.subplot(1,2,2)
plt.hist(Standerdization(df['Age']))