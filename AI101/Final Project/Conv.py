import torch
import warnings
import numpy as np
import pandas as pd
from torch import nn
import seaborn as sns
from Model import mainConvModel
import torch.optim as optim
import matplotlib.pyplot as plt
from Dataset import customDataset
from torch.utils.data import DataLoader
from timeit import default_timer as timer
warnings.filterwarnings("ignore")

if torch.backends.mps.is_built() and torch.backends.mps.is_available():
    device = torch.device('mps')

dfTrain = pd.read_csv('/Users/charlie/ML/AI101/Final Project/sign_mnist_train.csv')
dfTest = pd.read_csv('/Users/charlie/ML/AI101/Final Project/sign_mnist_test.csv')
trainLoader = customDataset(dfTrain)
testLoader = customDataset(dfTest)
img, label = trainLoader.__getitem__(0)
trainLoader = DataLoader(trainLoader, batch_size=128, drop_last=True, shuffle=True)
testLoader = DataLoader(testLoader, batch_size=128, drop_last=True, shuffle=True)

numberDict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


model = mainConvModel()
model = model.to(device)
criterion = nn.CrossEntropyLoss().to(device)
# optimizer = optim.SGD(model.parameters(), lr=0.0005, momentum=0.9)
optimizer = optim.Adam(model.parameters())

trainLossGraph = []
testLossGraph = []
trainAccuracyGraph = []
testAccuracyGraph = []

maxAccuracy = 0
start = timer()
for epoch in range(50):
    model.train()
    pbar = trainLoader
    trainAvgLoss = 0
    trainAvgAccuracy = 0
    for batch in pbar:
        X, y = batch
        X = X.to(device)
        y = y.to(device)
        outputs = model(X)
        predicted = torch.argmax(outputs, axis=1)
        loss = criterion(outputs, y)
        trainAvgLoss += loss.item()
        trainAvgAccuracy += (predicted == y).float().sum()
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    trainAvgLoss /= len(trainLoader) * 128
    trainAvgAccuracy /= len(trainLoader) * 128
    trainAvgAccuracy = trainAvgAccuracy.to('cpu')
    trainLossGraph.append(trainAvgLoss)
    trainAccuracyGraph.append(trainAvgAccuracy)
    model.eval()
    pbar = testLoader
    testAvgLoss = 0
    testAvgAccuracy = 0
    with torch.no_grad():
        for batch in pbar:
            X, y = batch
            X = X.to(device)
            y = y.to(device)
            outputs = model(X)
            predicted = torch.argmax(outputs, axis=1)
            loss = criterion(outputs, y)
            testAvgLoss += loss.item()
            testAvgAccuracy += (predicted == y).float().sum()
    testAvgLoss /= len(testLoader) * 128
    testAvgAccuracy /= len(testLoader) * 128
    testAvgAccuracy = testAvgAccuracy.to('cpu')
    testLossGraph.append(testAvgLoss)
    testAccuracyGraph.append(testAvgAccuracy)
    
    maxAccuracy = max(maxAccuracy, testAvgAccuracy)
    
    print(f"Epoch: {epoch} Train Loss {trainAvgLoss}")
    print(f"Accuracy: {testAvgAccuracy}")
    
time = timer() - start
print("")
print(f"Max Accuracy: {maxAccuracy}")
print(f"Time: {time}")

# torch.save(model, '/Users/charlie/ML/AI101/Final Project/CnnModel')    
# model = torch.load('/Users/charlie/ML/AI101/Final Project/CnnModel')

confusionMatrix = np.zeros(shape=(26, 26))
with torch.no_grad():
    for batch in testLoader:
        X, y = batch
        X = X.to(device)
        y = y.to(device)
        outputs = model(X)
        outputs = outputs.to('cpu')
        X = X.to('cpu')
        y = y.to('cpu')
        predicted = torch.argmax(outputs, axis=1)
        for i in range(len(predicted)):
            confusionMatrix[predicted[i]][y[i]] += 1
            if predicted[i] != y[i]:
                continue
                plt.imshow(X[i][0].to('cpu'))
                plt.title(f"Predicted : {numberDict[predicted[i].item()]} Ground Truth: {numberDict[y[i].item()]}")
                plt.show()        

for i in range(26):
    confusionMatrix[i][i] = 0

sns.heatmap(confusionMatrix / (len(testLoader) * 128))
plt.show()

plt.plot(trainAccuracyGraph, label='Train')
plt.plot(testAccuracyGraph, label='Test')
plt.legend()
plt.title('Accuracy')
plt.show()

plt.plot(trainLossGraph, label='Train')
plt.plot(testLossGraph, label='Test')
plt.legend()
plt.title('Loss')
plt.show()


    
    
    
    