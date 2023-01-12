'''
形態素を表すクラスMorphの実装
surface,base,pos,pos1をメンバ変数にもつ。
ai.ja.txt.parsedを読み込み、
各文をMorphオブジェクトのリストとして表現し，
冒頭の説明文の形態素列を表示せよ．
表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
'''
class Morph:
  def __init__(self,block):
    surface,attr = block.split('\t')
    attr = attr.split(',')
    self.surface = surface
    self.base = attr[6]
    self.pos = attr[0]
    self.pos1 = attr[1]

filename = 'ai.ja/ai.ja.txt.parsed'
sentence = []
ans = []

# mode='r'(default)
with open(filename) as f:
  for block in f:
    if block[0] == "*": # *の場合、次の行へ
      continue
    # 対象
    elif block != "EOS\n":
      ans.append(Morph(block))
    # 空リストではない
    elif ans:
      sentence.append(ans)
      ans = []

# 確認
# vars(x):オブジェクトxの__dic__属性を辞書で返す
# dict属性には、プロパティの名前と対応付けられている値が入る
for i in sentence[1]:
  print(vars(i))