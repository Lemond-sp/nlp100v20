f = open('popular-names.txt','r')
line_size = 0
for data in f:
  line_size+=1
print(line_size)


'''
wc -l popular-names.txt
wc ファイル名なら
行数(改行数 -l)、単語数(-w)、バイト数(-c) を表示
'''