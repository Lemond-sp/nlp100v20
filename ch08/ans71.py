# 単層ニューラルネットワークによる予測
import numpy as np
import torch
from torch import nn
from utils import Net

def main():
    contents_path = 'contents/features/bi-data/train_vec.npy'
    x_train = np.load(contents_path,allow_pickle=True) # dtypeがobjectの場合 allow_pickle=True
    x_train = x_train.tolist()
    x_train = np.array(x_train)
    x_train = torch.tensor(x_train,requires_grad=True).float()
    x_train.retain_grad()
    # 重み行列
    feature_num = 4
    net = Net(x_train.shape[1],feature_num)
    x = net(x_train)

    s = nn.Softmax(dim=1)
    ans = s(x)
    print(ans,ans[0:4][:],sep='\n') # 事例1~4までの出力結果も

    torch.save(net.state_dict(),'contents/output/ans71-model.pt')
    torch.save(x_train,'contents/output/x_train.pt')
    
if __name__ == "__main__":
    main()

'''
tensor([[0.2512, 0.2260, 0.2569, 0.2659],
        [0.2641, 0.2403, 0.2490, 0.2467],
        [0.2610, 0.2348, 0.2573, 0.2469],
        ...,
        [0.2573, 0.2164, 0.2576, 0.2686],
        [0.2678, 0.2330, 0.2488, 0.2504],
        [0.2545, 0.2391, 0.2535, 0.2529]], grad_fn=<SoftmaxBackward0>)
tensor([[0.2512, 0.2260, 0.2569, 0.2659],
        [0.2641, 0.2403, 0.2490, 0.2467],
        [0.2610, 0.2348, 0.2573, 0.2469],
        [0.2780, 0.2365, 0.2521, 0.2334]], grad_fn=<SliceBackward0>)
'''