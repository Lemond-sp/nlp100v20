# 61 単語のコサイン類似度

import gensim
import numpy as np
from gensim.models import KeyedVectors

def main():
  model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
  v1 = model['United_States']
  v2 = model['U.S.']
  print(cos_sim(v1,v2)) # 0.7310775

def cos_sim(v1,v2):
  return np.dot(v1,v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

if __name__ == '__main__':
  main()