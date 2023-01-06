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

pattern = re.compile('\|(.+?)\s=\s(.+)')
ans = {}
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
# pattern = r'\'{2,5}' # pattern = r"'+"でもよかった
# pattern = "'+"

r = re.compile("'+")
ans = {k: r.sub('',v) for k,v in ans.items()}

for k,v in ans.items():
  print(k + ':' + v)


"""
略名:イギリス
日本語国名:グレートブリテン及び北アイルランド連合王国
公式国名:{{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br />
国旗画像:Flag of the United Kingdom.svg
"""