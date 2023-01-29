'''
52で学習したロジスティック回帰モデルの適合率，再現率，F1スコアを，評価データ上で計測せよ
カテゴリごとに適合率，再現率，F1スコアを求め，カテゴリごとの性能を
マイクロ平均（micro-average）とマクロ平均（macro-average）で統合
'''
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
import pandas as pd
import numpy as np
import pickle

x_test = np.loadtxt('test.feature.txt')
y_test = pd.read_table('test.txt',header=None)[0]

# 保存したモデルをロードする
filename = '52_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
test_pred = loaded_model.predict(x_test)

# 適合率 再現率 F1スコア

print('--- precision ---')
print(precision_score(y_test,test_pred,average=None))
print(precision_score(y_test,test_pred,average='micro'))
print(precision_score(y_test,test_pred,average='macro'))
print('--- recall ---')
print(recall_score(y_test,test_pred,average=None))
print(recall_score(y_test,test_pred,average='micro'))
print(recall_score(y_test,test_pred,average='macro'))
print('--- f1 score ---')
print(f1_score(y_test,test_pred,average=None))
print(f1_score(y_test,test_pred,average='micro'))
print(f1_score(y_test,test_pred,average='macro'))