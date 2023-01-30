"""
29 :国旗画像のURLの取得
テンプレートの内容を利用し，国旗画像のURLを取得せよ．
（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
https://note.nkmk.me/python-requests-usage/
https://www.mediawiki.org/wiki/API:Imageinfo/ja#Python
"""

#25 :テンプレートの抽出、辞書作成
import pandas as pd
import re
import requests

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

#27 :内部リンクの除去(詳細はans27.pyへ)
r = re.compile('\[\[(.+\||)(.+?)\]\]')
ans = {k: r.sub(r'\2', v) for k, v in ans.items()}
"""for k,v in ans.items():
  print(f'{k} : {v}')"""

# 28 :{}の除去(24:メディアファイルは該当しないので無視)
r = re.compile('\{\{(.+\||)(.+?)\}\}')
ans = {k: r.sub(r'\2', v) for k, v in ans.items()}

# おまけ：メディアファイル
# python ans27.py | grep "国歌"
# python ans28.py | grep "国歌" で差分確認
r = re.compile('\[\[ファイル:(.+?)\}\}')
ans = {k: r.sub(r'\1', v) for k, v in ans.items()}

# 29 :国旗画像
flag_file = ans['国旗画像']
flag_file = flag_file.replace(' ','_')

title = "File:" + flag_file
S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action":"query",
    "format":"json",
    "prop":"imageinfo",
    "titles":title,
    "iiprop":"url"
}
R = S.get(url=URL, params=PARAMS)

DATA = R.json()

PAGES = DATA["query"]["pages"]
for v in PAGES.values():
  print(v["imageinfo"][0]["url"]) # https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg