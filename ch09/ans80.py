"""
学習データ(train)中の単語にユニークな番号を付与
最も頻出する単語に１、次を２
学習データ中で2回以上出現する単語にIDを付与する。
与えられた単語列に対して、番号の列（リスト）を返す関数を実装
"""

import argparse

import numpy as np
import argparse
import pickle
import os
from collections import defaultdict
from tqdm import tqdm
import gensim
from gensim.models import KeyedVectors
from typing import List, Dict


def main(args):
    token_dict = defaultdict(int)
    id_dict = defaultdict(int)

    train_path = "/home/kajikawa_r/nlp100v20/ch09/contents/text.train.tst"
    output_path = "/home/kajikawa_r/nlp100v20/ch09/contents/train_id.txt"
    token_dict = count_token_num(token_dict, train_path)
    token_dict = dict(
        sorted(token_dict.items(), key=lambda token: token[1], reverse=True)
    )
    # 学習データの単語と頻度をファイル保存
    with open(output_path, "w") as fw:
        n = 1
        for token, freq in token_dict.items():
            if freq > 1:
                id_dict[token] = n
                fw.write(token + "\t" + str(n) + "\n")
                n += 1

    text = "in on the"
    ans = text2id(text, id_dict)
    print(ans)  # [1, 2, 9]


def text2id(text: str, id_dict):
    id_list = list()
    text = text.strip()
    tokens = text.split()
    for token in tokens:
        id_list.append(id_dict[token])
    return id_list


def count_token_num(d: Dict, filename):
    with open(filename) as f:
        for block in f:
            block = block.strip()
            tokens = block.split()
            for token in tokens:
                d[token] += 1
    del d["[UNK]"]  # 未知語は削除する
    return d


def check_vocab(filename: str, output: str, model):
    """
    1. テキストに対して，vocabに存在しない単語を[UNK]に置換
    2. ファイル保存
    """
    with open(filename) as f, open(output, "w") as fw:
        for block in f:
            sentence = block.split()
            apply_words = [
                word if word in model.index_to_key else "[UNK]" for word in sentence
            ]
            fw.write(" ".join(apply_words) + "\n")


# def cal_freq(vocab: Dict, filename: str):
#     with open(filename) as f:
#         for block in f:
#             tokens = block.split()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default=None)
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()
    main(args)
