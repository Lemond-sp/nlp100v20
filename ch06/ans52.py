import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

y_train = pd.read_table('train.txt',header=None)[0]
y_test = pd.read_table('test.txt',header=None)[0]
y_valid = pd.read_table('valid.txt',header=None)[0]

x_train = np.loadtxt('train.feature.txt')
x_test = np.loadtxt('test.feature.txt')
x_valid = np.loadtxt('valid.feature.txt')

logr = LogisticRegression(max_iter=1000,random_state=42)
logr.fit(x_train,y_train)

# モデルを保存する
filename = '52_model.sav'
pickle.dump(logr, open(filename, 'wb'))

"""# 保存したモデルをロードする
loaded_model = pickle.load(open(filename, 'rb'))"""