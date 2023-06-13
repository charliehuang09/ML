import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# load the dataset:
data = pd.read_csv('/Users/charlie/ML/AI101/smsspamcollection.tsv', sep='\t')
print(data.head())
# Check for missing values:
data.isnull().sum()
# ham and spam* label
data['label'].unique
data['label'].value_counts()
# visualization
plt.hist(data[data['label']=='ham']['length'], bins=np.linspace(0, 600, 50))
plt.show()

plt.hist(data[data['label']=='spam']['length'], bins=np.linspace(0, 600, 50))
plt.show()

plt.hist(data[data['label']=='ham']['punct'], bins=np.linspace(0, 600, 50))
plt.show()

plt.hist(data[data['label']=='spam']['punct'], bins=np.linspace(0, 600, 50))
plt.show()
# determine X and y
X = data[['length', 'punct']]
y = data['label']
# Split the data
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2)

lr_model = LogisticRegression()

lr_model.fit(Xtrain, ytrain)

predictions = lr_model.predict(Xtest)

print(confusion_matrix(ytest, predictions))
print(classification_report(ytest, predictions))
# ========================= now work on text embedding
X = data['message']
y = data['label']
# Text preprocessing, tokenizing and filter out stopwords with CountVectorizer

count_vect = CountVectorizer()
X_counts = count_vect.fit(X)
print(X.shape)
# print(X_counts.shape)

Xtrain, Xtest, ytrain, ytest = train_test_split(X_counts, y, test_size=0.2)

lr_model = LogisticRegression()

lr_model.fit(Xtrain, ytrain)

predictions = lr_model.predict(Xtest)

print(confusion_matrix(ytest, predictions))
print(classification_report(ytest, predictions))
# ========================= TF-IDF approach
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X)

Xtrain, Xtest, ytrain, ytest = train_test_split(X_tfidf, y, test_size=0.2)

lr_model = LogisticRegression()

lr_model.fit(Xtrain, ytrain)

predictions = lr_model.predict(Xtest)

print(confusion_matrix(ytest, predictions))
print(classification_report(ytest, predictions))





