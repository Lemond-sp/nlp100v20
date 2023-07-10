#!/bin/sh

DATA_DIR=/home/kajikawa_r/nlp100v20/ch10/contents/kftt-data-1.0/data/spm

# preprocess

fairseq-preprocess \
    --destdir contents/ans95.bin \
    --source-lang ja \
    --target-lang en \
    --trainpref $DATA_DIR/train \
    --validpref $DATA_DIR/dev \
    --testpref $DATA_DIR/test \
    --task translation

# train

CUDA_VISIBLE_DEVICES=0,1,2 fairseq-train contents/ans95.bin \
  --save-dir contents/results/base/ans95 \
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
| tee -a contents/results/base/train-spm.log
