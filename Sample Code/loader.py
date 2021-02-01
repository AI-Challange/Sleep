import csv
import os
import numpy as np
from torch.utils import data
from torchvision import datasets, transforms
import random
from multiprocessing import cpu_count
import torch
from PIL import Image

def transform_image(image):
    custom_transformer = transforms.Compose([
                transforms.ToTensor(),
                ])
    image_tr = custom_transformer(image)

    return image_tr

def convert_label(label) :
    if label == 'Wake' : label = 0
    elif label == 'N1' : label = 1
    elif label == 'N2' : label = 2
    elif label == 'N3' : label = 3
    elif label == 'REM' : label = 4
    else : label = None

    return label
    

class CustomDataset(data.Dataset):
    def __init__(self, phase='train', root=''):
        self.root = root
        self.phase = phase
        self.data = {}

        path = os.path.join(root,self.phase+'set-for_user.csv')

        f = open(path, 'r', encoding='utf-8-sig')
        rdr = csv.reader(f)
        
        lst_img = []
        lst_label = []
        for idx, item in enumerate(rdr):
            path_img = os.path.join(self.root, item[0], item[1])
            if self.phase == 'train' or self.phase == 'validation' :
                label = item[2]
                label = convert_label(label)
            else : label = -1

            lst_img.append(path_img)
            lst_label.append(label)

        self.data['image'] = lst_img
        self.data['label'] = lst_label
        

    def __getitem__(self, index):
        path = self.data['image'][index]
        img = Image.open(path)
        img = transform_image(img)
        label = self.data['label'][index]
        return img, label
        
    def __len__(self):
        return len(self.data['image'])


def data_loader(phase, path_dataset = '../DATA', batch_size = 32, num_workers = 1):
    
    dataset = CustomDataset(phase=phase, root=path_dataset)

    if phase == 'train'  or phase =='validation':
        dataloader = data.DataLoader(dataset=dataset, batch_size=batch_size, num_workers = num_workers, shuffle=True)

    else :
        dataloader = data.DataLoader(dataset=dataset, batch_size=batch_size, num_workers = num_workers, shuffle=False)

    return dataloader

