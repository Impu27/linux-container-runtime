import os
import csv


# Simulated GPU resources
gpus = [
    {"id": 0, "mem_free": 8000},
    {"id": 1, "mem_free": 6000}
]


# Simulated container workload
workload = {
    "container_id": "container-A",
    "gpu_mem": 4000
}

def assign_gpu(gpu):
    os.environ["CUDA_VISIBLE_DEVICES"] = str(gpu["id"])
    print(f"Assigned GPU {gpu['id']} to {workload['container_id']}")
    return gpu["id"]

assigned_gpu = None


# Scheduling Logic
for gpu in gpus:
    if gpu["mem_free"] >= workload["gpu_mem"]:
        assigned_gpu = assign_gpu(gpu)
        gpu["mem_free"] -= workload["gpu_mem"]
        break

if assigned_gpu is None:
    print("No suitable GPU available")

# Save result to CSV
with open("gpu_schedule_log.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["container_id", "gpu_id", "gpu_mem_required"])
    writer.writerow([workload["container_id"], assigned_gpu, workload["gpu_mem"]])
