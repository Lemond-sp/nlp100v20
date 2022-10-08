'''
mecab -o ./neko.txt.mecab ./neko.txt

解析結果を読み込むプログラムの実装
各形態素
surface,base,pos,pos1 をキーとする辞書型
表層形、基本形(原形)、品詞、品詞細分類1
mecabの出力フォーマット
表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
#\u3000 : 全角スペース
'''
import re
#指定された要素を全て削除(したものを別リストに格納)
with open('./neko.txt.mecab','r') as f:
  text_dict = []
  sentence_dict = []
  # f.read:改行も含めた文字列
  # f.readlines:改行コードを区切って１行ごとに分解されたリスト
  for line in f.readlines():
    if line == '\n':
      continue
    # １文
    elif line != 'EOS\n':
      node = line.split('\t')
      if node[0] == '':
        continue
      # surface 以外はnode[1]
      feature = node[1].split(',')
      word_dict = {
        "surface":node[0],
        "base":feature[6],
        "pos":feature[0],
        "pos1":feature[1]
      }
      sentence_dict.append(word_dict)
    # 追加
    text_dict.append(sentence_dict)
    sentence_dict = []

  print(len(text_dict))
  for i in text_dict[:5]:
    for j in i:
      print(j)
    print(' ')