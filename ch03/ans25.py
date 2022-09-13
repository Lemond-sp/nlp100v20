#https://ja.wikipedia.org/wiki/Template:基礎情報_国
#https://www.ipentec.com/document/software-regular-expression-difference-question-equal-and-question-colon
#要復習
'''
{{基礎情報 国
|自治領等 =
|hogehoge =
という形(改行が含まれていることに注意)
}}
'''

import pandas as pd
import re

df = pd.read_json('jawiki-country.json',lines=True)
uk = df.query('title == "イギリス"')['text'].values[0]
#\nでリスト化しているので、今回はre.DOTALL、MULTILINE 不必要
uk = uk.split('\n')

pattern = re.compile('\|(.+?)\s=\s*(.+)')
ans = {}
'''
re.search
マッチしない場合、None
r[0]:パターンとして抽出された全体
r[i]:i番目パターンとして抽出されたもの

re.matchは先頭の文字列からチェックすることを前提
^を指定しなくても、大丈夫
'''
for line in uk:
  r = re.search(pattern,line)
  if r:
    ans[r[1]] = r[2]
print(ans)