# 損失と正解率のプロット
import os
from tqdm import tqdm
import time
import numpy as np
from matplotlib import pyplot as plt
import torch
from torch import nn
from torch.utils.data import TensorDataset,DataLoader
import torch.optim as optim
from sklearn.metrics import accuracy_score
from utils import Net
import pickle

BATCH_SIZE = 128
train_loss = []
valid_loss = []
train_acc = []
valid_acc = []

def main():
    tensor_path = 'contents/output'
    x_train,x_valid,x_test,y_train,y_valid,y_test = make_tensor(tensor_path)
    train_loader,val_loader,_ = make_dataloader(x_train,x_valid,x_test,y_train,y_valid,y_test)
    feature_num = 4
    net = Net(300,feature_num=feature_num)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print('using device:', device)
    net = net.to(device)

    # 損失
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.01)
    criterion = nn.CrossEntropyLoss()
    max_epoch = 30

    # 学習
    for epoch in tqdm(range(max_epoch)):
        start = time.time()
        # ミニバッチ学習
        for batch in train_loader:

            # バッチサイズ分のサンプルを抽出
            x, t = batch
            # データをGPUへ転送
            x = x.to(device)
            t = t.to(device)

            # 勾配を初期化
            optimizer.zero_grad()
            y = net(x)
            loss = criterion(y, t)
            # 誤差逆伝播
            loss.backward()
            optimizer.step()
        
        # 更新と切り離し、検証データの性能を確認
        with torch.no_grad():
            x_train = x_train.to(device)
            y_train = y_train.to(device)
            y_pred = net(x_train)
            loss = criterion(y_pred,y_train).item()
            acc = tensor_acc(y_pred,y_train)
            train_loss.append(loss)
            train_acc.append(acc)
            # データをGPUへ転送
            x_valid = x_valid.to(device)
            y_valid = y_valid.to(device)
            y_pred = net(x_valid)
            loss = criterion(y_pred,y_valid).item()
            acc = tensor_acc(y_pred,y_valid)
            valid_loss.append(loss)
            valid_acc.append(acc)
        end = time.time()
        print(f'BATCH : {BATCH_SIZE} time : {end - start} sec')
    
    # 損失と正解率のプロット
    fig, ax = plt.subplots(1, 2, figsize=(15, 5))
    ax[0].plot(np.array(train_loss), label='train')
    ax[0].plot(np.array(valid_loss), label='valid')
    ax[0].set_xlabel('epoch')
    ax[0].set_ylabel('loss')
    ax[0].legend()
    ax[1].plot(np.array(train_acc), label='train')
    ax[1].plot(np.array(valid_acc), label='valid')
    ax[1].set_xlabel('epoch')
    ax[1].set_ylabel('accuracy')
    ax[1].legend()
    plt.savefig('ans75.png')
    plt.show()

def make_tensor(tensor_path):
    x_train = torch.load(os.path.join(tensor_path,'x_train.pt'))
    x_valid = torch.load(os.path.join(tensor_path,'x_valid.pt'))
    x_test = torch.load(os.path.join(tensor_path,'x_test.pt'))
    y_train = torch.load(os.path.join(tensor_path,'y_train.pt'))
    y_valid = torch.load(os.path.join(tensor_path,'y_valid.pt'))
    y_test = torch.load(os.path.join(tensor_path,'y_test.pt'))
    return x_train,x_valid,x_test,\
            y_train,y_valid,y_test

def make_dataloader(x_train,x_valid,x_test,y_train,y_valid,y_test):
    train = TensorDataset(x_train, y_train)
    val = TensorDataset(x_valid, y_valid)
    test = TensorDataset(x_test, y_test)
    batch_size = BATCH_SIZE

    train_loader = DataLoader(train, batch_size, shuffle=True)
    val_loader = DataLoader(val, batch_size, shuffle=False)
    test_loader = DataLoader(test, 1, shuffle=False)
    return train_loader,val_loader,test_loader

def tensor_acc(pred,true):
    pred = pred.to('cpu').detach().numpy().copy()
    true = true.to('cpu').detach().numpy().copy()
    pred = np.argmax(pred,axis=1)
    return accuracy_score(pred,true)
if __name__ == "__main__":
    main()


'''
重みW 初期値
Parameter containing:
tensor([[ 0.0163, -0.0164, -0.0053,  ...,  0.0316, -0.0479,  0.0250],
        [-0.0536,  0.0158,  0.0495,  ...,  0.0320,  0.0336, -0.0050],
        [-0.0130,  0.0472, -0.0404,  ..., -0.0021, -0.0536, -0.0430],
        [-0.0502,  0.0328,  0.0325,  ...,  0.0002, -0.0337, -0.0489]],
       requires_grad=True)
重みW 学習後
Parameter containing:
tensor([[ 0.0140, -0.0123, -0.0079,  ...,  0.0404, -0.0369,  0.0124],
        [-0.0554,  0.0131,  0.0546,  ...,  0.0321,  0.0266, -0.0034],
        [-0.0034,  0.0506, -0.0500,  ..., -0.0132, -0.0511, -0.0376],
        [-0.0557,  0.0280,  0.0396,  ...,  0.0024, -0.0401, -0.0433]],
       requires_grad=True)

true = tensor([     2,      2,      0,      2,      0,      0,      0,      2,      2,
             2,      2,      0,      2,      0,      2,      0,      1,      1,
             2,      0,      2,      0,      2,      0,      0,      0,      0,
             0,      2,      2,      3,      0,      0,      2,      0,      1,
             2,      0,      2,      2,      0,      2,      0,      0,      2,
             0,      2,      2, 210714, 210715, 210716, 210717, 210718, 210719,
        210720, 210721, 210722, 210723,      0,      1,      2,      2,      2,
             0], device='cuda:0')
'''