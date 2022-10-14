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