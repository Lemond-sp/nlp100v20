import argparse
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
    # 未知語は[UNK]を用いたい
    global model
    model = KeyedVectors.load_word2vec_format('contents/')
    vocab_dict = 
    with open()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('')
    main()
