sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
sentence = sentence.split()
print(sentence)
#先頭の1文字のみ
one_ch = [0, 4, 5, 6, 7, 8, 14, 15, 18]
ans = {}
for i,word in enumerate(sentence):
  #先頭から何番目の単語か
  if i in one_ch:
    ans[word[0]] = i + 1
  else:
    ans[word[:2]] = i + 1
print(ans)

'''
['Hi', 'He', 'Lied', 'Because', 'Boron', 'Could', 'Not', 'Oxidize', 'Fluorine.', 'New', 'Nations', 'Might', 'Also', 'Sign', 'Peace', 'Security', 'Clause.', 'Arthur', 'King', 'Can.']
{'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20}
'''