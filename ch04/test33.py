# 配列から複数の要素を同時に取り出す方法
# https://qiita.com/Akio-1978/items/c003783517df23d360d0
test_data = [1,2,3,4,5]

# 最大でsizeつずつ取り出したい
size = int(input())
# 結局スライス以外ないらしい
for start in range(0, len(test_data), size):
    print(test_data[start : start + size])