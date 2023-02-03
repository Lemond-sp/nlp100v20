# 60 単語ベクトルの読み込みと表示
import gensim
from gensim.models import KeyedVectors

# model = gensim.models.KeyedVectors.load_word2vec_format()
model = KeyedVectors.load_word2vec_format('')

print(model['United_States'])