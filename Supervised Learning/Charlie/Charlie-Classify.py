
import torchvision.transforms as transforms
import torch
import cv2
import os
from huggingface_hub import hf_hub_download
# classes = {
#     0:'No Charlie',
#     1:'Yes Charlie'
# }
path = hf_hub_download(repo_id="bennyeatspants/Charlie", filename="model")
if torch.backends.mps.is_built() and torch.backends.mps.is_available():
    device = torch.device('mps')
else:
    device = torch.device('cpu')

print(device)

model = torch.load(path,map_location=device)
model = model.eval()
cam_port = 0
cam = cv2.VideoCapture(cam_port)
result, image = cam.read()

mean = [0.5108, 0.4802, 0.4441]
std = [0.2262, 0.2051, 0.1806]
transforms_ = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize(256),
    transforms.RandomHorizontalFlip(p = 0.25),
    transforms.Normalize(mean=mean, std=std)
])

img = cv2.imread('/Users/charlie/ML/Charlie/Charlie-Data-Current/Test.jpg')
img = transforms_(img).float()
img = img.unsqueeze(0)
output = model(img.to(device))
_, yes_charlie = torch.max(output.data, 1)
yes_charlie = yes_charlie.item()

id = 'd'
no = 0
yes = 0
index = 204
cv2.waitKey(1000 * 5)
while True:
    for i in range(60):
        result, image_ = cam.read()
        if result:
            img = image_
            img = transforms_(img).float()
            img = img.unsqueeze(0)
            output = model(img.to(device))
            _, predicted = torch.max(output.data, 1)
            if predicted == yes_charlie:
                yes = yes + 1
                print('Yes')

                if index < 10000:
                    cv2.imwrite(os.path.join('/Users/charlie/ML/Charlie/Charlie-Data-Current/False' , id + str(index) + '.jpg'), image_)
                    index = index + 1
            else:
                no = no + 1
                print('No')

                # if index < 10000:
                #     cv2.imwrite(os.path.join('/Users/charlie/ML/Charlie/Charlie-Data-Current/True' , id + str(index) + '.jpg'), image_)
                #     index = index + 1

        # cv2.imwrite(os.path.join('/Users/charlie/ML/Charlie/True' , str(index) + '.jpg'), image_)
        # index = index + 1

        cv2.waitKey(1000)
    print(f"On commputer: {round(yes / 60)} Touching Grass: {round(no / 60)}")