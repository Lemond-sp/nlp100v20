# ２次元リストを１次元リストに変換する方法
# における実行時間の比較
# https://qiita.com/kenta1984/items/39ffd8cb91078c972316
import random
import time
import itertools

random.seed(42)

# sum関数
x1 = [[random.randint(0,10) for i in range(50000)]]

start = time.time()
s1 = sum(x1,[])
sum_time = time.time() - start

# itertools
x2 = [[random.randint(0,10) for i in range(50000)]]
start = time.time()
s2 = itertools.chain.from_iterable(x2)
iter_time = time.time() - start

print(f'sum func: {sum_time}\nitertools: {iter_time}\
      \nsum関数はitertoolsの{(sum_time / iter_time):.3f}倍の計算時間')

'''
*rangeの値が少ない場合はsumの方が速い
sum func: 0.00011014938354492188
itertools: 4.0531158447265625e-06      
sum関数はitertoolsの27.176倍の計算時間
'''