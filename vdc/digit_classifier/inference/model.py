import PIL
from PIL import Image, ImageDraw,ImageTk
import torch.nn.functional as F
import torch.nn as nn
import torch
import numpy as np
from torchvision import transforms
import matplotlib.pyplot as plt
from pathlib import Path

transform1 = transforms.Compose([transforms.ToTensor(), transforms.Resize((28,28)),
                                transforms.Normalize((0.5),(0.5))])

class classifier(nn.Module):
  def __init__(self, in_features, h1, h2, out_features):
    super().__init__()
    self.linear1=nn.Linear(in_features, h1)
    self.linear2 = nn.Linear(h1, h2)
    self.linear3=nn.Linear(h2,out_features)
  def forward(self, x):
    x = F.relu(self.linear1(x))
    x = F.relu(self.linear2(x))
    x = self.linear3(x)
    return x

model = classifier(784, 125, 65, 10)
model.load_state_dict(torch.load("D:/Stud/AI/programs and projects/Visual digit classifier/vdc/digit_classifier/inference/model/MNIST-97%.pt"))

def im_convert(tensor):
  image = tensor.clone().detach().cpu().numpy()
  image = image.transpose(1,2,0)
  image = image * np.array((0.5,0.5,0.5))/np.array((0.5,0.5,0.5))
  image = image.clip(0,1)
  return image


def recognize(file_path):
    guess={}
    img = Image.open(file_path)
    img = img.convert('1')
    img = transform1(img)
    plt.imshow(im_convert(img))
    plt.show()
    img=img.view(img.shape[0], -1)
    outputs = model(img)
    _,pred=torch.max(outputs,1)
    print(pred.item())
  
    return pred.item()