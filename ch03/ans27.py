'''
26の結果から開始
内部リンクの除去
[[記事名]]
[[記事名|表示文字]]
[[記事名#節名|表示文字]]
＊未解決＊
https://ja.wikipedia.org/wiki/Help:早見表
'''
#25 :テンプレートの抽出、辞書作成
import pandas as pd
import re

df = pd.read_json('jawiki-country.json',lines=True)
uk = df.query('title == "イギリス"')['text'].values[0]
uk = uk.split('\n')

pattern = re.compile('\|(.+?)\s*=\s(.+)')
ans = {}
for line in uk:
  r = re.search(pattern,line)
  if r:
    ans[r[1]] = r[2]

#26 :強調マークアップの除去
pattern = r'\'{2,5}'
ans = {k: re.sub(pattern,'',v) for k,v in ans.items()}

#27 :内部リンクの除去
pattern = r'\[{2}'
ans = {k: re.sub(pattern,'',v,10,re.MULTILINE) for k,v in ans.items()}

pattern = r'\]{2}'
ans = {k: re.sub(pattern,'',v,10,re.MULTILINE) for k,v in ans.items()}
for k,v in ans.items():
  print(f'{k} : {v}')
"""
r = re.compile('\[\[(.+\||)(.+?)\]\]')
ans = {k: r.sub(r'\2', v) for k, v in dc.items()}

# キャプチャグループの2番目にreplace
# \<number> or \g<number>
https://micropython-docs-ja.readthedocs.io/ja/latest/library/re.html#re.sub

"""