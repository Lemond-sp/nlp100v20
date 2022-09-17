'''
26の結果から開始
内部リンクの除去
https://ja.wikipedia.org/wiki/Help:早見表
'''
#25の処理
import pandas as pd
import re

df = pd.read_json('jawiki-country.json',lines=True)
uk = df.query('title == "イギリス"')['text'].values[0]
uk = uk.split('\n')

pattern = re.compile('\|(.+?)\s*=\s*(.+)')
ans = {}
for line in uk:
  r = re.search(pattern,line)
  if r:
    ans[r[1]] = r[2]

#26の処理
pattern = r'\'{2,5}'
ans = {k: re.sub(pattern,'',v) for k,v in ans.items()}
#print(ans)
#27の処理
pattern = r'\[{2}'
ans = {k: re.sub(pattern,'',v) for k,v in ans.items()}

pattern = r'\]{2}'
ans = {k: re.sub(pattern,'',v) for k,v in ans.items()}
print(ans)