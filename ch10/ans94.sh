#!/bin/sh

for N in {1..20}
do
fairseq-interactive --path contents/results/base/ans91/checkpoint10.pt \
                    --input /home/kajikawa_r/nlp100v20/ch10/contents/kftt-data-1.0/data/tok/kyoto-dev.ja \
                    --buffer-size 1024 --nbest 1 --max-len-b 50 \
                    --beam $N \
                    | grep "^H-" | sort -V | cut -f3 > contents/results/kyoto.dev.$N.txt
done

for N in {1..20}
do
    sacrebleu  /home/kajikawa_r/nlp100v20/ch10/contents/kftt-data-1.0/data/tok/kyoto-dev.en -i contents/results/kyoto.dev.$N.txt  > contents/results/beam.$N.score
done
