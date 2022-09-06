def n_gram(text,n):
  return [text[i:i+n] for i in range(len(text) - n + 1)]

str1 = 'paraparaparadise'
str2 = 'paragraph'

X = set(n_gram(str1,2))
Y = set(n_gram(str2,2))
union = X | Y
intersection = X & Y
difference = X - Y
print(union,intersection,difference)
print('se' in X)
print('se' in Y)
