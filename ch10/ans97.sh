# base model
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

# optimizer
CUDA_VISIBLE_DEVICES=0,1,2 fairseq-train contents/ans95.bin \
  --save-dir contents/results/base/ans95 \
  --task translation \
  --arch transformer \
  --max-tokens 4096 \
  --optimizer adagrad \
  --reset-optimizer --reset-dataloader --reset-lr-scheduler \
  --source-lang ja --target-lang en \
  --max-epoch 10 \
  --lr 1e-4 \
  --lr-scheduler inverse_sqrt --warmup-updates 2000 \
  --criterion label_smoothed_cross_entropy \
| tee -a contents/results/base/train-spm.log

# epoch
CUDA_VISIBLE_DEVICES=0,1,2 fairseq-train contents/ans95.bin \
  --save-dir contents/results/base/ans95 \
  --task translation \
  --arch transformer \
  --max-tokens 4096 \
  --optimizer adam \
  --reset-optimizer --reset-dataloader --reset-lr-scheduler \
  --source-lang ja --target-lang en \
  --max-epoch 30 \
  --lr 1e-4 \
  --lr-scheduler inverse_sqrt --warmup-updates 2000 \
  --criterion label_smoothed_cross_entropy \
| tee -a contents/results/base/train-spm.log

