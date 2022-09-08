import pandas as pd

df = pd.read_csv('popular-names.txt',sep='\t',header=None)
#df[0]でも
print(df.iloc[:,0].unique())

'''
uniq popular-names.txt | cut -f 1
'''