import time
import csv

def read_cpu_times():
    with open("/proc/stat", "r") as f:
        line = f.readline()
    parts = line.split()
    values = list(map(int, parts[1:]))
    idle = values[3]
    total = sum(values)
    return idle, total

def cpu_usage(prev, curr):
    idle_diff = curr[0] - prev[0]
    total_diff = curr[1] - prev[1]
    return 100 * (1 - idle_diff / total_diff)

with open("cpu_metrics.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "cpu_usage_percent"])

    prev = read_cpu_times()
    time.sleep(1)

    for _ in range(20):
        curr = read_cpu_times()
        usage = cpu_usage(prev, curr)
        writer.writerow([time.time(), round(usage, 2)])
        prev = curr
        time.sleep(1)
