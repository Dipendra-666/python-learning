import shutil

total, used, free = shutil.disk_usage("/")

used_percentage = (used / total) * 100

print(f"Disk Usage: {used_percentage:.2f}%")

if used_percentage > 80:
    print("WARNING: Disk usage is above 80%")
else:
    print("Disk usage is normal")