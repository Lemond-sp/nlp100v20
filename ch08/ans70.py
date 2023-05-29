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
from tqdm import tqdm
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
    print('start train')
    for i,seq in enumerate(x_train):
        x_train[i] = s2v(x_train[i]) # return numpy array
    print('start test')
    for i,seq in enumerate(x_test):
        x_test[i] = s2v(x_test[i]) # return numpy array
    print('start valid')
    for i,seq in enumerate(x_valid):
        x_valid[i] = s2v(x_valid[i]) # return numpy array
    
    # #print(x_test.shape,x_test[0].shape) # (n, 300) (300,)
    # # エラーなら、dictにいれる
    print(x_train.shape,x_test.shape,x_valid.shape)
    X = [x_train,x_test,x_valid]
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
    x_train = np.array(x_train,dtype=object)
    x_test = load_data(path,'text_test.txt')
    x_test = sep_list(x_test)
    x_test = np.array(x_test,dtype=object)
    x_valid = load_data(path,'text_valid.txt')
    x_valid = sep_list(x_valid)
    x_valid = np.array(x_valid,dtype=object)
    y_train = load_data(path,'label_train.txt')
    y_train = np.array(y_train,dtype=np.float64)
    y_test = load_data(path,'label_test.txt')
    y_test = np.array(y_test,dtype=np.float64)
    y_valid = load_data(path,'label_valid.txt')
    y_valid = np.array(y_valid,dtype=np.float64)
    return x_train,x_test,x_valid,\
            y_train,y_test,y_valid

def s2v(sentence : List,d_size = 300):
    '''
    sentence to vector
    average word vectors
    '''
    vectors = []
    # vocabに存在するもののみ
    apply_words = [word for word in sentence if word in model.index_to_key]
    
    # 対象語彙が存在するテキストのみmodel適用
    if len(apply_words) != 0:
        sentence_vec = np.mean(model[apply_words],axis=0)
    else:
        print(f'{sentence} is not vocab !')
        sentence_vec = np.zeros((d_size,)) # 未知語処理（任意の値を入れる手法もある）
    
    return sentence_vec

if __name__ == "__main__":
    main()