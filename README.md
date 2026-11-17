# Sea-only Vast.ai experiments

This repository is the Sea-only Qwen3.5-9B LoRA pipeline for Vast.ai.
It uses ordinary 16-bit LoRA (not QLoRA/NF4), masked SFT, checkpoint/resume,
and scheduled CoT loss. Only the dataset, Sea taxonomy, and naval prompts differ
from the corresponding Air pipeline.

Dataset: `KhanhChien/Data-Qwen3.5-SFT-Sea-Only`

The dataset was verified against the local copy used for this pipeline:
2,781 training rows, 309 validation rows, and 403 real-test rows. Its schema includes
`gt_class`, `system_prompt`, `user_prompt`, and `assistant_cot`.
The code validates every target against the 21 labels in `sea_prompts.py`.
CoT modes retain each record's original `system_prompt`, `user_prompt`, and
`assistant_cot`. Only direct mode replaces the prompt and target.
On Vast.ai, use the dataset repo ID for training and the downloaded Parquet paths
for inference.

## Scheduled CoT training

```powershell
torchrun --standalone --nproc_per_node=1 train_sea_vast.py `
  --parquet_dir KhanhChien/Data-Qwen3.5-SFT-Sea-Only `
  --output_dir ./outputs/sea_scheduled_cot `
  --mode scheduled_cot --model_id Qwen/Qwen3.5-9B `
  --epochs 3 --stop_after_epoch 1 `
  --batch_size 2 --grad_accum 8 --lr 2e-4 `
  --lora_r 16 --lora_alpha 32 --max_seq_length 1280 `
  --cot_weight_start 1.0 --cot_weight_end 0.5 --answer_weight 1.0 `
  --save_steps 100 --logging_steps 10 --eval_steps 100
```

For subsequent epochs, keep all settings unchanged and change only
`--stop_after_epoch 2` or `--stop_after_epoch 3`.

## Inference

```powershell
python inference_sea_vast.py `
  --data ./data/selected_sea_only_real.parquet `
  --prompt-parquet ./.hf_dataset_files/data/train-sea-only.parquet `
  --adapter ./outputs/sea_scheduled_cot/epoch-1 `
  --mode scheduled_cot --batch-size 1 --max-new-tokens 512 `
  --output ./results/sea_scheduled_cot.csv
```
