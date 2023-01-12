'''
40に加えて、分節を示すクラスChunkの実装
形態素（Morphオブジェクト）のリスト（morphs），
係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数
冒頭の説明文の文節の文字列と係り先を表示
'''

# 文節
class Chunk:
  def __init__(self,morphs,dst):
    # 形態素のリスト(morphs)
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

# 文節(chunks)リスト
class Sentence:
  def __init__(self,chunks):
    self.chunks = chunks
    # i が文節番号
    # そもそもEOSで文節ごとに分割しているため、
    # その文節を超えた i は指定されることはない。
    for i ,chunk in enumerate(self.chunks):
      # 係先があるか
      if chunk.dst not in [None,-1]:
        # ex)i番目に17Dがあれば、17のchunk.srcsにiを格納
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
      dst = None # 初期化

for chunk in sentences[2].chunks:
  print([morph.surface for morph in chunk.morphs], chunk.dst, chunk.srcs)
'''
['人工', '知能'] 17 []
['（', 'じん', 'こうち', 'のう', '、', '、'] 17 []
'''