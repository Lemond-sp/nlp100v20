x = "パタトクカシーー"
ans = x[::2]
print(ans)

'''
ans = str[0] + str[2] + str[4] + str[6]
i個飛ばし で要素を取得
list[::i]
２つ目の:から指定
'''

'''
文字列を2文字ずつ分割
import re
buf = 'abccdef'
list = re.split('(..)',buf)[1::2]
print list
>>>['ab', 'cd', 'ef']
'''