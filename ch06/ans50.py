import pandas as pd
from sklearn.model_selection import train_test_split
import re

'''
readme.txt より

FILENAME #1: newsCorpora.csv (102.297.000 bytes)
DESCRIPTION: News pages
FORMAT: ID \t TITLE \t URL \t PUBLISHER \t CATEGORY \t STORY \t HOSTNAME \t TIMESTAMP
TITLE : ニュースの見出し
CATEGORY	News category (b = business, t = science and technology, e = entertainment, m = health)
'''
# titleに「"」で始まる文字列があるため，quoting=3として、ダブルコーテーションによるエスケープ処理を無効化
df = pd.read_csv('../ch06/contents/newsCorpora.csv',\
  names=['id','title','url','publisher','category','story','hostname','timestamp']\
    ,sep='\t',quoting=3)

cols = ["Reuters","Huffington Post","Businessweek","Contactmusic.com","Daily Mail"]

df = df[df['publisher'].isin(cols)]
# print(df.query(f'publisher == {cols}'))
# queryではカラム名に「.」「 」「数字」を入れてはいけない

df_pub = df.sample(frac=1, random_state=42).reset_index(drop=True)


# train:test:dev = 8:1:1
train, test = train_test_split(df_pub, test_size=0.2, random_state=42, stratify=df_pub['category'])
test,dev = train_test_split(test,test_size=0.5,random_state=42,stratify=test['category'])

# dataframe to txt
# sep='\t'
dev_list = dev['category'].tolist()
dev_title = dev['title'].tolist()
print(dev_list[752],dev_title[752]) # 752-765
dev.to_csv('valid-pre.txt',columns=['category','title'],sep='\t',index=False, header=None)
#print(dev['category'])
train['category'] = train['category'].map({'b': 0, 't': 1, 'e': 2, 'm': 3})
train["title"] = train["title"].replace(re.compile(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)"), '', regex=True)
test['category'] = test['category'].map({'b': 0, 't': 1, 'e': 2, 'm': 3})
test["title"] = test["title"].replace(re.compile(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)"), '', regex=True)

dev['category'] = dev['category'].map({'b': 0, 't': 1, 'e': 2, 'm': 3})
print(dev[dev['title'].str.match('http')])
#dev["title"] = dev["title"].replace(re.compile(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)"), '', regex=True)

print(set(dev['category']))
train.to_csv('train.txt',columns=['category','title'],sep='\t',index=False, header=None)
test.to_csv('test.txt',columns=['category','title'],sep='\t',index=False, header=None)
dev.to_csv('valid.txt',columns=['category','title'],sep='\t',index=False, header=None)

# Check the number of cases in each category
# print('train value_counts')
# print(train.shape)
# print(train['category'].value_counts())
# print('test value_counts')
# print(test.shape)
# print(test['category'].value_counts())