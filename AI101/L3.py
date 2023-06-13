import seaborn as sns
import pandas as pd

whitePath = '/Users/charlie/ML/AI101/winequality-white.csv'
redPath = '/Users/charlie/ML/AI101/winequality-red.csv'

whiteWine = pd.read_csv(whitePath, sep=';')
redWine = pd.read_csv(redPath, sep=';')
whiteWine['wine_type'] = 'white'
redWine['wine_type'] = 'red'

wine = pd.concat([whiteWine, redWine])

#sns.lineplot(wine['sulphates'][:100])

#sns.histplot(wine['sulphates'][:100], bins=20)

#sns.barplot(x='quality', y = 'sulphates', data=wine)
#sns.barplot(x='quality', y = 'sulphates', hue = 'wine_type', data=wine)

#sns.violinplot(x='quality', y = 'sulphates', hue = 'wine_type', data=wine, split=True)

corr = wine.iloc[:,:-1].corr()
sns.heatmap(corr, vmin=-1.0, vmax=1.0, annot=True, fmt='.1f')

sns.jointplot(x='sulphates', y='alcohol', data=wine, kind='reg')