'''
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
品詞が記号の場合、無視(空文字列)
'''
import re

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
    self.surface = '' if attr[0] == '記号' else surface
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
'''
for chunk in sentences[2].chunks:
  # dst 番号が srcにあればsurface表示
  print(''.join(morph.surface for morph in chunk.morphs) + '\t' +\
    # sentences[2]より、文節全体を対象とする
    ''.join(morph.surface for morph in sentences[2].chunks[chunk.dst].morphs))
