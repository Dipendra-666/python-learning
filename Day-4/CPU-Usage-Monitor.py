# Write a Python script using a while loop that keeps running until CPU usage drops below 50%.

# 👉 Example:

# Start with cpu_usage = 90
# Decrease CPU usage by 10 in each loop
# Print current usage each time
current_cpu_usage = 90
while current_cpu_usage >= 50:
    print(f"current cpu usage is:{current_cpu_usage}%")
    current_cpu_usage -= 10
print("CPU usage is now below 50%")