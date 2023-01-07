# 続きは、リーディングリスト(参照サイト)を見ながらする
"""
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
26 : 強調マークアップの除去
27 : 内部リンクマークアップの除去
28 : 27の出力より、{}(中括弧、ブレース)などがとれる
"""

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
for k,v in ans.items():
  print(f'{k} : {v}')

'''
国歌 : 女王陛下万歳|{{lang|en|God Save the Queen}}{{en icon}}<br />神よ女王を護り賜え<br />{{center|ファイル:United States Navy Band - God Save the Queen.ogg}}
公式国名 : {{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br />
他元首等氏名2 : {{仮リンク|リンゼイ・ホイル|en|Lindsay Hoyle}}
確立年月日4 : 1927年{{0}}4月12日
'''