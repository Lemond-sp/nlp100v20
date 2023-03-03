"""
国名に関する単語ベクトルを抽出し
k-meansクラスタリングをクラスタ数k=5として実行せよ
国名データは国連加盟国一覧から取得
https://www.mofa.go.jp/mofaj/files/000023536.pdf
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from sklearn.cluster import KMeans
import gensim
from gensim.models import KeyedVectors

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
  
  # kMeans
  kmeans = KMeans(n_clusters=5)
  kmeans.fit(country_vec)
  for i in range(5):
    cluster = np.where(kmeans.labels_ == i)[0]
    print('cluster', i)
    print(', '.join([country_list[k] for k in cluster]))

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

"""
cluster 0
Afghanistan, Armenia, Australia, Azerbaijan, Bahrain, Bangladesh, Bhutan, Brunei_Darussalam, Cambodia, China, Egypt, Georgia, India, Indonesia, Iran, Iraq, Israel, Japan, Jordan, Kazakhstan, Kuwait, Kyrgyzstan, Lebanon, Libya, Malaysia, Mongolia, Morocco, Myanmar, Nepal, Oman, Pakistan, Philippines, Qatar, Saudi_Arabia, Singapore, Sri_Lanka, Syria, Tajikistan, Thailand, Turkey, Turkmenistan, United_Arab_Emirates, Uzbekistan, Viet_Nam, Yemen
cluster 1
Algeria, Angola, Benin, Botswana, Burkina_Faso, Burundi, Cameroon, Chad, Djibouti, Equatorial_Guinea, Eritrea, Ethiopia, Gabon, Gambia, Ghana, Guinea, Kenya, Lesotho, Liberia, Madagascar, Malawi, Mali, Mauritania, Mozambique, Namibia, Niger, Nigeria, Rwanda, Senegal, Sierra_Leone, Somalia, South_Africa, Sudan, Togo, Tunisia, Uganda, Zambia, Zimbabwe
cluster 2
Albania, Andorra, Argentina, Austria, Belarus, Belgium, Bulgaria, Canada, Croatia, Cyprus, Czech_Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Iceland, Ireland, Italy, Latvia, Liechtenstein, Lithuania, Luxembourg, Malta, Monaco, Montenegro, Netherlands, Norway, Paraguay, Poland, Portugal, Romania, San_Marino, Serbia, Slovakia, Slovenia, Spain, Sweden, Switzerland, Ukraine, United_Kingdom, Uruguay
cluster 3
Cabo_Verde, Comoros, Fiji, Kiribati, Maldives, Marshall_Islands, Mauritius, Nauru, New_Zealand, Palau, Samoa, Seychelles, Solomon_Islands, Tonga, Tuvalu, Vanuatu
cluster 4
Bahamas, Barbados, Belize, Bolivia, Brazil, Chile, Colombia, Costa_Rica, Cuba, Dominica, Dominican_Republic, Ecuador, El_Salvador, Grenada, Guatemala, Guyana, Haiti, Honduras, Jamaica, Mexico, Nicaragua, Panama, Peru, Saint_Lucia, Suriname, Venezuela
"""