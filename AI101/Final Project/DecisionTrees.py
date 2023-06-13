import pandas as pd
from tqdm import trange as trange
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
import seaborn as sns
import matplotlib.pyplot as plt
from timeit import default_timer as timer

trainDf = pd.read_csv('/Users/charlie/ML/AI101/Final Project/sign_mnist_train.csv')
testDf = pd.read_csv('/Users/charlie/ML/AI101/Final Project/sign_mnist_test.csv')

Xtrain = trainDf.drop(columns=['label'])
Ytrain = trainDf['label']

Xtest = testDf.drop(columns=['label'])
Ytest = testDf['label']

model = DecisionTreeClassifier(criterion='entropy', splitter='random')
start = timer()
model.fit(Xtrain, Ytrain)
time = timer() - start
outputs = model.predict(Xtest)
accuracy = accuracy_score(Ytest, outputs)

print("")
print(f"{round(accuracy * 100)}%")
print(f"Time: {round(time, 3)}")
plot_tree(model)
plt.show()