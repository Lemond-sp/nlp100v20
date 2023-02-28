"""
WordSimilarity-353での評価
The WordSimilarity-353 Test Collectionの評価データをダウンロードし
単語ベクトルにより計算される類似度のランキングと
人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．
"""

import pandas as pd
from tqdm import tqdm
import gensim
from gensim.models import KeyedVectors

def main():
  # load model
  model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

if __name__ == "__main__":
  main()