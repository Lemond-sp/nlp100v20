'''
与えられたシーケンス（文字列やリスト など)から
n-gramを作る関数
'''
def n_gram(text,n):
  return [text[i:i+n] for i in range(len(text) - n + 1)]

sentence = "I am an NLPer"
char_seq = sentence.replace(' ','')
#文字bi-gram
print(n_gram(char_seq,2))
sentence = sentence.split()
#単語bi-gram
print(*n_gram(sentence,2))
'''
['Ia', 'am', 'ma', 'an', 'nN', 'NL', 'LP', 'Pe', 'er']
['I', 'am'] ['am', 'an'] ['an', 'NLPer']
'''