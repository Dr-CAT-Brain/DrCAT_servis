import numpy as np
from PIL import Image
from pathlib import Path

from torchvision import transforms
from sklearn.neighbors import NearestNeighbors
import torch

import warnings

warnings.filterwarnings(action='ignore', category=DeprecationWarning)

RESCALE_SIZE = 32
TRAIN_DIR = Path('train/all_kt')


def to_tensor(file_name):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    x = Image.open(file_name)
    x.load()
    x = x.crop((470, 0, 1449, 979))
    x = x.resize((RESCALE_SIZE, RESCALE_SIZE))
    x = np.array(x)
    x = np.array(x / 255, dtype='float32')
    x = transform(x)
    x = torch.reshape(x, (-1,))
    return x.tolist()


train_files = sorted(list(TRAIN_DIR.rglob('*.jpg')))

X = [to_tensor(file_name) for file_name in train_files]
neighbours = NearestNeighbors().fit(X)

neigh_ind = neighbours.kneighbors([to_tensor(train_files[0])])

for i in neigh_ind[1][0]:
    print(train_files[i])

test_file = Path("/content/gdrive/MyDrive/kt_test_fold/5.jpg")
neigh_ind = neighbours.kneighbors([to_tensor(test_file)], 30)
print(neigh_ind[1][0])

for i in neigh_ind[1][0]:
    print(train_files[i])


def give_KNN(file_name, num=20):
    neigh_ind = neighbours.kneighbors([to_tensor(file_name)], num)
    ressa = [train_files[i] for i in neigh_ind[1][0]]
    return ressa
