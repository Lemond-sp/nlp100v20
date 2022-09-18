'''
mecab -o ./neko.txt.mecab ./neko.txt
'''

#デフォルト mode='r'
with open('./neko.txt.mecab') as f:
  morpheme = [s.strip() for s in f.readlines()]
  #リスト内の空白の要素の削除
  morpheme.remove('')
  for i in range(0,3):
    print(morpheme[i])