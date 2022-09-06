import random
str = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
str = str.split()
ans = []
for word in str:
  if len(word) > 4:
    #先頭と末尾の文字以外の取り出し・shuffleはリスト化
    mid = list(word[1:-1])
    random.shuffle(mid)
    word = word[0] + ''.join(mid) + word[-1]
    ans.append(word)
  else:
    ans.append(word)
print(' '.join(ans))