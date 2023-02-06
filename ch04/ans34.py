# 名詞の連接(連続して出現する名詞)を最長一致で抽出
# ans30
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
      # surfaceが空白の場合除外
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
    # 追加文が無い場合は除外(elseだと、つまり無い場合も追加したら9210→9964)
    elif len(sentence_dict) != 0:
      text_dict.append(sentence_dict)
      sentence_dict = []

#ans34
# 名詞の連接を最長一致で表示

import itertools
verb_dict = []
sentence_dict = itertools.chain.from_iterable(text_dict)
# 名詞の連接
noun_connect = []

# 一覧
noun_seq = []
for sentence in sentence_dict:
  if sentence['pos'] == '名詞':
    noun_connect.append(sentence['surface'])
  elif len(noun_connect) > 1:
    noun_seq.append(noun_connect)
    noun_connect = []
  else: # 1 or 0(1はそもそも連接ではない)
    noun_connect = []
    continue

for max_noun in noun_seq:
  print(*max_noun)