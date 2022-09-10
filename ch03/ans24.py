#[[ファイル:Wikipedia-logo-v2-ja.png|thumb|説明文]]
import pandas as pd
import re

df = pd.read_json('jawiki-country.json',lines=True)
uk = df.query('title == "イギリス"')['text'].values[0]

pattern = r'''
          \[\[
          ファイル
          :
          (.+?)
          \|
          '''
file_name = re.findall(pattern,uk,re.MULTILINE+re.VERBOSE)
for fn in file_name:
  print(fn)