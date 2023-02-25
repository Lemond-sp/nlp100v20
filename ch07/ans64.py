"""
vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
そのベクトルと類似度が最も高い単語と，その類似度を求めよ．
求めた単語と類似度は，各事例の末尾に追記せよ．
"""

import pandas as pd
from tqdm import tqdm
import gensim
from gensim.models import KeyedVectors

def main():
  # load model
  model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
  
  with open('questions-words.txt') as f,\
    open('ans64.txt','w') as fw:
    for line in tqdm(f):
      words = line.split()
      
      if words[0] == ":":
        ans = " ".join(words)
      else:
        #print(len(words),words)
        most_sim ,cossim = get_cosine_similarity(model,words,1)
        cossim = str(cossim)
        words.extend([most_sim,cossim])
        ans = " ".join(words)
      fw.write(ans + "\n")
    
def get_cosine_similarity(model,words,k=1):
  cossims = model.most_similar(positive=[words[1],words[2]], negative=[words[0]], topn=k) # tuple in list
  
  return cossims[0][0],cossims[0][1]

if __name__ == "__main__":
  main()