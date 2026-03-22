# Lightweight Container Runtime

## Overview
This project demonstrates core container runtime concepts implemented from scratch
inside a Linux VM, including isolation, scheduling, resource control, and automation.

---

## Architecture

- Namespaces → Process isolation
- cgroups v2 → CPU & memory limits
- CPU affinity → Core-aware scheduling
- Metrics → Data-driven scheduling
- GPU scheduler → Simulated GPU allocation
- CI/CD → Automated testing pipeline
- CLI tool → Unified container execution interface

---

## Safety Model

- All operations performed inside a VirtualBox VM
- No kernel modifications
- No privileged host access
- GPU scheduling is simulated
- Safe, reproducible environment

---

## Experiments

- Process isolation using `unshare`
- CPU throttling using cgroups
- Core pinning verified via `htop`
- Metrics collected from `/proc/stat`
- GPU scheduling using simulated resources
- Automated CI testing via GitHub Actions

---

## CLI Usage

```bash
python3 containerctl.py run workload.yaml
