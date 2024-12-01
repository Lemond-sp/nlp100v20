str1 = "パトカー"
str2 = "タクシー"

# ['パタ', 'トク', 'カシ', 'ーー']
ans = [i + j for i, j in zip(str1, str2)]

# パタトクカシーー
ans = "".join(ans)
print(ans)
