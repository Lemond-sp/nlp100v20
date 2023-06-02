# 損失と勾配の計算
# 事例1,事例集合1,2,3,4に対して
# クロスエントロピー損失、行列Wに対する勾配の計算
import os
import numpy as np
import torch
from torch import nn

def main():
    contents_path = 'contents/output'
    x_train = torch.load(os.path.join(contents_path,'ans71.pt')) # torch.Size([10672, 4])
    y_train = np.load(os.path.join(contents_path,'../features/bi-data/train_label.npy')) # float64,(N,)
    y_train = torch.LongTensor(y_train) # 64bit符号付き整数
    
    # 損失
    loss = nn.CrossEntropyLoss()
    x1 = x_train[0][:] # スライスすると，x1が末端変数でない(grad_fn=SliceBackward)からgradがnoneになる
    x2 = x_train[0:4][:] # is_leafで末端のテンソルかどうか確認
    # 逆伝搬時に末端以外のテンソルの微分係数の記録を可能にする
    x1.retain_grad()
    x2.retain_grad()
    
    out1 = loss(x1,y_train[0])
    out2 = loss(x2,y_train[0:4])

    print(out1,out2)
    # 行列に対する勾配
    out1.retain_grad()
    out2.retain_grad()
    out1.backward()
    out2.backward()

    print(x1.grad,x2.grad) # x_train.grad[0][:]でもよかった

if __name__ == "__main__":
    main()