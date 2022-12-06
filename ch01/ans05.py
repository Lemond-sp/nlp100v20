'''
与えられたシーケンス（文字列やリスト など)から
n-gramを作る関数
'''
def n_gram(text,n):
  return [text[i:i+n] for i in range(len(text) - n + 1)]

sentence = "I am an NLPer"
#文字bi-gram
print(n_gram(sentence,2))
sentence = sentence.split()
#単語bi-gram
print(*n_gram(sentence,2))
'''
['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
['I', 'am'] ['am', 'an'] ['an', 'NLPer']
'''