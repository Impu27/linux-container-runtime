# Task 3 — Multi-Core CPU Scheduling (CPU Affinity)

## Goal
Demonstrate core-aware scheduling by pinning container-like processes
to specific CPU cores.

## Method
Used Linux scheduler affinity via Python os.sched_setaffinity().

## Experiment
- Container A pinned to core 0
- Container B pinned to core 1
- Verified via htop and taskset

## Output
CPU affinity logged in CSV format:
container_id, core, cpu_usage

## Result
Successfully demonstrated Linux multi-core scheduling and strict CPU affinity,
similar to CPU pinning used in container runtimes and Kubernetes.
