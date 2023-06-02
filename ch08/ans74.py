# 正解率の計測
# 学習データと評価データの事例を推論，正解率を算出
import os
import numpy as np
import torch
from torch import nn
import torch.optim as optim
from sklearn.metrics import accuracy_score
from utils import Net

def main():
    contents_path = 'contents'
    x_train = torch.load(os.path.join(contents_path,'output/x_train.pt'))
    x_train.retain_grad() # 逆伝搬時に末端以外のテンソルの微分係数の記録を可能にする
    x_test = np.load(os.path.join(contents_path,'features/bi-data/test_vec.npy'),allow_pickle=True) # dtypeがobjectの場合 allow_pickle=True
    x_test = x_test.tolist()
    x_test = np.array(x_test)
    x_test = torch.tensor(x_test,requires_grad=True).float()
    x_test.retain_grad()

    feature_num = 4
    
    # 学習済みモデル
    net = Net(300,feature_num=feature_num)
    net.load_state_dict(torch.load('contents/output/ans73-model.pt'))

    y_test = np.load(os.path.join(contents_path,'features/bi-data/test_label.npy')) # float64,(N,)
    y_test = torch.LongTensor(y_test) # 64bit符号付き整数
    y_train = np.load(os.path.join(contents_path,'features/bi-data/train_label.npy')) # float64,(N,)
    y_train = torch.LongTensor(y_train) # 64bit符号付き整数

    outputs = net(x_test) # torch.Size([1334, 4])
    test_preds = torch.argmax(outputs,dim=1)
    test_preds = test_preds.numpy()
    print(accuracy_score(y_test,test_preds))
    outputs = net(x_train) # torch.Size([1334, 4])
    train_preds = torch.argmax(outputs,dim=1)
    train_preds = train_preds.numpy()
    print(accuracy_score(y_train,train_preds))

if __name__ == "__main__":
    main()
