import subprocess
print("Starting isolated namespace shell...")
subprocess.run(["unshare", "--pid", "--fork", "--mount", "bash"])
