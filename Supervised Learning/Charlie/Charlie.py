import torch
from PIL import Image
from torch import nn, save, load
from torch.optim import Adam
from torch.utils.data import DataLoader, random_split
from torchvision import datasets
from torchvision.transforms import ToTensor
import torchvision.transforms as transforms
import torch.optim as optim
#from torchsummary import summary
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
# transforms.ColorJitter()
# transforms.autoaugment()
# transforms.RandomPerspective()

if torch.backends.mps.is_built() and torch.backends.mps.is_available():
    device = torch.device('mps')

path = '/Users/charlie/ML/Supervised Learning/Charlie/Charlie-Data'


class AddGaussianNoise(object):
    def __init__(self, mean=0., std=1.5):
        self.std = std
        self.mean = mean

    def __call__(self, tensor):
        return tensor + torch.randn(tensor.size()) * self.std + self.mean

    def __repr__(self):
        return self.__class__.__name__ + '(mean={0}, std={1})'.format(self.mean, self.std)


class changeType(object):
    def __init__(self):
        return

    def __call__(self, tensor):
        return tensor.type('torch.uint8')


def get_mean_and_std(loader):
    mean = 0.
    std = 0.
    count = 0
    pbar = tqdm(loader)
    for batch in pbar:
        images, _ = batch
        curr_count = images.size(0)
        images = images.view(curr_count, images.size(1), -1)
        mean += images.mean(2).sum(0)
        std += images.std(2).sum(0)
        count += curr_count

    mean /= count
    std /= count
    return mean, std


mean = [0.5, 0.5, 0.5]
std = [0.2, 0.2, 0.2]
print(mean, std)

transforms_ = transforms.Compose([
    transforms.AugMix(),
    transforms.ToTensor(),
    transforms.Resize(512),
    transforms.RandomHorizontalFlip(p=0.25),
    transforms.Normalize(mean=mean, std=std),
    AddGaussianNoise(),
    transforms.RandomPerspective(distortion_scale=0.5),
])
data = datasets.ImageFolder(root=path, transform=transforms_)
train, valid = random_split(data, [len(data) - 50, 50])
trainloader = DataLoader(train, batch_size=4, shuffle=True)
validloader = DataLoader(valid, batch_size=4, shuffle=True)

images, label = next(iter(trainloader))
plt.imshow(np.transpose(images[0].numpy(), (1, 2, 0)))

model = models.resnet18(pretrained=True).to(device)
for param in model.parameters():
    param.requires_grad = False
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 2)

criterion = nn.CrossEntropyLoss().to(device)
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
# optimizer = Adam(model.parameters(), lr=0.01)

# lambda1 = lambda epoch: epoch / 10
# scheduler = torch.optim.lr_scheduler.MultiplicativeLR(optimizer, lr_lambda=lambda1)

max_accuracy = 0
model = model.to(device)
criterion = criterion.to(device)
for epoch in range(3):
    model.train()
    model_loss = 0
    pbar = tqdm(trainloader)
    for batch in pbar:
        X, y = batch
        X = X.to(device)
        y = y.to(device)
        outputs = model(X)
        loss = criterion(outputs, y)
        model_loss += loss.item()
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    # scheduler.step()
    model_loss /= len(trainloader)
    model.eval()
    correct = 0
    incorrect = 0
    for batch in validloader:
        X, y = batch
        X = X.to(device)
        y = y.to(device)
        outputs = model(X)
        _, preditced = torch.max(outputs.data, 1)
        correct += (preditced == y).float().sum()
        incorrect += (preditced != y).float().sum()
    print(
        f"Epoch: {epoch + 1} Accuracy: {correct / (correct + incorrect) * 100} Loss: {model_loss}")
    if max_accuracy <= correct / (correct + incorrect):
        max_accuracy = correct / (correct + incorrect)
        torch.save(model, 'model')
        print('Saved')
print(max_accuracy)

torch.save(model, 'model')

correctImg = []
correctImgLabel = []
wrongImg = []
wrongImgLabel = []
for batch in validloader:
    X, y = batch
    X = X.to(device)
    y = y.to(device)
    model = model.to(device)
    outputs = model(X)
    _, preditced = torch.max(outputs.data, 1)
    for i in range(len(preditced)):
        if (preditced[i] == y[i]):
            correctImg.append(np.transpose
                              (X[i].to('cpu').numpy()))
            correctImgLabel.append(y[i])
        else:
            wrongImg.append(np.transpose(X[i].to('cpu').numpy()))
            wrongImgLabel.append(y[i])


def displayImg(input, label):
    plt.figure()
    f, axarr = plt.subplots(len(input) + 1, 1)
    for i in range(len(input)):
        axarr[i][0].imshow(input[i])

#np.transpose(wrongimg, axes=(1,0,2))


displayImg(wrongImg, wrongImgLabel)
