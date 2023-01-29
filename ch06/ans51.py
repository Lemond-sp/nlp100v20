# TF-IDF による特徴量抽出
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import pickle

train = pd.read_table('train.txt',header=None)
test = pd.read_table('test.txt',header=None)
valid = pd.read_table('valid.txt',header=None)

train_text = train[1]
test_text = test[1]
valid_text = valid[1]

vectorizer = TfidfVectorizer(max_features=1500,smooth_idf=True)
x_train = vectorizer.fit_transform(train_text)
x_test = vectorizer.transform(test_text)
x_valid = vectorizer.transform(valid_text)

np.savetxt("train.feature.txt",x_train.toarray())
np.savetxt("test.feature.txt",x_test.toarray())
np.savetxt("valid.feature.txt",x_valid.toarray())

# 語彙を保存(57より)
vocab = vectorizer.get_feature_names()
# モデルを保存する
filename = '52_vocab.sav'
pickle.dump(vocab, open(filename, 'wb'))
