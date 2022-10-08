# ２次元リストを１次元リストに変換する方法
# における実行時間の比較
# https://qiita.com/kenta1984/items/39ffd8cb91078c972316
import random
import time
import itertools

random.seed(42)

# sum関数
x1 = [[random.randint(0,10) for i in range(5)]]
print(x1)

start = time.time()
s1 = sum(x1,[])
sum_time = time.time() - start

# itertools
x2 = [[random.randint(0,10) for i in range(5)]]
start = time.time()
s2 = itertools.chain.from_iterable(x2)
iter_time = time.time() - start

print(f'sum func: {sum_time}\nitertools: {iter_time}\
      \nsum関数はitertoolsの{sum_time / iter_time}倍の計算時間')

'''
[[10, 1, 0, 4, 3]]
sum func: 1.9073486328125e-06
itertools: 0.000186920166015625      
sum関数はitertoolsの0.01020408163265306倍の計算時間
sum関数の方が早い？(記事中ではitertoolsの方が高速らしい)
'''