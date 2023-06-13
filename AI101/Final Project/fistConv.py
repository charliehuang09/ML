import torch
import warnings
import numpy as np
import pandas as pd
from torch import nn
import seaborn as sns
from Eval import evalModel
import torch.optim as optim
from tqdm import trange, tqdm
from torchvision import models
from Model import mainConvModel
import matplotlib.pyplot as plt
from torchsummary import summary
from Dataset import customDataset
from torch.optim import SGD, Adam
from torch.utils.data import DataLoader
warnings.filterwarnings("ignore")
if torch.backends.mps.is_built() and torch.backends.mps.is_available():
    device = torch.device('mps')

dfTrain = pd.read_csv('/Users/charlie/ML/AI101/Final Project/sign_mnist_train.csv')
dfTest = pd.read_csv('/Users/charlie/ML/AI101/Final Project/sign_mnist_test.csv')

A = dfTrain[dfTrain['label']==0]
E = dfTrain[dfTrain['label']==4]
M = dfTrain[dfTrain['label']==12]
N = dfTrain[dfTrain['label']==13]
S = dfTrain[dfTrain['label']==18]
dfTrain = pd.concat([A, E, M, N, S])
A = dfTest[dfTest['label']==0]
E = dfTest[dfTest['label']==4]
M = dfTest[dfTest['label']==12]
N = dfTest[dfTest['label']==13]
S = dfTest[dfTest['label']==18]
dfTest = pd.concat([A, E, M, N, S])

trainLoader = customDataset(dfTrain)
testLoader = customDataset(dfTest)
trainLoader = DataLoader(trainLoader, batch_size=128, drop_last=True, shuffle=True)
testLoader = DataLoader(testLoader, batch_size=128, drop_last=True, shuffle=True)

model = mainConvModel()
model = model.to(device)
criterion = nn.CrossEntropyLoss().to(device)
# optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
optimizer = optim.Adam(model.parameters())


maxAccuracy = 0
for epoch in range(50):
    model.train()
    pbar = trainLoader
    # pbar = tqdm(trainLoader)
    trainLoss = 0
    for batch in pbar:
        X, y = batch
        X = X.to(device)
        y = y.to(device)
        outputs = model(X)
        loss = criterion(outputs, y)
        trainLoss += loss.item()
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    model.eval()
    pbar = testLoader
    testCorrect = 0
    with torch.no_grad():
        for batch in pbar:
            X, y = batch
            X = X.to(device)
            y = y.to(device)
            outputs = model(X)
            predicted = torch.argmax(outputs, axis=1)
            # _, preditced = torch.max(outputs.data, 1)
            testCorrect += (predicted == y).float().sum()
    maxAccuracy = max(maxAccuracy, testCorrect / (len(testLoader) * 128) * 100)
    print(f"Epoch: {epoch + 1} Train Loss {trainLoss}")
    print(f"Accuracy: {testCorrect / (len(testLoader) * 128) * 100}")


print(maxAccuracy)

# torch.save(model, '/Users/charlie/ML/AI101/Final Project/FistCnnModel')
# model = torch.load('/Users/charlie/ML/AI101/Final Project/MainCnnModel')



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
            # if predicted[i] != y[i]:
            #     continue
            #     plt.imshow(X[i][0].to('cpu'))
            #     plt.title(f"Predicted : {predicted[i].item()} Ground Truth: {y[i].item()}")
            #     plt.show()

for i in range(26):
    confusionMatrix[i][i] = 0

sns.heatmap(confusionMatrix / (len(testLoader) * 128))



