from sklearn.model_selection import train_test_split
import pandas as pd
df = pd.read_csv('/Users/charlie/ML/AI101/Data_Filled.csv')
df = df.drop(columns=['Unnamed: 0.1', 'Unnamed: 0'])
train, test = train_test_split(df, test_size=0.2, stratify=True)
X_train = train.drop(columns=['Purchased'])
Y_train = train['Purchased']
X_test = test.drop(columns=['Purchased'])
Y_test = test['Purchased']
train.to_csv('/Users/charlie/ML/AI101/Data_Train.csv')
test.to_csv('/Users/charlie/ML/AI101/Data_Test.csv')