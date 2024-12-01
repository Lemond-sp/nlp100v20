import re

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print(sentence)
sentence = re.sub("[,|.]", "", sentence)
print(sentence)
ans = sentence.split()
print(ans)
# 各単語の文字数
ans = [len(i) for i in ans]
print(ans)

"""
https://docs.python.org/ja/3/library/re.html#re.sub
re.sub(pattern,replace,string,count=0,flags=0)
pattern → replace

['Now', 'I', 'need', 'a', 'drink', 'alcoholic', 'of', 'course', 'after', 'the', 'heavy', 'lectures', 'involving', 'quantum', 'mechanics']
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
"""
