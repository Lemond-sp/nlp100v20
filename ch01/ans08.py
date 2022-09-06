def cipher(lst):
  for i,c in enumerate(lst):
    if lst[i].isalpha() and lst[i].islower():
      lst[i] = 219 - ord(lst[i])
  return lst

str = 'Ab12'
lst = list(str)
print(cipher(lst))
'''
文字列は不変 immutable
リストに変換すると、更新可能
['A', 121, '1', '2']
'''