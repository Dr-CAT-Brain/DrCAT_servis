import os
import pathlib

import torch
import pickle
import numpy as np
from torch.utils.data import DataLoader
import torch.nn as nn

from neuronet.KTDataset import KTDataset
from neuronet.Net import SimpleCnn

num_classes = 14
base_model = SimpleCnn(num_classes)

weights_absolute_path = os.path.abspath('neuronet/KT_base_v2_last.pth')
base_model.load_state_dict(torch.load(weights_absolute_path, map_location=torch.device('cpu')))

encoder_absolute_path = os.path.abspath('neuronet/label_encoder_v2.pkl')
label_encoder = pickle.load(open(encoder_absolute_path, 'rb'))


def predict(model, test_loader):
    with torch.no_grad():
        logits = []

        for inputs in test_loader:
            model.eval()
            outputs = model(inputs).cpu()
            logits.append(outputs)

    probs = nn.functional.softmax(torch.cat(logits), dim=-1).numpy()
    return probs


def predict_picture(full_path):
    # full_path = os.path.abspath('' + file_name)
    test_files = [str(pathlib.PurePosixPath(full_path))]
    test_dataset = KTDataset(test_files, mode="test")
    test_loader = DataLoader(test_dataset, shuffle=False, batch_size=64)
    probs = predict(base_model, test_loader)
    predicted_proba = np.max(probs) * 100
    y_pred = np.argmax(probs)
    predicted_label = label_encoder.classes_[y_pred]
    return predicted_label, predicted_proba


if __name__ == '__main__':
    print(predict_picture("3D_MPR_-_SHISHKINA_N.M._66y_-_11.10.2020_19_24_51_-_Head__1.5__J30s_0085.jpg"))
