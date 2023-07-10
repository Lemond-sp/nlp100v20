"""
学習済みのsentencepieceより
実際にエンコードする
spm-model/tag : タグありのtrain で学習
今後はこれを用いてエンコードする
"""

import sentencepiece as spm
import argparse
import os

MODEL_PATH = "/home/kajikawa_r/nlp100v20/ch10/contents/spm/"
# 元データ
DATA_PATH = "/home/kajikawa_r/nlp100v20/ch10/contents/kftt-data-1.0/data/orig/"
# サブワード後のデータ
SPM_PATH = "/home/kajikawa_r/nlp100v20/ch10/contents/kftt-data-1.0/data/spm/"


def main():
    # train spm model
    spm.SentencePieceTrainer.Train(
        "--input=kftt-data-1.0/data/orig/kyoto-train.ja --model_prefix=contents/spm/kyoto.ja --vocab_size=16000 --character_coverage=1.0"
    )
    spm.SentencePieceTrainer.Train(
        "--input=kftt-data-1.0/data/orig/kyoto-train.en --model_prefix=contents/spm/kyoto.en --vocab_size=16000 --character_coverage=1.0"
    )

    langs = [".en", ".ja"]
    types = ["train", "test", "dev"]

    for lang in langs:
        # load sp model
        sp = spm.SentencePieceProcessor(
            model_file=MODEL_PATH + "kyoto" + lang + ".model"
        )
        for type in types:
            filename = "".join([type, lang])
            path = os.path.join(DATA_PATH, "tag", filename)
            spm_path = os.path.join(SPM_PATH, "tag", filename)
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
