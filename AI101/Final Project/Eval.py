import torch
import numpy as np
import pandas as pd
from torch.utils.data import Dataset
def evalModel(model, testLoader, device):
    model.eval()
    testCorrect = 0
    with torch.no_grad():
        for batch in testLoader:
            X, y = batch
            X = X.to(device)
            y = y.to(device)
            outputs = model(X)
            _, preditced = torch.max(outputs.data, 1)
            testCorrect += (preditced == y).float().sum()
        print(f"Accuracy: {testCorrect / (len(testLoader) * 128) * 100}")
