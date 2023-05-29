# 単層ニューラルネットワークによる予測
import numpy as np
import torch
from torch import nn

def main():
    contents_path = 'contents/features/test_vec.npy'
    x_train = np.load(contents_path,allow_pickle=True)
    x_train = x_train.tolist()
    x_train = np.array(x_train)
    x_train = torch.tensor(x_train,requires_grad=True)
    # 重み行列
    feature_num = 4
    W = torch.randn(x_train.shape[1],feature_num)
    xW = torch.mm(x_train,W)

    s = nn.Softmax(dim=1)
    ans = s(xW)
    print(ans,ans[0:4][:],sep='\n') # 事例1~4までの出力結果も

if __name__ == "__main__":
    main()