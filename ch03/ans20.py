'''
jawaki-country.json
title : 記事名(国名)
text  : 記事本文

jsonl : 1レコードがjsonになっているファイル

'''

#jsonファイル読み込み
import pandas as pd
import json
import re
# json to daraframe
df = pd.read_json('jawiki-country.json',orient='records',lines=True)
#titleがイギリスの記事は1つのみ
uk = df.query('title == "イギリス"')['text'].values[0]
print(uk)
'''
read_json
・orient :DataFrameにあった形式でjsonを読み込むため
  ・行ごとのリスト構造 :orient = 'records'
  ・列ごとのリスト構造 :orient = 'columns'
  ・index、columns、dataで明示的に分かれている場合 :orient = 'split'

lines:１行ごとに処理
query(条件式)
valuesで値を取り出し

別解
1 : 直接指定
uk = df[df['title'] == "イギリス"]['text'].values[0]でも

2 :gzip
with gzip.open('~.gz') as f:
  for line in f:
gzファイルのままでもロード可

3 :jsonモジュール
with open('~.json') as f:
  data = json.load(f)
>>>json.decoder.JSONDecodeError: Extra data: line 2 column 1

jsonlであるため一行ずつ読み込む

with open('jawiki-country.json', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data['title'] == 'イギリス':
            print(data['text'])

https://www.dmysd.net/blog/archives/52#orient-records

'''