'''
名詞間の係受けパスの抽出
文中の全ての名詞句のペアを結ぶ「最短」係受けパスの抽出
1:文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
2:上記以外で、文節iとjから構文木の根に至る経路上で共通の文節kで交わる場合
  文節iからkに至る直前のパスと文節jからkに至る直前までのパス、
  文節kの内容を"|"で連結して表示

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

# 49
from itertools import combinations
import re

# sentence[1]

for sentence in sentences:
  nouns = []
  for i,chunk in enumerate(sentence.chunks):
    if '名詞' in [morph.pos for morph in chunk.morphs]:
      nouns.append(i) # 名詞が含まれている文節番号

  for i,j in combinations(nouns,2): # 全ての名詞句のペア
    path_i = []
    path_j = []
    while i != j:
      if i < j:
        path_i.append(i)
        i = sentence.chunks[i].dst # 係り先
      else:
        path_j.append(j)
        j = sentence.chunks[j].dst
    
    if len(path_j) == 0:
      chunk_X = ''.join([morph.surface if (morph.pos != '名詞' and morph.pos != '記号') else 'X' for morph in sentence.chunks[path_i[0]].morphs])
      chunk_Y = ''.join([morph.surface if (morph.pos != '名詞' and morph.pos != '記号') else 'Y' for morph in sentence.chunks[i].morphs])
      chunk_X = re.sub('X+', 'X', chunk_X) # Xを１個に制限
      chunk_Y = re.sub('Y+', 'Y', chunk_Y)
      path_XtoY = [chunk_X] + [''.join([morph.surface for morph in sentence.chunks[n].morphs if morph.pos != '記号']) for n in path_i[1:]] + [chunk_Y]
      print(' -> '.join(path_XtoY))
    else:
      chunk_X = ''.join([morph.surface if (morph.pos != '名詞' and morph.pos != '記号') else 'X' for morph in sentence.chunks[path_i[0]].morphs])
      chunk_Y = ''.join([morph.surface if (morph.pos != '名詞' and morph.pos != '記号') else 'Y' for morph in sentence.chunks[path_j[0]].morphs])
      chunk_k = ''.join([morph.surface for morph in sentence.chunks[i].morphs if morph.pos != '記号'])
      chunk_X = re.sub('X+', 'X', chunk_X)
      chunk_Y = re.sub('Y+', 'Y', chunk_Y)
      path_X = [chunk_X] + [''.join([morph.surface for morph in sentence.chunks[n].morphs if morph.pos != '記号']) for n in path_i[1:]]
      path_Y = [chunk_Y] + [''.join([morph.surface for morph in sentence.chunks[n].morphs if morph.pos != '記号']) for n in path_j[1:]]
      print(' | '.join([' -> '.join(path_X), ' -> '.join(path_Y), chunk_k]))

# 48
"""for sentence in sentences:
  for chunk in sentence.chunks:
    # 名詞が含まれている文節
    if '名詞' in [morph.pos for morph in chunk.morphs]:
      # chunk の表層形を接続
      path = [''.join([morph.surface for morph in chunk.morphs])]
      # 構文木の根に至るまで
      while chunk.dst != -1:
        path.append(''.join(morph.surface for morph in sentence.chunks[chunk.dst].morphs))
        chunk = sentence.chunks[chunk.dst]
      print(' -> '.join(path))"""