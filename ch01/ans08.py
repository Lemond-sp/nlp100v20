def cipher(lst):
  for i,c in enumerate(lst):
    # 英字 and 小文字
    if lst[i].isalpha() and lst[i].islower():
      # ord :unicode変換
      lst[i] = 219 - ord(lst[i])
  return lst

ch = 'Ab12'
lst = list(ch)
print(f'before :{lst}')
print(f'cipher :{cipher(lst)}')
'''
文字列は不変 immutable
リストに変換すると、更新可能
['A', 121, '1', '2']
'''