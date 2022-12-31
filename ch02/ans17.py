import pandas as pd

df = pd.read_csv('popular-names.txt',sep='\t',header=None)
#df[0]でも
print(df.iloc[:,0].unique())

'''
cut  : 横方向に分割する
sort : 昇順
uniq : 重複している行の削除
cut -f 1 popular-names.txt | sort | uniq
'''