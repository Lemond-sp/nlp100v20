str1 = "パトカー"
str2 = "タクシー"
ans = [i + j for i, j in zip(str1, str2)]
print(ans)
ans = "".join(ans)
print(ans)
"""
['パタ', 'トク', 'カシ', 'ーー']
パタトクカシーー

l = ['aaa', 'bbb', 'ccc']
s = "-".join(l)
>>>'aaa-bbb-ccc'
"""
