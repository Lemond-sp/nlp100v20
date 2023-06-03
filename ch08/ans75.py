# 確率的勾配降下法
# 重み行列を学習
import os
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import torch
from torch import nn
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
import torch.optim as optim
from sklearn.metrics import accuracy_score
from utils import Net
import pickle

BATCH_SIZE = 128
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'

def main():
    tensor_path = 'contents/output'
    train_loader,val_loader,test_loader = make_dataloader(tensor_path)
    feature_num = 4
    net = Net(300,feature_num=feature_num)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print('using device:', device)
    net = net.to(device)

    # 損失
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.01)
    criterion = nn.CrossEntropyLoss()
    max_epoch = 3
    eps = 1e-6
    eps = torch.tensor(eps)
    train_ep_loss = [] # エポックごとの損失値
    test_ep_loss = []
    train_ep_acc = []
    test_ep_acc = []
    for epoch in tqdm(range(max_epoch)):
        train_losses = []
        train_pred = []
        train_true = []
        # ミニバッチ学習
        for batch in train_loader:

            # バッチサイズ分のサンプルを抽出
            x, t = batch  # 黄色の部分
            # データをGPUへ転送
            x = x.to(device)
            t = t.to(device)

            # 勾配を初期化
            optimizer.zero_grad()
            # 順伝播
            y = net(x)  # 赤色の部分
            train_pred.extend(y)
            train_true.extend(t)
            loss = criterion(y, t)  # 緑色の部分
            train_losses.append(loss)
            print(f'{epoch}epoch | loss:{loss}')
            # 誤差逆伝播
            loss.backward()  # 青色の部分
            optimizer.step()  # 青色の部分
        
        # 更新と切り離し、検証データの性能を確認
        with torch.no_grad():
            test_losses = []
            test_pred = []
            test_true = []
            for batch in test_loader:
                x, t = batch  # 黄色の部分
                x = x.to(device)
                t = t.to(device)
                y = net(x)  # 赤色の部分
                print(f' true = {t}')
                test_pred.extend(y.to('cpu').tolist())
                test_true.extend(t.tolist())
                
                loss = criterion(y, t)  # 緑色の部分
                test_losses.append(loss)
        train_loss = torch.tensor(train_losses).mean()
        train_ep_loss.append(train_loss)
        train_ep_acc.append(accuracy_score(train_true,train_pred))
        test_loss = torch.tensor(test_losses).mean()
        test_ep_loss.append(test_loss)
        test_ep_acc.append(accuracy_score(test_true,test_pred))

        print("Epoch: %02d  train_loss: %.3f" % (epoch+1, train_loss))
        print("Epoch: %02d  test_loss: %.3f" % (epoch+1, test_loss))
    
    # 正解率・損失値保存
    print(f'train{train_ep_acc} | {train_ep_loss}')
    print(f'test{test_ep_acc} | {test_ep_loss}')
    
    torch.save(net.state_dict(),'contents/output/ans73-model.pt')
    print('重みW 学習後')
    print(net.fc.weight)

def make_dataloader(tensor_path):
    x_train = torch.load(os.path.join(tensor_path,'x_train.pt'))
    x_valid = torch.load(os.path.join(tensor_path,'x_valid.pt'))
    x_test = torch.load(os.path.join(tensor_path,'x_test.pt'))
    y_train = torch.load(os.path.join(tensor_path,'y_train.pt'))
    y_valid = torch.load(os.path.join(tensor_path,'y_valid.pt'))
    y_test = torch.load(os.path.join(tensor_path,'y_test.pt'))
    # print(torch.max(y_valid)) なぜが210723
    train = TensorDataset(x_train, y_train)
    val = TensorDataset(x_valid, y_valid)
    test = TensorDataset(x_test, y_test)
    batch_size = BATCH_SIZE

    train_loader = DataLoader(train, batch_size, shuffle=True)
    val_loader = DataLoader(val, batch_size, shuffle=False)
    test_loader = DataLoader(test, 1, shuffle=False)
    return train_loader,val_loader,test_loader

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