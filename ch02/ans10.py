f = open('popular-names.txt','r')
line_size = 0
for data in f:
  line_size+=1
print(line_size)


'''
wc -l popular-names.txt
wc ファイル名なら
行数、単語数、バイト数 を表示
'''