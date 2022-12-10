import random
random.seed(42)

sentence = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
sent_list = sentence.split()
ans = []

for word in sent_list:
  if len(word) > 4:
    #先頭と末尾の文字以外の取り出し・shuffleはリスト化
    mid = list(word[1:-1])
    random.shuffle(mid)
    word = word[0] + ''.join(mid) + word[-1]
    ans.append(word)
  else:
    ans.append(word)
print(sentence)
print(' '.join(ans))

'''
I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .
I cdulno’t beievle that I cuold atulcaly uanentsdrd what I was rdaeing : the penaoehnml pweor of the haumn mind .
'''