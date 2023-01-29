import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

y_train = pd.read_table('train.txt',header=None)[0]
y_test = pd.read_table('test.txt',header=None)[0]
x_train = np.loadtxt('train.feature.txt')
x_test = np.loadtxt('test.feature.txt')

# 保存したモデルをロードする
filename = '52_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
res_train = loaded_model.score(x_train,y_train) # mean acc
res_test = loaded_model.score(x_test,y_test)

print(f'train :{res_train} | test :{res_test}')