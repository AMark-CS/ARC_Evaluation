# Qwen2.5 Evaluation Coursework

## Project overview

This repository contains coursework materials for evaluating language-model quality and inference efficiency. The experiments use the [EleutherAI LM Evaluation Harness](arc/README.md) and record results for Qwen2.5 model variants.

The saved runs compare short and long prompts and include 0.5B and 7B models, with quantized variants such as AWQ, GPTQ 4-bit and 8-bit, and GGUF where available. The benchmark result files cover ARC-Challenge, HellaSwag, and PIQA. The result tree also contains memory and throughput measurements.

## Repository layout

- `arc/` — LM Evaluation Harness source used by the experiments.
- `result/Primary_Run/` — primary experiment outputs, grouped by prompt length, model, and execution mode.
- `result/Additional_Run/` — supplementary experiment outputs.
- `result/Standalone_Evaluations/` — standalone benchmark result exports, including a 4-bit result file.
- `dataset/` — `input_upper.npy` and `workbook_1.xlsx`. Their provenance and exact relationship to the language-model experiments are not documented in the files currently present.

## Reading the results

The JSON files named `results.json` contain benchmark scores such as `acc` and `acc_norm`, with standard-error fields where available. `memory_results.json` and `throughput_results.json` record resource and speed measurements. The workbook in `result/Primary_Run/` is also part of the archived experiment outputs.

These are preserved run artifacts. The repository does not include enough run-specific configuration to guarantee an exact reproduction of every result, such as the original model locations and full runtime environment. Consult `arc/README.md` for the evaluation harness documentation.
