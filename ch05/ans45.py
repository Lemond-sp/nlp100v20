'''
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ．
・動詞を含む文節において，最左の動詞の基本形を述語とする
・述語に係る助詞を格とする
・述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
'''
class Chunk:
  def __init__(self,morphs,dst):
    self.morphs = morphs
    # 係り先(-1もある 17Dとかの17)
    self.dst = dst
    # 係り元文節の保存
    self.srcs = []


class Morph:
  def __init__(self,block):
    surface,attr = block.split('\t')
    attr = attr.split(',')
    # 句読点などの記号はNG
    self.surface = surface
    #self.surface = '' if attr[0] == '記号' else surface
    self.base = attr[6]
    # 記号は除去
    self.pos = attr[0]
    self.pos1 = attr[1]

class Sentence:
  def __init__(self,chunks):
    self.chunks = chunks
    for i ,chunk in enumerate(self.chunks):
      if chunk.dst not in [None,-1]:
        # chunks の dst番号対象
        self.chunks[chunk.dst].srcs.append(i)

filename = 'ai.ja/ai.ja.txt.parsed'
sentences = []
# chunkのインスタンス変数の集合
chunks = []
morphs = []

with open(filename) as f:
  for block in f:
    # Add Chunk
    if block[0] == "*":
      if len(morphs) > 0:
        chunks.append(Chunk(morphs,dst))
        morphs = []
      # 文字列の末尾部分を除去
      # 引数より除去される文字集合
      # 17D → 17
      dst = int(block.split(' ')[2].rstrip('D'))
    # Add Morph
    elif block != 'EOS\n':
      morphs.append(Morph(block))
    
    # paragraph
    else:
      chunks.append(Chunk(morphs,dst))
      sentences.append(Sentence(chunks))
      morphs = []
      chunks = []
      dst = None

'''
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
品詞が記号の場合、無視(空文字列)
+ 名詞から動詞
'''
# modiferをkeyとしてmodificationをリストのvalueにする
# forで追加後改めて表示する
sentences = sentences[7].chunks
for chunk in sentences:
  # 係り元
  modifier = ''.join([morph.base for morph in chunk.morphs if morph.pos == '助詞'])
  # 係り先
  modification = ''.join([morph.surface for morph in sentences[chunk.dst].morphs if morph.pos == '動詞'])
  if modifier and modification:
    print(modification,modifier,sep='\t')
