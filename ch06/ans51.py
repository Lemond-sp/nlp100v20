from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

train = pd.read_table('train.txt',header=None)
test = pd.read_table('test.txt',header=None)
valid = pd.read_table('valid.txt',header=None)

train_text = train[1]
print(train_text)
vectorizer = TfidfVectorizer()
vectorizer.fit(train_text)

train_x = vectorizer.transform(train_text)
