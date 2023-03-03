"""
Ward法によるクラスタリング
国名に関する単語ベクトルに対し
Ward法による階層型クラスタリングを実行せよ
さらに、クラスタリング結果をデンドログラムとして可視化せよ
国名データは国連加盟国一覧から取得
https://www.mofa.go.jp/mofaj/files/000023536.pdf
"""
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gensim
from gensim.models import KeyedVectors
from scipy.cluster.hierarchy import ward,dendrogram,linkage

def main():
  # save_countries_vec.py
  # 国名と対応する単語ベクトルのリスト
  with open('contents/countries_vec.bin','rb') as p:
    countries_vec = pickle.load(p)
  with open('contents/countries_names.bin','rb') as p:
    countries_list = pickle.load(p)
  
  #_ward = linkage(countries_vec, method='ward')
  _ward = ward(countries_vec)
  print(_ward)
  dendrogram(_ward, labels=countries_list)
  plt.show()
  plt.savefig('ans68_dendrogram.png')
if __name__ == "__main__":
  main()
