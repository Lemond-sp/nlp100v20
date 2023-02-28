"""
WordSimilarity-353での評価
The WordSimilarity-353 Test Collectionの評価データをダウンロードし
単語ベクトルにより計算される類似度のランキングと
人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．
"""

import pandas as pd
import numpy as np
from tqdm import tqdm
import gensim
from gensim.models import KeyedVectors

def main():
  # load model
  global model
  model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
  combined_df = pd.read_csv('combined.csv')
  combined_df['predict'] = combined_df.apply(calc_cos_sim, axis=1)
  spearman_corr = combined_df[['Human (mean)', 'predict']].corr(method='spearman')
  print(f'spearman corr: {spearman_corr}')

def cos_sim(v1,v2):
  return np.dot(v1,v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def calc_cos_sim(row):
    v1 = model[row['Word 1']]
    v2 = model[row['Word 2']]
    return cos_sim(v1,v2)

if __name__ == "__main__":
  main()