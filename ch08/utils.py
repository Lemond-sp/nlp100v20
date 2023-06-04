import numpy as np
import os
from typing import List
import torch
import torch.nn as nn
import torch.nn.functional as F

# def main():
#     for i in ["label.dev.txt","label.train.txt","text.dev.txt","text.test.txt","text.train.txt"]:
#         load_data(i)

def load_data(path: str,data: str):
    with open(os.path.join(path,data)) as f:
        list_data = f.read().split('\n')
    del list_data[len(list_data) - 1]
    return list_data

# リスト内のテキストをsplitする
def sep_list(data: List):
    for i,seq in enumerate(data):
        data[i] = seq.split(' ')
    return data

# 単層ニューラルネット
class Net(nn.Module):
    def __init__(self,input_size,feature_num):
        super().__init__()
        self.fc = nn.Linear(input_size,feature_num) # 重み初期化はデフォルトでinit.kaiming_uniform_(self.weight, a=math.sqrt(5))
    
    def forward(self,x):
        x = self.fc(x)
        return x

# 多層ニューラルネット(ans79)
class MNet(nn.Module):

    def __init__(self,input_size,feature_num):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(input_size,100)
        self.fc2 = nn.Linear(100, feature_num)
        self.fc3 = nn.Linear(feature_num, 3)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# チェックポイントの保存(ans76)
def save_checkpoint(model,optimizer,filename,epoch):
    if filename.endswith('.pt') or filename.endswith('.pth'):
        # saveはdictも保存できる
        torch.save({
            'epoch' : epoch,
            'model_state_dict' : model.state_dict(),
            'optimizer_state_dict' : optimizer.state_dict(),
        },
        filename)