# [[ファイル:Wikipedia-logo-v2-ja.png|thumb|説明文]]
# Wikipedia-logo-v2-ja.pngがほしい

import pandas as pd
import re

df = pd.read_json('jawiki-country.json',lines=True)
uk = df.query('title == "イギリス"')['text'].values[0]

pattern = r'''
          \[\[
          ファイル
          :
          (.+?)
          \| # .+?と\|で仕切りを入れる
          '''
file_name = re.findall(pattern,uk,re.MULTILINE+re.VERBOSE)
for fn in file_name:
  print(fn)