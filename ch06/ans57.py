# 重みの高い特徴量トップ10と，重みの低い特徴量トップ10を確認
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

x_test = np.loadtxt('test.feature.txt')
y_test = pd.read_table('test.txt',header=None)[0]

# 保存したモデルをロードする
filename = '52_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
coefs = loaded_model.coef_

n = 0
filename = '52_vocab.sav'
vocab = pickle.load(open(filename, 'rb'))

for c in coefs:
  # 上(下)位 10件
  d = dict(zip(vocab, c))
  print(f'{n}ラベルの重みより')
  d_top10 = sorted(d.items(), key=lambda x: abs(x[1]), reverse=True)[:10]
  d_bottom10 = sorted(d.items(), key=lambda x: abs(x[1]))[:10]
  print('--- top 10 ---')
  print(d_top10)
  print('--- bottom 10 ---')
  print(d_bottom10)
  print('\n')
  n += 1
"""
loaded_model.coef_
[[ 0.1870892   0.33908416 -0.19306187 ...  0.74965191 -0.65568315
   0.60904358]
 [-0.38457625 -0.33142125  0.64496635 ... -0.36581889  1.33998003
  -0.55222928]
 [ 0.33792357  0.00747908 -0.52348533 ... -0.23525207 -0.341083
  -0.05480144]
 [-0.14043653 -0.015142    0.07158085 ... -0.14858095 -0.34321388
  -0.00201285]]
"""