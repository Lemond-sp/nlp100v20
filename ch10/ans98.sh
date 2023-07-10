
# 準備
# unkタグの割合が示してある
# --destdir :バイナリデータの保存場所(def:data-bin)
ENDICT='/home/kajikawa_r/competition/gradcomp/ch03/model/big-enja/dict.en.txt'
JADICT='/home/kajikawa_r/competition/gradcomp/ch03/model/big-enja/dict.ja.txt'

fairseq-preprocess --source-lang ja --target-lang en \
                --trainpref contents/kftt-data-1.0/data/spm-jpara/train \
                --validpref contents/kftt-data-1.0/data/spm-jpara/dev \
                --testpref contents/kftt-data-1.0/data/spm-jpara/test \
                --destdir enja --srcdict $ENDICT --tgtdict $JADICT \
                --destdir contents/data98

# finetune

PRETRAINED_MODEL="/content/drive/MyDrive/big-3.0-jaen/big.pretrain.pt"
SEED=10

! fairseq-train contents/data98 --arch transformer --restore-file PRETRAINED_MODEL --no-epoch-checkpoints \
    --seed SEED --patience 10 \
    --batch-size 16 --optimizer adam --adam-betas '(0.9,0.98)' --lr 1e-4 --lr-scheduler inverse_sqrt --warmup-updates 4000 --warmup-init-lr 1e-07 \
    --dropout 0.1 --weight-decay 0.0001 --clip-norm 1.0 \
    --reset-optimizer --reset-meters --reset-dataloader --reset-lr-scheduler \
    --criterion label_smoothed_cross_entropy --label-smoothing 0.1 \
    --encoder-embed-dim 1024 --decoder-embed-dim 1024 \
    --encoder-ffn-embed-dim 4096 --decoder-ffn-embed-dim 4096 \
    --encoder-attention-heads 16 --decoder-attention-heads 16 \
    --log-interval 100 --validate-interval-updates 9999 --save-interval-updates 1000
