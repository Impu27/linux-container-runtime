#  Lightweight Container Runtime (Linux Internals Project)

##  Overview

This project demonstrates the internal working of container runtimes by implementing core Linux concepts such as namespaces, cgroups, CPU scheduling, and resource management from scratch inside a Virtual Machine.

It evolves into a modular system with a CLI interface, runtime engine, scheduling logic, and CI/CD automation — closely resembling real-world container systems like Docker and containerd.

---

##  Key Features

*  Process isolation using Linux namespaces
*  Resource control via cgroups v2
*  CPU core scheduling with affinity
*  Metrics-driven scheduling using `/proc/stat`
*  GPU-aware scheduling (safe simulation)
*  CLI tool for container execution
*  CI/CD pipeline with GitHub Actions
*  Structured logs and experiment tracking

---

## Architecture

```
containerctl (CLI)
        ↓
parser (YAML config)
        ↓
runner (execution engine)
        ↓
runtime/
 ├── affinity.py        → CPU core pinning
 ├── scheduler.py       → scheduling logic
 ├── metrics.py         → system metrics
 └── gpu_scheduler.py   → GPU allocation (simulated)
```

---

##  Project Structure

```
linux-container-runtime/
├── containerctl/        # CLI + orchestration layer
│   ├── main.py
│   ├── parser.py
│   └── runner.py
│
├── runtime/             # core system logic
│   ├── affinity.py
│   ├── scheduler.py
│   ├── metrics.py
│   └── gpu_scheduler.py
│
├── experiments/         # logs & outputs
│   ├── cpu_affinity.csv
│   ├── cpu_metrics.csv
│   ├── gpu_schedule.csv
│   └── graphs/
│       └── cpu_usage.png
│
├── examples/            # workload configs
│   └── basic.yaml
│
├── tests/               # unit tests
│   └── test_basic.py
│
├── docs/                # logs and notes
│   ├── namespaces_log.txt
│   └── cgroups_log.txt
│
├── .github/workflows/   # CI/CD pipeline
│   └── ci.yml
│
├── requirements.txt
└── README.md
```

---

##  CLI Usage

Run a container workload:

```bash
python3 -m containerctl.main run examples/basic.yaml
```

---

##  Example Workload

```yaml
cpu: 2
memory: 512M
gpu: true
command: stress --cpu 2
```

---

##  Experiments

The project includes real execution data:

* CPU affinity logs → `experiments/cpu_affinity.csv`
* CPU usage metrics → `experiments/cpu_metrics.csv`
* GPU scheduling logs → `experiments/gpu_schedule.csv`
* Graphs → `experiments/graphs/cpu_usage.png`

---

##  Safety Model

* All operations executed inside a VirtualBox VM
* No kernel modifications
* No impact on host OS
* GPU scheduling is simulated
* Safe and reproducible environment

---

##  Implementation Breakdown

### Task 1 — Namespace Isolation

* Used `unshare` for PID isolation
* Verified process separation

### Task 2 — Resource Control

* Applied CPU limits using cgroups v2
* Attached processes to control groups

### Task 3 — CPU Scheduling

* Implemented CPU affinity using `sched_setaffinity`
* Verified using `htop`

### Task 4 — Metrics & Scheduling

* Read `/proc/stat`
* Implemented load-based scheduling
* Generated CPU usage graphs

### Task 5 — GPU Scheduling (Simulation)

* Simulated GPU resources
* Assigned GPUs based on memory availability

### Task 6 — CI/CD Pipeline

* Implemented GitHub Actions workflow
* Automated test execution

### Task 7 — CLI Integration

* Built modular CLI tool (`containerctl`)
* YAML-based workload execution

---

##  Limitations

* No real container filesystem isolation
* GPU scheduling is simulated (no CUDA execution)
* Limited networking features
* Not a production-ready runtime

---

##  Key Learnings

* Deep understanding of Linux kernel primitives
* Practical implementation of container internals
* Resource scheduling and system-level programming
* DevOps practices with CI/CD pipelines

---

##  Resume Highlight

> Built a modular container runtime using Linux namespaces, cgroups, CPU affinity, and data-driven scheduling with simulated GPU allocation and CI/CD automation.

---

##  Future Improvements

* Add filesystem isolation (chroot / overlayfs)
* Implement network namespaces
* Support multiple containers
* Extend scheduler with advanced policies

---

##  Conclusion

This project demonstrates how container runtimes work internally by combining Linux system programming with modern software architecture and DevOps practices.

---
