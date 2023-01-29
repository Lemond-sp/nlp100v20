import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
y_train = pd.read_table('train.txt',header=None)[0]
y_test = pd.read_table('test.txt',header=None)[0]
y_valid = pd.read_table('valid.txt',header=None)[0]

x_train = np.loadtxt('train.feature.txt')
x_test = np.loadtxt('test.feature.txt')
x_valid = np.loadtxt('valid.feature.txt')

C = [0.01,0.1,1,10]
sc_train = []
sc_test = []
sc_valid = []

for c in C:
  logr = LogisticRegression(max_iter=1000,random_state=42,C=c)
  logr.fit(x_train,y_train)
  sc_train.append(logr.score(x_train,y_train))
  sc_test.append(logr.score(x_test,y_test))
  sc_valid.append(logr.score(x_valid,y_valid))


# 表示
fig, ax = plt.subplots()

ax.set_xlabel('Regularization C')
ax.set_ylabel('mean acc')

ax.plot(C,sc_train,color='red',label='train',marker='o')
ax.plot(C,sc_test,color='green',label='test',marker='o')
ax.plot(C,sc_valid,color='blue',label='valid',marker='o')
ax.legend(loc=0)

plt.show()