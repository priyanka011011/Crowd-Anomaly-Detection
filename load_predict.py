import os
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import pickle

# Load the trained model
iris_model = nn.Sequential(
            nn.Linear(4,32),
            nn.Tanh(),
            nn.Linear(32,3),
            nn.LogSoftmax(dim=1))

# iris_model.load_state_dict(torch.load('/kaggle/input/iris-pymodel/iris_model.pt'))

iris_model.load_state_dict(torch.load("C:\\Users\\HOME\\Zummit_2023\\model_template.pt"))

iris_model.eval() # переводим модель в режим применения
input_tensor = torch.tensor([[4.9,2.4,3.3,1.0]])

# Predictions
outputs = iris_model(input_tensor)
outputs = iris_model(input_tensor)

_, predicted = torch.max(outputs, dim=1)

print('Output Tensor:\n', outputs)
print('\nTorch Max Function Result: ', predicted)