"""
64の実行結果を用い
意味的アナロジー（semantic analogy）と文法的アナロジー（syntactic analogy）の正解率を測定せよ
semantic analogy  : カテゴリ名に「gram」以外
syntactic analogy : カテゴリ名に「gram」
https://tomowarkar.github.io/blog/posts/nlp100-07/#65-アナロジータスクでの正解率
出力結果との正解率を算出する。
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