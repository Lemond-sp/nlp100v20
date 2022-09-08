import pandas as pd

df1 = pd.read_csv('col1.txt',header=None)
df1 = df1.rename(columns={0:'name'})
df2 = pd.read_csv('col2.txt',header=None)
df2 = df2.rename(columns={0:'sex'})
df = pd.concat([df1,df2],axis=1)
print(df)

#テキストファイル

df.to_csv("col1_2.txt",sep='\t',index=False,header=None)

'''
paste:複数のファイルを行単位に連結、標準出力に出力
paste col1.txt col2.txt | head
'''