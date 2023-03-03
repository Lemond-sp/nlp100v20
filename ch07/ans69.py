"""
t-SNEによる可視化
ベクトル空間上の国名に関する単語ベクトルをt-SNEで可視化せよ
"""
import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

def main():
  # save_countries_vec.py
  # 国名と対応する単語ベクトルのリスト
  with open('contents/countries_vec.bin','rb') as p:
    countries_vec = pickle.load(p)
  with open('contents/countries_names.bin','rb') as p:
    countries_list = pickle.load(p)
  
  # t-SNE
  tsne = TSNE(random_state=42, n_iter=15000, metric='cosine')
  countries_tsne = tsne.fit_transform(np.array(countries_vec)) # AttributeError: 'list' object has no attribute 'shape'

  # プロット
  plt.figure(figsize=(10, 10))
  plt.scatter(np.array(countries_tsne).T[0], np.array(countries_tsne).T[1])
  for (x, y), name in zip(countries_tsne,countries_list):
      plt.annotate(name, (x, y))
  plt.show()
  plt.savefig('ans69_tSNE.png')
if __name__ == "__main__":
  main()