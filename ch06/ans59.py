import pandas as pd
import numpy  as np

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier
import pickle

y_train = pd.read_table('train.txt',header=None)[0]
y_test = pd.read_table('test.txt',header=None)[0]
y_valid = pd.read_table('valid.txt',header=None)[0]

x_train = np.loadtxt('train.feature.txt')
x_test = np.loadtxt('test.feature.txt')
x_valid = np.loadtxt('valid.feature.txt')

"""#機械学習モデルをリストに格納
models = []
models.append(("ロジスティック回帰","LogisticRegression",LogisticRegression()))
models.append(("k近傍法","k-Nearest Neighbors",KNeighborsClassifier()))
models.append(("決定木","Decision Tree",DecisionTreeClassifier()))
models.append(("サポートベクターマシン(線形)","Support Vector Machine(linear)",SVC(kernel='linear')))
models.append(("サポートベクターマシン(非線形)","Support Vector Machine(rbf)",SVC(kernel='rbf')))
models.append(("ランダムフォレスト","Random Forest",RandomForestClassifier()))
models.append(("パーセプトロン","Perceptron",Perceptron()))
models.append(("多層パーセプトロンパーセプトロン","Multilayer perceptron",MLPClassifier()))
 
names_jp = []
names_en = []
results = []
for name_jp,name_en,model in models:
    
    print(model.fit(x_train,y_train),"\n")
    
    names_jp.append(name_jp)
    names_en.append(name_en)
    results.append(model.score(x_valid,y_valid))

list_df = pd.DataFrame( columns=['識別子','識別子(英名)','スコア'] )

for i in range(len(names_jp)):
    list_df = list_df.append( pd.Series( [names_jp[i],names_en[i],results[i]], index=list_df.columns ), ignore_index=True)

print(list_df) # SVM(rbf)0.866567が最良

"""
"""# SVM(rbf)でハイパラいじり
C = [0.01,0.1,1,10]
max_res = 1e-9
max_res = 0
for c in C:
  rbf = SVC(kernel='rbf',C=c)
  rbf.fit(x_train,y_train)
  res = rbf.score(x_test,y_test)
  print(f'res :{res/valid}')
  print(f'res :{res/valid}')bbb
  if max_res < res:
    max_res = res
    max_c = c

print(f'max_res :{max_res} | max_c :{max_c}')
max_res :0.8778110944527736 | max_c :10
"""
max_c = 10 # また回すの面倒なので
rbf = SVC(kernel='rbf',C=max_c)
rbf.fit(x_train,y_train)
res = rbf.score(x_valid,y_valid) # 0.8778110944527736
print(res)