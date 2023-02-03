# 63 加法構成性によるアナロジー
# “Spain”の単語ベクトルから”Madrid”のベクトルを引き，
# ”Athens”のベクトルを足したベクトルを計算し，
# そのベクトルと類似度の高い10語とその類似度を出力せよ．
import gensim
from gensim.models import KeyedVectors
from pprint import pprint
def main():

  model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
  pprint(model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'], topn=10))

if __name__ == "__main__":
  main()

'''
[('Greece', 0.6898480653762817),
 ('Aristeidis_Grigoriadis', 0.5606847405433655),
 ('Ioannis_Drymonakos', 0.5552908778190613),
 ('Greeks', 0.545068621635437),
 ('Ioannis_Christou', 0.5400862693786621),
 ('Hrysopiyi_Devetzi', 0.5248445272445679),
 ('Heraklio', 0.5207759737968445),
 ('Athens_Greece', 0.516880989074707),
 ('Lithuania', 0.5166866183280945),
 ('Iraklion', 0.5146791338920593)]
'''