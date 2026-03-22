import csv
import matplotlib.pyplot as plt

timestamps = []
cpu = []

with open("cpu_metrics.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        timestamps.append(float(row["timestamp"]))
        cpu.append(float(row["cpu_usage_percent"]))

plt.plot(cpu)
plt.axhline(60, color='red', linestyle='--', label='Scheduling Threshold')
plt.xlabel("Time (seconds)")
plt.ylabel("CPU Usage (%)")
plt.title("CPU Usage vs Time")
plt.legend()
plt.savefig("cpu_usage.png")
plt.show()
