'''
別解：collectionを用いる方法
'''
import MeCab
import collections
f = open('neko.txt')
text = f.read()  # ファイル終端まで全て読んだデータを返す
f.close()
m = MeCab.Tagger('-Ochasen')

node = m.parseToNode(text)
words = []
while node:
  words.append(node.surface)
  node = node.next

c = collections.Counter(words)
print(c.most_common(10))
# mecab -oしたものと少し異なる
# [('の', 9194), ('。', 7486), ('て', 6873), ('、', 6772), ('は', 6422), ('に', 6268), ('を', 6071), ('と', 5515), ('が', 5339), ('た', 3989)]