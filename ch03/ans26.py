'''
「'」２つ３つ５つ
25の結果から開始
'''
#25の処理
import pandas as pd
import re

df = pd.read_json('jawiki-country.json',lines=True)
uk = df.query('title == "イギリス"')['text'].values[0]
#\nでリスト化しているので、今回はre.DOTALL、MULTILINE 不必要
uk = uk.split('\n')

pattern = re.compile('\|(.+?)\s*=\s*(.+)')
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
#print(ans)

#26
'''
ansは辞書型であるので、re.MULTILINE不要
ちなみに enumerateだと インデックス+key
'''
pattern = r'\'{2,5}'
ans = {k: re.sub(pattern,'',v) for k,v in ans.items()}
#print(ans)
for k,v in ans.items():
  print(k + ':' + v)