'''
40に加えて、分節を示すクラスChunkの実装
形態素（Morphオブジェクト）のリスト（morphs），
係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数
冒頭の説明文の文節の文字列と係り先を表示
'''


class Chunk:
  def __init__(self,morphs,dst):
    self.morphs = morphs
    # 係り先
    self.dst = dst
    # 係り元文節の保存
    self.srcs = []


class Morph:
  def __init__(self,block):
    surface,attr = block.split('\t')
    attr = attr.split(',')
    self.surface = surface
    self.base = attr[6]
    self.pos = attr[0]
    self.pos1 = attr[1]

class Sentence:
  def __init__(self,chunks):
    self.chunks = chunks
    for i ,chunk in enumerate(self.chunks):
      if chunk.dst not in [None,-1]:
        self.chunks[chunk.dst].srcs.append(i)

filename = 'ai.ja/ai.ja.txt.parsed'
sentences = []
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

for chunk in sentences[2].chunks:
  print([morph.surface for morph in chunk.morphs], chunk.dst, chunk.srcs)
'''
['人工', '知能'] 17 []
['（', 'じん', 'こうち', 'のう', '、', '、'] 17 []
'''