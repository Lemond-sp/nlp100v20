'''
カテゴリについて
https://ja.wikipedia.org/wiki/Help:カテゴリ
'''
import pandas as pd
import json
import re

df = pd.read_json('jawiki-country.json',lines=True)
uk = df.query('title == "イギリス"')['text'].values[0]
# findall :マッチした「文字列のリスト」を返す
uk_list = re.findall(r'^(\[\[Category:.*\]\])$',uk,re.MULTILINE+re.VERBOSE)
print(uk_list)
'''

re.VERBOSE : パターン記述の際、改行して見やすくできる
re.MULTILINE : 通常'^'は文字列の先頭でのみマッチするが
              追加で各行の先頭(各開業の直後)でマッチできるようにする
              '$'も同様である。
'^' : 文字列の先頭(re.MULTILINEを追加すれば、各行の先頭も)
'$' : 文字列の末尾(re.MULTILINEを追加すれば、各行の末尾も)

1 : 別解
uk_list = uk.split('\n')
ans = list(filter(lambda x:'[Category:' in x,uk_list))
print(ans)
'''