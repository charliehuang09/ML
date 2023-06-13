import torch
import numpy as np
import pandas as pd
from torch.utils.data import Dataset

class customDataset():
    def __init__(self, df):
        self.df = df
        
    def __len__(self):
        return len(self.df)
    
    def __getitem__(self, index):
        #28 28
        y = self.df.iloc[index]
        y = y[0]
        # y = torch.tensor([y])
        img = self.df.iloc[index]
        img = img[1:]
        img = img.values
        img = np.float32(img)
        img = img.reshape(1, 28, 28)
        img = torch.from_numpy(img)
        return (img, y)
        