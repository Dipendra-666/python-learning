import psutil

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent

print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory}%")

if cpu > 80:
    print("High CPU Usage Alert")

if memory > 80:
    print("High Memory Usage Alert")