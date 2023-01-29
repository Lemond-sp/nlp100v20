import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

x_test = np.loadtxt('test.feature.txt')
y_test = pd.read_table('test.txt',header=None)[0]

# 保存したモデルをロードする
filename = '52_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
res = loaded_model.predict(x_test) # 予測カテゴリ
res_prob = loaded_model.predict_proba(x_test) # 各カテゴリの予測確率
print(res,res_prob,sep='\n')