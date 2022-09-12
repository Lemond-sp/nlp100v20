#記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．
#https://ja.wikipedia.org/wiki/Help:早見表
import pandas as pd
import re

df = pd.read_json('jawiki-country.json',lines=True)
uk = df.query('title == "イギリス"')['text'].values[0]

pattern = r'''
          ^(\={2,})
          \s*
          (.+?)
          \s*
          (\={2,})
          .*$'''
#VERBOSEとトリプルクォーテーションでパターン中に改行(見やすく)
sections = re.findall(pattern,uk,re.MULTILINE+re.VERBOSE)
print(sections)
for section in sections:
  level = len(section[0]) - 1
  print(f'{section[1]} {level}')

'''
findall:パターンにマッチした全ての文字列をリスト形式で返す
()を使ってキャプチャ対象を指定できる、
Pythonの正規表現は、複数候補の中から最も長い文字列にマッチ(貪欲マッチ)
?を加えると、最も短い文字列にマッチ(非貪欲マッチ)
'''