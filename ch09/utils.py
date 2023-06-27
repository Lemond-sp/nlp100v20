from utils import load_data, sep_list
import torch
import torch.nn as nn
import numpy as np
import argparse
import pickle
import os
from tqdm import tqdm
import gensim
from gensim.models import KeyedVectors
from typing import List


# 86は n_layers=k(k > 1), bidirectional=True
class RNN(nn.Module):
    def __init__(
        self,
        n_input,
        n_embed=300,
        n_hidden=50,
        n_layers=1,
        n_output=4,
        dropout=0.2,
        bidirectional=False,
    ):
        super().__init__()

        self.embed = nn.Embedding(
            num_embeddings=n_input, embedding_dim=n_embed, padding_idx=0
        )
        self.rnn = nn.RNN(
            input_size=n_embed,
            hidden_size=n_hidden,
            num_layers=n_layers,
            batch_first=True,
        )
        self.fc = nn.Linear(
            in_features=n_hidden,
            out_features=n_output,
        )
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x, h_0=0):
        x = self.embed(x)
        x, h_t = self.rnn(x, h_0)
        x = x[:, -1, :]
        x = self.fc(x)
        x = self.softmax(x)
        return x


def text2id(text: str, id_dict):
    id_list = list()
    text = text.strip()
    tokens = text.split()
    for token in tokens:
        id_list.append(id_dict[token])
    return id_list


def s2v(sentence: List, d_size=300):
    """
    sentence to vector
    average word vectors
    """
    vectors = []
    # vocabに存在するもののみ
    apply_words = [word for word in sentence if word in model.index_to_key]

    # 対象語彙が存在するテキストのみmodel適用
    if len(apply_words) != 0:
        sentence_vec = np.mean(model[apply_words], axis=0)
    else:
        print(f"{sentence} is not vocab !")
        sentence_vec = np.zeros((d_size,))  # 未知語処理（任意の値を入れる手法もある）

    return sentence_vec
