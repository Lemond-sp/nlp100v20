import pandas as pd
import sys
args = sys.argv

df = pd.read_csv('popular-names.txt',sep='\t',header=None)
#args[0]はpyファイル名
n = int(args[1])
print(df.head(n))
'''
N=5の場合
head -n 5 popular-names.txt
'''