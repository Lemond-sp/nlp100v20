"""
学習済みのsentencepieceより
実際にエンコードする
spm-model/tag : タグありのtrain で学習
今後はこれを用いてエンコードする
"""

import sentencepiece as spm
import argparse
import os

MODEL_PATH = "/home/kajikawa_r/nlp100v20/ch10/contents/"
# 元データ
DATA_PATH = "/home/kajikawa_r/nlp100v20/ch10/contents/kftt-data-1.0/data/orig"
# サブワード後のデータ
SPM_PATH = "/home/kajikawa_r/nlp100v20/ch10/contents/kftt-data-1.0/data/spm-jpara"


def main():
    langs = [".en", ".ja"]
    types = ["train", "test", "dev"]

    for lang in langs:
        # load sp model
        sp = spm.SentencePieceProcessor(model_file=MODEL_PATH + "model_pblc.model")
        for type in types:
            filename = "".join([type, lang])
            path = os.path.join(DATA_PATH, filename)
            spm_path = os.path.join(SPM_PATH, filename)
            subword(sp, path, spm_path)


def subword(sp, path, spmpath):
    fout = open(spmpath, "w")
    fin = open(path)
    for line in fin:
        fout.write(" ".join(sp.EncodeAsPieces(line)) + "\n")
    fin.close()
    fout.close()


if __name__ == "__main__":
    main()
