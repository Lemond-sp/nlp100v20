#!/bin/sh

DATA_DIR=/home/kajikawa_r/nlp100v20/ch10/contents/kftt-data-1.0/data/tok

# preprocess

fairseq-preprocess \
    --destdir contents/ans91.bin \
    --source-lang ja \
    --target-lang en \
    --trainpref $DATA_DIR/kyoto-train.cln \
    --validpref $DATA_DIR/kyoto-dev \
    --testpref $DATA_DIR/kyoto-test \
    --task translation

# train

fairseq-train contents/ans91.bin \
  --save-dir contents/results/base/ans91 \
  --task translation \
  --arch transformer \
  --max-tokens 4096 \
  --optimizer adam \
  --reset-optimizer --reset-dataloader --reset-lr-scheduler \
  --source-lang ja --target-lang en \
  --max-epoch 10 \
  --lr 1e-4 \
  --lr-scheduler inverse_sqrt --warmup-updates 2000 \
  --criterion label_smoothed_cross_entropy \
| tee -a contents/results/base/train.log
