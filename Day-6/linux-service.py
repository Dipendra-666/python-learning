import subprocess

service_name = "nginx"

command = f"systemctl is-active {service_name}"

result = subprocess.run(command, shell=True, capture_output=True, text=True)

status = result.stdout.strip()

if status == "active":
    print(f"{service_name} is running")
else:
    print(f"{service_name} is NOT running")