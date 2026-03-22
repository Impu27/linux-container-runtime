import os
import csv

def set_cpu_affinity(cpu_cores):
    pid = os.getpid()
    cores = set(range(cpu_cores))

    os.sched_setaffinity(pid, cores)
    print(f"[Affinity] PID {pid} pinned to cores {cores}")

    # Log to file
    with open("experiments/cpu_affinity.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([pid, list(cores)])
