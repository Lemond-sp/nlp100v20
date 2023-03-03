"""
ans67.py より
国名の単語ベクトルをpickleで保存する
"""
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gensim
from gensim.models import KeyedVectors

COUNTRY_NUM = 193

def main():
  country_list = [] # 国名一覧
  country_vec = []
  model = KeyedVectors.load_word2vec_format('contents/GoogleNews-vectors-negative300.bin', binary=True)
  with open('contents/country.txt') as f:
    for line in f:
      country_name = line.split('　　')[1] # issue
      country_name = country_name.strip()
      country_name = country_name.replace(' ','_')
      w2v(model,country_name,country_list,country_vec)
  
  # 単語ベクトル・国名を保存
  with open('contents/countries_vec.bin','wb') as p:
    pickle.dump(country_vec,p)
  with open('contents/countries_names.bin','wb') as p:
    pickle.dump(country_list,p)
  print(f'単語ベクトル数 : {COUNTRY_NUM} --> {len(country_list)}') # 193 --> 169
# KeyErrorに該当した国名は除外
def w2v(model,word,word_list,vec_list):
  try:
    model[word]
  except KeyError:
    print(f'{word} is KeyError')
    return 0
  word_list.append(word)
  vec_list.append(model[word])
if __name__ == "__main__":
  main()