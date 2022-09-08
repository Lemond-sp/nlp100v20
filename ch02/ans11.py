import pandas as pd

#read_csvでも可
df = pd.read_table('popular-names.txt',sep='\t',header=None)
df.to_csv("res11.txt",sep=' ',index=False,header=False)

'''
read_csv
sed コマンドにより、
sed -e 's/\t/ /g' popular-names.txt >> res11-sh.txt
-e:文字列の置換を行う
g:各行に出現する全ての対象文字列を置換する

'''