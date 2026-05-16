import subprocess

container_name = "nginx"

command = "docker ps --format '{{.Names}}'"

result = subprocess.run(
    command,
    shell=True,
    capture_output=True,
    text=True
)

running_containers = result.stdout.splitlines()

if container_name in running_containers:
    print(f"Container '{container_name}' is RUNNING")
else:
    print(f"Container '{container_name}' is NOT running")