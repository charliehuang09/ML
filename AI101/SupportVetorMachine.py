import pandas as pd
from sklearn import svm
import numpy as np
import seaborn as sns
path = '/Users/charlie/ML/AI101/Pumpkin_Seeds_Dataset.xlsx'
df = pd.read_excel(path)
df['Class'] = df['Class'].map({'Çerçevelik':1,'Ürgüp Sivrisi':0})

corr = df.iloc[:,:-1].corr()
sns.heatmap(corr, vmin=-1.0, vmax=1.0, annot=True, fmt='.1f')

clf = svm.SVC(kernel='linear')

clf.fit(df.drop(columns=['Class']), df['Class'])

outputs = clf.predict(df.drop(columns=['Class']))

accuracy = (outputs == df['Class']).sum() / len(df.index)


