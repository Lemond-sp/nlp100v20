"""
問題50で作成した各データを行列（ベクトル）に変換
特徴ベクトルは単語ベクトルの平均
行列・ベクトルを作成、ファイルに保存
"""
from utils import load_data,sep_list

import numpy as np
import argparse
import pickle
import os
import gensim
from gensim.models import KeyedVectors
from typing import List

def main():
    global model
    model = KeyedVectors.load_word2vec_format('contents/GoogleNews-vectors-negative300.bin', binary=True)
    contents_path = 'contents/features/'
    names = ['train','test','valid']
    
    # set data
    x_train,x_test,x_valid,y_train,y_test,y_valid = preprocess(contents_path)
    # print(x_train[1]) # ["China's", 'Stocks', 'Head', 'for', 'Weekly', 'Gain', 'on', 'Economic', 'Growth', 'Optimism']
    for i,seq in enumerate(x_test):
        x_test[i] = s2v(x_test[i]) # return numpy array
    #print(x_test.shape,x_test[0].shape) # (n, 300) (300,)
    # エラーなら、dictにいれる
    X = [np.array(x_train,dtype=object),np.array(x_test,dtype=object),np.array(x_valid,dtype=object)]
    Y = [y_train,y_test,y_valid]

    # データ保存
    for name,x in zip(names,X):
        np.save(
            f'{os.path.join(contents_path,name)}_vec',
            x
        )
    for name,y in zip(names,Y):
        np.save(
            f'{os.path.join(contents_path,name)}_label',
            y
        )
# Sentence to vector
def preprocess(path: str):
    # set data
    x_train = load_data(path,'text_train.txt')
    x_train = sep_list(x_train)
    #x_train = np.array(x_train)
    x_test = load_data(path,'text_test.txt')
    x_test = sep_list(x_test)
    #x_test = np.array(x_test)
    x_valid = load_data(path,'text_valid.txt')
    x_valid = sep_list(x_valid)
    #x_valid = np.array(x_valid)
    y_train = load_data(path,'label_train.txt')
    y_train = np.array(y_train)
    y_test = load_data(path,'label_test.txt')
    y_test = np.array(y_test)
    y_valid = load_data(path,'label_valid.txt')
    y_valid = np.array(y_valid)
    return x_train,x_test,x_valid,\
            y_train,y_test,y_valid

def s2v(sentence : List):
    '''
    sentence to vector
    average word vectors
    '''
    vectors = []
    # vocabに存在するもののみ
    apply_words = [word for word in sentence if word in model.index_to_key]
    
    # 対象語彙が存在するテキストのみmodel適用
    if len(apply_words) != 0:
        for word in apply_words:
            vectors.append(model[word])
        # average
        vectors = np.array(vectors)
        sentence_vec = np.mean(vectors,axis=0)
        return sentence_vec
    else:
        return []

if __name__ == "__main__":
    main()