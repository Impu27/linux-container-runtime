import os
import time
import csv
import sys

pid = os.getpid()

core = int(sys.argv[1])
CORE_SET = {core}

os.sched_setaffinity(pid, CORE_SET)

print(f"[Container] PID {pid} pinned to CPU core(s): {CORE_SET}")

start = time.time()
while time.time() - start < 120:
	pass

with open("cpu_affinity_log.csv", "a", newline="") as f:
	writer = csv.writer(f)
	writer.writerow([pid, list(CORE_SET), "busy"])
