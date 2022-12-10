def report(x,y,z):
  #rep = str(x) + "時の" + y + "は" +str(z)
  #rep = '{}時の{}は{}'.format(x,y,z)
  rep = f'{x}時の{y}は{z}'
  return rep
print(report(12,"気温",22.4))

'''
f-stringsは3.6以降
f'{x}' と直接・シンプル

Python3.8では、{変数名=}とすることで、
変数名=変数の値という形の埋め込みが可能

# `=`で変数名と値を両方表示
    print(f"{x=}") # x=値
'''