# -*- coding: utf-8 -*-
"""machinelearning3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AsYjD-9f7RLDdRWN1o6L7XyHJs-8BktM
"""

import torch
from torchvision import utils
from torchvision import models
from torchvision import datasets
from torchvision import transforms

from PIL import Image
import urllib.request as request
from matplotlib import pyplot as plt

"""MODELOS PRE-ENTRENADOS"""

inception = models.inception_v3(pretrained=True)

url = 'https://demascotas.info/wp-content/uploads/2018/02/dog-1192029_1280-1024x739.jpg'
image = request.urlretrieve(url, 'test.jpg')
img = Image.open(image[0])

# utilizamos un tamaño más pequepo
# CenterCrop para que quede centrado
preprocess = transforms.Compose([
        transforms.Resize(170),
        transforms.CenterCrop(120),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456,0.406],
            std = [0.229,0.224,0.225]
        )
])

img_t = preprocess(img)
batch = torch.unsqueeze(img_t, 0)
plt.imshow(img_t.permute(1,2,0))

inception.eval()

out = inception(batch)
out

request.urlretrieve('https://gist.githubusercontent.com/ykro/acb00a36f737c12013f6e0f8a0d2cb61/raw/a2bb113b83e274048992f6550050a437fa4db76d/imagenet_classes.txt', 'labels.txt')
with open('labels.txt') as f:
    labels = [line.strip() for line in f.readlines()]

out

_, index = torch.max(out, 1)

percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
labels[index[0]], percentage[index[0]].item()

_, indices = torch.sort(out, descending=True)

top_five = indices[0][:5]
for i in top_five:
  print(labels[i], percentage[i].item())

"""Trabajando con un dataset"""

data_path = 'data/'
dataset = datasets.CIFAR10(data_path, train= True, download=True)
validation_set = datasets.CIFAR10(data_path, train= False, download=True)

classes = ['plane','car','bird','cat','deer','dog','frog','horse','ship','truck']
len(dataset)

img, label = dataset[50]
img, label , classes[label]

plt.imshow(img)

tensor_transform = transforms.ToTensor()

img_tensor = tensor_transform(img)
img, img_tensor, img_tensor.shape

dataset = datasets.CIFAR10(data_path, train= True, download=True, transform=transforms.ToTensor())

img, label = dataset[50]
img

img.max(), img.min()

plt.imshow(img.permute(1,2,0))

imgs  = torch.stack([img_tensor for img_tensor, _ in dataset], dim=3)

imgs.shape