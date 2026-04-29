#Write a Python script that uses a for loop to read a list of log lines
#and count how many lines contain the word "ERROR".
logs = [
    "INFO Server started",
    "ERROR Database failed",
    "WARNING Disk space low",
    "ERROR Timeout occurred"
]
error_count = 0
condition = "ERROR"
for i in logs:
    if condition in i:
        error_count += 1

print("Number of lines containing 'ERROR':", error_count)