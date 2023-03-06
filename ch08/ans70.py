"""
問題50で作成した各データを行列（ベクトル）に変換
特徴ベクトルは単語ベクトルの平均
"""
import numpy as np
import argparse
import pickle
import os
import gensim
from gensim.models import KeyedVectors

def main():
    global model
    # model = KeyedVectors.load_word2vec_format('contents/GoogleNews-vectors-negative300.bin', binary=True)
    f = open('contents/text_train.txt')
    train_data = f.read()
    train_data = train_data.split('\n')
    del train_data[10673]
    for i in range(len(train_data)):
        train_data[i] = train_data[i].split(' ')
def data_load(filename)
# Sentence to vector
# words    
# def s2v(words)
if __name__ == "__main__":
    main()