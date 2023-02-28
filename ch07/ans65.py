"""
64の実行結果を用い
意味的アナロジー（semantic analogy）と文法的アナロジー（syntactic analogy）の正解率を測定せよ
semantic analogy  : カテゴリ名に「gram」以外
syntactic analogy : カテゴリ名に「gram」
https://tomowarkar.github.io/blog/posts/nlp100-07/#65-アナロジータスクでの正解率
出力結果との正解率を算出する
"""

import pandas as pd
from tqdm import tqdm
import gensim
from gensim.models import KeyedVectors

def main():
  # load model
  model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
  semantic = []
  syntactic = []
  flag = True
  with open('ans64.txt') as f:
    for line in tqdm(f):
      words = line.split()
      
      # 意味的アナロジー
      if flag:
        if words[0] == ":" and "gram" in words[1]: # 意味的アナロジーではない行に達した
          flag = False
        elif len(words) > 2:
          # 正解率
          semantic.append(words[3] == words[4])
      
      # 文法的アナロジー
      else:
        # 意味的アナロジー
        if len(words) > 2:
          syntactic.append(words[3] == words[4])
      
    print(f'意味的アナロジー : {sum(semantic) / len(semantic)}% \n,\
            文法的アナロジー : {sum(syntactic) / len(syntactic)}%')
"""
words[3] : 正解
words[4] : predict
意味的アナロジー : 0.7308602999210734% 
文法的アナロジー : 0.7400468384074942%
"""
def get_cosine_similarity(model,words,k=1):
  cossims = model.most_similar(positive=[words[1],words[2]], negative=[words[0]], topn=k) # tuple in list
  
  return cossims[0][0],cossims[0][1]

if __name__ == "__main__":
  main()