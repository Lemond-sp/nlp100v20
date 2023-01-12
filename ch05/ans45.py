'''
動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ．
・動詞を含む文節において，最左の"動詞の基本形"を述語とする
・述語に係る"助詞"を格とする
・述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
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

'''
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
品詞が記号の場合、無視(空文字列)
+ 名詞から動詞
'''

with open("./result45.txt", "w") as f:
  for i in range(len(sentences)):
    for chunk in sentences[i].chunks:
      for morph in chunk.morphs:
        if morph.pos == "動詞": 
          particles = []
          for src in chunk.srcs:
            particles += [morph.base for morph in sentences[i].chunks[src].morphs if morph.pos == "助詞"]
          if len(particles) > 1:
            particles = set(particles)
            particles = sorted(list(particles))
            form = " ".join(particles)
            print(f"{morph.base}\t{form}", file=f)

'''
cat ./result45.txt | sort |uniq -c | sort -nr |head -n 5
cat ./result45.txt |grep '行う'| sort |uniq -c | sort -nr |head -n 5

'''