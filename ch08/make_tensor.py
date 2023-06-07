# tensorへの変形
import numpy as np
import torch
from torch import nn
from utils import Net

def main():
    names = ['train','valid','test']
    for name in names:
        make_tensor(name,mode='vec')
        make_tensor(name,mode='label')
    
def make_tensor(name,mode):
    if mode == 'vec':
        contents_path = 'contents/features/bi-data/' + name + '_vec.npy'
        vec_data = np.load(contents_path,allow_pickle=True) # dtypeがobjectの場合 allow_pickle=True
        vec_data = vec_data.tolist()
        vec_data = np.array(vec_data)
        vec_data = torch.tensor(vec_data,requires_grad=True).float()
        vec_data.retain_grad()
        torch.save(vec_data,'contents/output/x_' + name + '.pt')

    elif mode == 'label':
        contents_path = 'contents/features/bi-data/' + name + '_label.npy'
        label_data = np.load(contents_path) # float64,(N,)
        label_data = torch.LongTensor(label_data)
        torch.save(label_data,'contents/output/y_' + name + '.pt')

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