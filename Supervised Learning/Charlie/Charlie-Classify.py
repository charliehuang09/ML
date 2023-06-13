
import torchvision.transforms as transforms
import torch
import cv2
import os
# from huggingface_hub import hf_hub_download
# classes = {
#     0:'No Charlie',
#     1:'Yes Charlie'
# }
# path = hf_hub_download(repo_id="bennyeatspants/Charlie", filename="model")
if torch.backends.mps.is_built() and torch.backends.mps.is_available():
    device = torch.device('mps')
else:
    device = torch.device('cpu')

print(device)
path = '/Users/charlie/ML/Supervised Learning/Charlie/model'
model = torch.load(path, map_location=device)
model = model.eval()
cam_port = 0
cam = cv2.VideoCapture(cam_port)
exit()
result, image = cam.read()

mean = [0.5, 0.5, 0.5]
std = [0.2, 0.2, 0.2]
transforms_ = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize(512),
    transforms.RandomHorizontalFlip(p = 0.25),
    transforms.Normalize(mean=mean, std=std)
])
no = 0
yes = 0
index = len(os.listdir('/Users/charlie/ML/Supervised Learning/Charlie/Charlie-Data/No_Charlie') + os.listdir('/Users/charlie/ML/Supervised Learning/Charlie/Charlie-Data/Yes_Charlie'))
cv2.waitKey(1000 * 2.5)
while True:
    for i in range(60):
        result, image_ = cam.read()
        if result:
            
            img = image_
            img = transforms_(img).float()
            img = img.unsqueeze(0)
            output = model(img.to(device))
            _, predicted = torch.max(output.data, 1)
            if predicted == 1:
                yes = yes + 1
                print('Yes')
                #cv2.imwrite(os.path.join('/Users/charlie/ML/Supervised Learning/Charlie/Charlie-Data/No_Charlie' , str(index) + '.jpg'), image_)
                index = index + 1
            else:
                no = no + 1
                print('No')
                # cv2.imwrite(os.path.join('/Users/charlie/ML/Supervised Learning/Charlie/Charlie-Data/Yes_Charlie', str(index) + '.jpg'), image_)
                index = index + 1

        cv2.waitKey(1000)
    # print(f"On commputer: {round(yes / 60)} Touching Grass: {round(no / 60)}")