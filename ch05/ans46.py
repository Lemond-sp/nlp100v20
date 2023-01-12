'''
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格と
項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
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

with open("./result46.txt", "w") as f:
  for i in range(len(sentences)):
    for chunk in sentences[i].chunks:
      for morph in chunk.morphs:
        if morph.pos == "動詞": 
          particles = []
          items = []
          for src in chunk.srcs:
            particles += [morph.surface for morph in sentences[i].chunks[src].morphs if morph.pos == "助詞"]
            items += ["".join([morph.surface for morph in sentences[i].chunks[src].morphs if morph.pos != "記号"])]
          if len(particles) > 1:
            if len(items) > 1:
              particles = sorted(set(particles))
              items = sorted(set(items))
              particles_form = " ".join(particles)
              items_form = " ".join(items)
              print(f"{morph.base}\t{particles_form}\t{items_form}", file=f)
