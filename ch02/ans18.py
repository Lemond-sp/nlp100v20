import pandas as pd

df = pd.read_csv("popular-names.txt", sep="\t", header=None)

df = df.sort_values(2, ascending=False)
print(df.head(5))

"""
対象列が文字列として認識され、数値としてソーティングされていなかった
sort -rnk 3 popular-names.txt | head -n 5
r : 降順
n : 文字列を数値と見なして並べ替える
k : 列指定

-rnk -nrk としてもいい
-(１つ以上のオプション)(パラメータを使うオプション) [パラメータ] の順で実行する
"""
