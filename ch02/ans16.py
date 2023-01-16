import pandas as pd
import sys
args = sys.argv

n = int(args[1])
df = pd.read_csv('popular-names.txt',sep='\t',header=None)

nrow = len(df) / n
# n分割表示
for i in range(n):
  print(df.loc[nrow * i:nrow * (i+1)])

'''
split -n 5 popular-names.txt
macOSでは オプションnがないため、-lで行う
split -l 5 popular-names.txt
'''