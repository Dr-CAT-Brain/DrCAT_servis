import numpy as np
from PIL import Image
from pathlib import Path

from torchvision import transforms
from sklearn.neighbors import NearestNeighbors
import torch

import warnings
import pickle

from web.models import Treatment

warnings.filterwarnings(action='ignore', category=DeprecationWarning)

RESCALE_SIZE = 32
TRAIN_DIR = Path('knn_img/train')
TEST_DIR = 'knn_img/test/'


class KNN:
    def __init__(self):
        self.neighbours = None
        self.treatments = []

    def fit(self, treatments: list):
        X = [KNN.to_tensor(treatment.snapshot) for treatment in treatments]
        self.neighbours = NearestNeighbors().fit(X)
        self.treatments = treatments

    def save_model(self, file_name):
        assert self.neighbours

        with open(file_name + '.pkl', 'wb') as le_dump_file:
            pickle.dump(self.neighbours, le_dump_file)

        with open(file_name + '_file_names' + '.pkl', 'wb') as le_dump_file:
            pickle.dump(self.treatments, le_dump_file)

    def load_form_file(self, file_name):
        self.neighbours = pickle.load(open(file_name + '.pkl', 'rb'))
        self.treatments = pickle.load(open(file_name + '_file_names' + '.pkl', 'rb'))

    def predict(self, treatment: Treatment, num=1) -> set:
        assert self.neighbours
        distance, indexes = self.neighbours.kneighbors([KNN.to_tensor(treatment.snapshot)], num)

        similar_files = set()

        for i in indexes[0]:
            similar_files.add(self.treatments[int(i)])

        return similar_files

    @staticmethod
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

