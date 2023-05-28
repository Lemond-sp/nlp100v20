import numpy as np
import os
from typing import List

# def main():
#     for i in ["label.dev.txt","label.train.txt","text.dev.txt","text.test.txt","text.train.txt"]:
#         load_data(i)

def load_data(path: str,data: str):
    with open(os.path.join(path,data)) as f:
        list_data = f.read().split('\n')
    del list_data[len(list_data) - 1]
    return list_data

# リスト内のテキストをsplitする
def sep_list(data: List):
    for i,seq in enumerate(data):
        data[i] = seq.split(' ')
    return data
# x_test = load_data('/home/kajikawa_r/nlp100v20/ch08/contents/','text_test.txt')

# print(len(x_test))
# if __name__ == "__main__":
#     main()