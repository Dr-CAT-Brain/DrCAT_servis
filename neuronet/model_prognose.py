import torch
import pickle
import numpy as np
from pathlib import Path
from torch.utils.data import Dataset, DataLoader
import torch.nn as nn

from Dataset import KTDataset
from Net import SimpleCnn

num_classes=14
base_model=SimpleCnn(num_classes)
base_model.load_state_dict(torch.load("KT_base_v2_last.pth", map_location=torch.device('cpu')))
label_encoder = pickle.load(open("label_encoder_v2.pkl", 'rb'))

def predict(model, test_loader):
    with torch.no_grad():
        logits = []

        for inputs in test_loader:
            model.eval()
            outputs = model(inputs).cpu()
            logits.append(outputs)

    probs = nn.functional.softmax(torch.cat(logits), dim=-1).numpy()
    return probs

def predict_picture(file_name):
    TEST_DIR = Path('C:/Users/Digitaljay/Documents/GitHub/strokes_diagnostic')

    test_files = list(TEST_DIR.rglob(file_name))

    test_dataset = KTDataset(test_files, mode="test")
    test_loader = DataLoader(test_dataset, shuffle=False, batch_size=64)
    probs = predict(base_model, test_loader)
    predicted_proba = np.max(probs)*100
    y_pred = np.argmax(probs)
    predicted_label = label_encoder.classes_[y_pred]
    return predicted_label, predicted_proba

print(predict_picture("1.jpg"))
