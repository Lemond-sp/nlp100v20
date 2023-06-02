# 単層ニューラルネットワークによる予測
import numpy as np
import torch
from torch import nn

def main():
    contents_path = 'contents/features/train_vec.npy'
    x_train = np.load(contents_path,allow_pickle=True) # dtypeがobjectの場合 allow_pickle=True
    x_train = x_train.tolist()
    x_train = np.array(x_train)
    x_train = torch.tensor(x_train,requires_grad=True).float()
    # 重み行列
    feature_num = 4
    W = torch.randn(x_train.shape[1],feature_num) # 300,4
    xW = torch.mm(x_train,W)

    s = nn.Softmax(dim=1)
    ans = s(xW)
    print(ans,ans[0:4][:],sep='\n') # 事例1~4までの出力結果も

if __name__ == "__main__":
    main()

'''
tensor([[0.0363, 0.0823, 0.2563, 0.6251],
        [0.1019, 0.0511, 0.5000, 0.3469],
        [0.2088, 0.0806, 0.4425, 0.2681],
        ...,
        [0.3278, 0.3156, 0.0281, 0.3285],
        [0.0196, 0.0104, 0.6584, 0.3115],
        [0.0518, 0.0484, 0.8597, 0.0400]], grad_fn=<SoftmaxBackward0>)
tensor([[0.0363, 0.0823, 0.2563, 0.6251],
        [0.1019, 0.0511, 0.5000, 0.3469],
        [0.2088, 0.0806, 0.4425, 0.2681],
        [0.8974, 0.0124, 0.0588, 0.0314]], grad_fn=<SliceBackward0>)
'''