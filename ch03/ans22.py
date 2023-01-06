import pandas as pd
import re

df = pd.read_json('jawiki-country.json',lines=True)
uk = df.query('title == "イギリス"')['text'].values[0]
uk_list = uk.split('\n')
ans = list(filter(lambda x:'[[Category:' in x,uk_list))
ans = [re.sub(r'[\[\[Category:|*\]\]]','',a) for a in ans]
print(ans)

'''
MULTILINE:複数行文字列に対するマッチング コンパイルフラグの一種
pattern = r'^.*\[\[Category:(.*?)(?:\|.*)?\]\].*$'
res = '\n'.join(re.findall(pattern,uk,re.MULTILINE))

replace
ans = [a.replace('[[Category:','').replace('|*','').replace(']]','') for a in ans]

translate 複数の置換
ans = [a.translate(str.maketrans({'[[Category:':'','|*':'',']]':''})) for a in ans]
ValueError: string keys in translate table must be of length 1
辞書のキーは長さ一の文字に設定する必要あり
不採用
'''