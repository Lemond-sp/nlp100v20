fairseq-train contents/ans95.bin \
  --save-dir contents/results/base/ans96 \
  --tensorboard-logdir contents/results/base/log96 \
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
| tee -a contents/results/base/train-96.log
