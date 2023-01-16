"""
各行の1列目の文字列の出現頻度を求め その高い順に並べて表示せよ。確認にはcut, uniq, sortコマンドを用いよ。
"""
import pandas as pd

df = pd.read_csv('popular-names.txt',sep='\t',header=None)
print(df.head())
print(df[0].value_counts())

'''
cut -f 1 popular-names.txt \ # １列目の文字列を抽出
  | sort | uniq -c | sort -nr | head -n 5 # 出現回数順に並べる

cut -f 1 popular-names.txt | sort | uniq -c | sort -nr | head -n 5

https://blog.y-yuki.net/entry/2019/08/12/220000
'''