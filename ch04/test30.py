from cgitb import text
import re
#text = '表層形  品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音'
#複数のタブがある場合
# 1,2,3,7
with open('./neko.txt.mecab','r') as f:
  text_dict = []
  sentence_dict = []
  n = 0
  # f.read:改行も含めた文字列
  # f.readlines:改行コードを区切って１行ごとに分解されたリスト
  for line in f.readlines():
    print(line)
    n += 1
    if n == 10:
      break
 '''
 output
 EOS\n や 無駄な改行 がある
 一      名詞,数,*,*,*,*,一,イチ,イチ



        記号,一般,*,*,*,*,*

EOS



        記号,一般,*,*,*,*,*

EOS

　      記号,空白,*,*,*,*,　,　,　

吾輩    名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ

は      助詞,係助詞,*,*,*,*,は,ハ,ワ
 '''