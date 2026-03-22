import yaml
import os
import sys

def run_workload(config):
    print("\n=== Container Runtime Simulation ===")

    cpu = config.get("cpu")
    memory = config.get("memory")
    gpu = config.get("gpu")
    command = config.get("command")

    print(f"CPU: {cpu} cores")
    print(f"Memory: {memory}")
    print(f"GPU required: {gpu}")
    print(f"Command: {command}")

    # Simulate CPU affinity
    if cpu:
        print(f"[SIMULATION] Would assign {cpu} CPU cores")

    # Simulate memory limit
    if memory:
        print(f"[SIMULATION] Would limit memory to {memory}")

    # Simulate GPU scheduling
    if gpu:
        os.environ["CUDA_VISIBLE_DEVICES"] = "0"
        print("[SIMULATION] Assigned GPU 0")

    # Execute workload
    print("\n[RUNNING COMMAND]")
    os.system(command)


def main():
    if len(sys.argv) < 3:
        print("Usage: containerctl run <config.yaml>")
        sys.exit(1)

    action = sys.argv[1]
    file = sys.argv[2]

    if action != "run":
        print("Only 'run' supported")
        sys.exit(1)

    with open(file) as f:
        config = yaml.safe_load(f)

    run_workload(config)


if __name__ == "__main__":
    main()
