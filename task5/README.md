# Day 5 — GPU-Aware Scheduling (Safe Simulation)

## Goal
Demonstrate GPU scheduling logic without real GPU hardware.

## Method
- Simulated GPU resources with memory availability
- Simulated container GPU requirements
- Scheduler assigns GPU based on available memory

## Scheduling Logic
If GPU memory is sufficient:
→ Assign GPU and set CUDA_VISIBLE_DEVICES

## Safety Note
GPU logic is simulated inside VM for safety.
No real GPU access is used.

## Output
container_id, gpu_id, gpu_mem_required
