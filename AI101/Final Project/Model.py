import torch.nn as nn

class mainConvModel(nn.Module):

    def __init__(self):
        super(mainConvModel, self).__init__()
        self.to64conv = nn.Sequential(
            nn.Conv2d(1, 4, (3, 3)),
            nn.ReLU(),
            nn.Conv2d(4, 4, (3, 3)),
            nn.ReLU(),
            nn.Conv2d(4, 16, (3, 3)),
            nn.ReLU(),
            nn.Conv2d(16, 64, (3, 3)),
            nn.ReLU()
        )
        self.conv64 = nn.Sequential(
            nn.Conv2d(64, 64, (3, 3)),
            nn.ReLU()
        )
        self.pool = nn.Sequential(
            nn.AvgPool2d(3, 3)
        )
        self.end = nn.Sequential(
            nn.Conv2d(64, 8, (3, 3)),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(288, 25)
        )
    def forward(self, x):
        x = self.to64conv(x)
        x = self.conv64(x)
        x = self.conv64(x)
        x = self.conv64(x)
        x = self.conv64(x)
        x = self.conv64(x)
        x = self.conv64(x)
        x = self.end(x)
        return x
        
  