import pandas as pd

df = pd.read_csv('popular-names.txt',sep='\t',header=False)
df.iloc[:,0].to_csv('col1.txt',index=False,header=False)
df.iloc[:,1].to_csv('col2.txt',index=False,header=False)

'''
cut -f 1 popular-names.txt >> col1-sh.txt
cut -f 2 popular-names.txt >> col2-sh.txt
'''