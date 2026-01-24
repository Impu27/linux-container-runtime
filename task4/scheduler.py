import csv

THRESHOLD = 60.0

with open("cpu_metrics.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cpu = float(row["cpu_usage_percent"])
        if cpu < THRESHOLD:
            decision = "SCHEDULE"
        else:
            decision = "DELAY"
        print(f"CPU={cpu}% → {decision}")
