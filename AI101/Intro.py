import torch
from PIL import Image
from torch import nn, save, load
from torch.optim import Adam
from torch.utils.data import DataLoader, random_split
from torchvision import datasets
from torchvision.transforms import ToTensor
import torchvision.transforms as transforms
import torch.optim as optim
import torch.optim.lr_scheduler as scheduler
from tqdm import trange, tqdm
import numpy as np
from torch.utils.data.sampler import BatchSampler
import matplotlib.pyplot as plt
from torchvision import models
from torch.optim import lr_scheduler
from collections import Counter
import math
import matplotlib.image as mpimg
from pytorch_model_summary import summary

device = torch.device('mps')

path = '/Users/charlie/ML/Supervised Learning/Charlie/Charlie-Data'