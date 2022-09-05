str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str = str.split()
print(str)
#先頭の1文字のみ
one_ch = [0, 4, 5, 6, 7, 8, 14, 15, 18]
ans = {}
for i,word in enumerate(str):
  #先頭から何番目の単語か
  if i in one_ch:
    ans[word[0]] = i
  else:
    ans[word[:2]] = i
print(ans)