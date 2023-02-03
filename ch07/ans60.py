# 60 単語ベクトルの読み込みと表示
# gensim によるPre-trained Word Vectors
import gensim
from gensim.models import KeyedVectors

def main():
  
  model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
  print(model['United_States'])
  print(model['United_States'].shape) # (300,)

if __name__ == "__main__":
  main()