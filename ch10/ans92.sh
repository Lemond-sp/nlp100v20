#!/bin/sh

fairseq-interactive --path contents/results/base/ans91/checkpoint10.pt \
                    --input /home/kajikawa_r/nlp100v20/ch10/contents/kftt-data-1.0/data/tok/kyoto-dev.ja \
                    --buffer-size 1024 --nbest 1 --max-len-b 50 \
                    | grep "^H-" | sort -V | cut -f3 > contents/results/kyoto.dev.txt
