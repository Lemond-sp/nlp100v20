'''
文中のすべての名詞を含む文節に対し，
その文節から構文木の根に至るパスを抽出せよ．
ただし，構文木上のパスは以下の仕様を満たすものとする．

・各文節は（表層形の）形態素列で表現する
・パスの開始文節から終了文節に至るまで，各文節の表現を” -> “で連結する
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

# 48
for sentence in sentences:
  for chunk in sentence.chunks:
    # 名詞が含まれている文節
    if '名詞' in [morph.pos for morph in chunk.morphs]:
      # chunk の表層形を接続
      path = [''.join([morph.surface for morph in chunk.morphs])]
      # 構文木の根に至るまで
      while chunk.dst != -1:
        path.append(''.join(morph.surface for morph in sentence.chunks[chunk.dst].morphs))
        chunk = sentence.chunks[chunk.dst]
      print(' -> '.join(path))
