import csv

def assign_gpu(config):
    gpus = [
        {"id": 0, "mem_free": 8000},
        {"id": 1, "mem_free": 6000}
    ]

    required = config.get("gpu_mem", 2000)
    container_id = config.get("container_id", "container")

    for gpu in gpus:
        if gpu["mem_free"] >= required:
            print(f"[GPU] Assigned GPU {gpu['id']}")

            # Log result
            with open("experiments/gpu_schedule.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([container_id, gpu["id"], required])

            return gpu["id"]

    print("[GPU] No GPU available")
    return -1
