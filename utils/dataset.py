import pandas as pd
import numpy as np
#from skimage import io
#from skimage.transform import resize

import torch
from torch.utils.data import Dataset




class MnistTrain(Dataset):

   # def _vectorized(self, label):
   #     vector = np.zeros((1,10), dtype=np.int64)
   #     vector[0, label] = 1
   #     return vector

    def __init__(self, csv_train_path):
        self.dataset = pd.read_csv(csv_train_path)

    
    def __len__(self):
        return len(self.dataset)
    
    def __getitem__(self, index):
        data = self.dataset.iloc[index].values
        label, image = np.split(data, [1])
        #label = self._vectorized(label)
        image = np.reshape(image, (28, 28)).astype(np.float32)
        #image = resize(image, (228, 228)).astype(np.float32)
        return label, image


class MnistTest(Dataset):

    def __init__(self, csv_test_path):
        self.dataset = pd.read_csv(csv_test_path)
    
    def __len__(self):
        return len(self.dataset)
    
    def __getitem__(self, index):
        image = self.dataset.iloc[index].values
        image = np.reshape(image, (28, 28)).astype(np.float32)
        return index + 1, image