# 損失と勾配の計算
# 事例1,事例集合1,2,3,4に対して
# クロスエントロピー損失、行列Wに対する勾配の計算
import os
import numpy as np
import torch
from torch import nn
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
    t1 = t[0]
    t2 = t[0:4]
    net1 = Net(300,feature_num=feature_num)
    net1.load_state_dict(torch.load('contents/output/ans71-model.pt'))
    net2 = Net(300,feature_num=feature_num)
    net2.load_state_dict(torch.load('contents/output/ans71-model.pt'))
    
    x1 = x_train[0][:] # スライスすると，x1が末端変数でない(grad_fn=SliceBackward)からgradがnoneになる(retain_gradTrueだとおｋ)
    x2 = x_train[0:4][:] # is_leafで末端のテンソルかどうか確認

    y1 = net1(x1)
    y2 = net2(x2)
    loss1 = criterion(y1, t1)
    loss2 = criterion(y2, t2)
    net1.zero_grad()
    loss1.backward()
    loss2.backward()
    print('----事例x1----')
    print('損失 :', loss1.item())
    print('勾配')
    print(net1.fc.weight.grad)
    print('----事例集合1,2,3,4----')
    print('損失 :', loss2.item())
    print('勾配')
    print(net2.fc.weight.grad)
    
if __name__ == "__main__":
    main()