# 確率的勾配降下法
# 重み行列を学習
import os
import numpy as np
import torch
from torch import nn
import torch.optim as optim
from utils import Net

def main():
    contents_path = 'contents'
    x_train = torch.load(os.path.join(contents_path,'output/x_train.pt'))
    x_train.retain_grad() # 逆伝搬時に末端以外のテンソルの微分係数の記録を可能にする
    feature_num = 4
    
    # # 損失
    criterion = nn.CrossEntropyLoss()
    t = np.load(os.path.join(contents_path,'features/bi-data/train_label.npy')) # float64,(N,)
    t = torch.LongTensor(t) # 64bit符号付き整数
    net = Net(300,feature_num=feature_num)
    optimizer = optim.SGD(net.parameters(), lr=0.01)
    criterion = nn.CrossEntropyLoss()
    epoch = 100
    print('重みW 初期値')
    print(net.fc.weight)
    # 学習
    for i in range(epoch):
        optimizer.zero_grad()
        output = net(x_train)
        loss = criterion(output,t)
        loss.backward()
        optimizer.step()
    
    torch.save(net.state_dict(),'contents/output/ans73-model.pt')
    print('重みW 学習後')
    print(net.fc.weight)

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
'''