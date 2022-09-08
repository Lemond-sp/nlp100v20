import pandas as pd

df = pd.read_csv('popular-names.txt',sep='\t',header=None)

df = df.sort_values(2,ascending=False)
print(df)

'''
sort -k 3 -r popular-names.txt
k:列指定
r:降順
'''