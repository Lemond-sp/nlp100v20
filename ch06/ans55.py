# https://note.nkmk.me/python-sklearn-confusion-matrix-score/
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import pickle

y_train = pd.read_table('train.txt',header=None)[0]
y_test = pd.read_table('test.txt',header=None)[0]
x_train = np.loadtxt('train.feature.txt')
x_test = np.loadtxt('test.feature.txt')

# 保存したモデルをロードする
filename = '52_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
train_pred = loaded_model.predict(x_train) # mean acc
test_pred = loaded_model.predict(x_test)

# 混同行列
cm = confusion_matrix(y_train,train_pred)
print('--- train ---')
print(cm)

cm = confusion_matrix(y_test,test_pred)
print('--- test ---')
print(cm)