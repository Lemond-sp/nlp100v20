from utils import load_data, sep_list

import numpy as np
import argparse
import pickle
import os
from tqdm import tqdm
import gensim
from gensim.models import KeyedVectors
from typing import List


def s2v(sentence: List, d_size=300):
    """
    sentence to vector
    average word vectors
    """
    vectors = []
    # vocabに存在するもののみ
    apply_words = [word for word in sentence if word in model.index_to_key]

    # 対象語彙が存在するテキストのみmodel適用
    if len(apply_words) != 0:
        sentence_vec = np.mean(model[apply_words], axis=0)
    else:
        print(f"{sentence} is not vocab !")
        sentence_vec = np.zeros((d_size,))  # 未知語処理（任意の値を入れる手法もある）

    return sentence_vec
