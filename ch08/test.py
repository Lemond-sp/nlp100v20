import numpy as np
import argparse
import pickle
import os
import statistics
import gensim
from gensim.models import KeyedVectors

def main():
    global model
    w2v = []
    model = KeyedVectors.load_word2vec_format('contents/GoogleNews-vectors-negative300.bin', binary=True)
    data = [['UPDATE', '1-Colorado', 'reaps', '$2.1', 'mln', 'from', 'first', 'month', 'of', 'recreational', 'pot', 'sales'], ['UPDATE', '1-Putin', 'ally', 'expects', 'flurry', 'of', 'China', 'deals', 'in', 'new', 'role']]
    for d in data:
        w2v.append(s2v(data))
    w2v = np.array(w2v)
    print(w2v.shape)
    
# Sentence to vector
def s2v(words):
    avg_list = [model[word] for word in words]
    return statistics.mean(avg_list)
# words    
# def s2v(words)
if __name__ == "__main__":
    main()