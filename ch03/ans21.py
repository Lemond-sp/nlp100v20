'''
カテゴリについて
https://ja.wikipedia.org/wiki/Help:カテゴリ
'''
import pandas as pd
import json
import re

df = pd.read_json('jawiki-country.json',lines=True)
uk = df.query('title == "イギリス"')['text'].values[0]

uk_list = uk.split('\n')
ans = list(filter(lambda x:'[Category:' in x,uk_list))
print(ans)