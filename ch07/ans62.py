# 62 類似度の高い単語10件
# “United States”とコサイン類似度が高い10語と，その類似度を出力
import gensim
from gensim.models import KeyedVectors
from pprint import pprint
def main():

  model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
  pprint(model.most_similar('United_States',topn=10))

if __name__ == "__main__":
  main()

'''
[('Unites_States', 0.7877248525619507),
 ('Untied_States', 0.7541370987892151),
 ('United_Sates', 0.7400725483894348),
 ('U.S.', 0.7310774922370911),
 ('theUnited_States', 0.6404394507408142),
 ('America', 0.6178409457206726),
 ('UnitedStates', 0.6167312264442444),
 ('Europe', 0.6132988929748535),
 ('countries', 0.6044804453849792),
 ('Canada', 0.6019068956375122)]
'''