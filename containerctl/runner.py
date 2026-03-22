import os
from runtime.affinity import set_cpu_affinity
from runtime.gpu_scheduler import assign_gpu

def run_container(config):
    cpu = config.get("cpu")
    memory = config.get("memory")
    gpu = config.get("gpu")
    command = config.get("command")

    print("\n=== Running Container ===")
    print(f"CPU: {cpu}, Memory: {memory}, GPU: {gpu}")

    # CPU affinity
    if cpu:
        set_cpu_affinity(cpu)

    # GPU assignment
    if gpu:
        gpu_id = assign_gpu(config)
        os.environ["CUDA_VISIBLE_DEVICES"] = str(gpu_id)
        print(f"Assigned GPU: {gpu_id}")

    print(f"\nExecuting: {command}")
    os.system(command)
