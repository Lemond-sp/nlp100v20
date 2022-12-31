#jsonファイル読み込み
import pandas as pd
import json
import re

df = pd.read_json('jawiki-country.json',lines=True)
#titleがイギリスの記事は1つのみ
uk = df.query('title == "イギリス"')['text'].values[0]
print(uk)
'''
lines:１行ごとに処理
query(条件式)
valuesで値を取り出し

uk = df[df['title'] == "イギリス"]['text'].values[0]でも

'''