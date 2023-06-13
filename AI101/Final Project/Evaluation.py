import torch
import numpy as np
import pandas as pd
import seaborn as sns
from tqdm import tqdm as tqdm
import matplotlib.pyplot as plt
from Dataset import customDataset
from torch.utils.data import DataLoader
    
mainModel = torch.load('/Users/charlie/ML/AI101/Final Project/CnnModel').to('cpu')
fistModel = torch.load('/Users/charlie/ML/AI101/Final Project/FistCnnModel').to('cpu')

dfTest = pd.read_csv('/Users/charlie/ML/AI101/Final Project/sign_mnist_test.csv')
testLoader = customDataset(dfTest)
testLoader = DataLoader(testLoader, batch_size=1, drop_last=False, shuffle=False)

numberDict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

baseTestAvgAccuracy = 0
baseModelConfusionMatrix = np.zeros(shape=(26, 26))
with torch.no_grad():
    for batch in testLoader:
        X, y = batch
        outputs = mainModel(X)
        predicted = torch.argmax(outputs, axis=1)
        baseTestAvgAccuracy += (predicted == y).float().sum()
        baseModelConfusionMatrix[predicted][y] += 1
baseTestAvgAccuracy /= len(testLoader)
baseTestAvgAccuracy = baseTestAvgAccuracy.item() * 100

for i in range(26):
    baseModelConfusionMatrix[i][i] = 0
    continue

print(f"Base Model Accuracy: {baseTestAvgAccuracy}%")
sns.heatmap(baseModelConfusionMatrix)
plt.title("Base Model Confusion Matrix")
plt.show()


baseWrong = 0
fistWrong = 0
total = 0
fistTestAvgAccuracy = 0
fistModelConfusionMatrix = np.zeros(shape=(26, 26))
with torch.no_grad():
    for batch in testLoader:
        X, y = batch
        outputs = mainModel(X)
        predicted = torch.argmax(outputs, axis=1)
        #0,4,12,18
        
        if predicted == 0 or predicted == 4 or predicted == 12 or predicted == 13 or predicted == 18:
            total += 1
            if predicted != y:
                baseWrong += 1
            outputs = fistModel(X)
            predicted = torch.argmax(outputs, axis=1)
            if predicted != y:
                fistWrong += 1
            
        fistTestAvgAccuracy += (predicted == y).float().sum()
        fistModelConfusionMatrix[predicted][y] += 1
            
fistTestAvgAccuracy /= len(testLoader)
fistTestAvgAccuracy = fistTestAvgAccuracy.item() * 100

for i in range(26):
    fistModelConfusionMatrix[i][i] = 0
    continue

print(f"Fist Model Accuracy: {fistTestAvgAccuracy}%")
sns.heatmap(fistModelConfusionMatrix)
plt.title("Fist Model Confusion Matrix")
plt.show()

