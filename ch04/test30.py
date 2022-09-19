import re
text = '表層形  品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音'
print(text)
print('-'*50)
f1 = text.split('\t')
print(f1)

print('-'*50)
'''
複数の条件で分割 re.split
謎の空白の要素が生成されるので removeで無理矢理消した
'''
f2 = re.split('[  ,]',text)
f2.remove('')
print(f2)