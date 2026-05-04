error_count = 0
warning_count = 0
logs = [
    "INFO Server started",
    "ERROR Database failed",
    "WARNING Disk space low",
    "ERROR Timeout occurred",
    "INFO User logged in",
    "WARNING High memory usage"
]

for line in logs:
    
    # Convert to lowercase for safe matching
    lower_line = line.lower()
    
    # Check for ERROR
    if "error" in lower_line:
        error_count += 1
        print("ERROR FOUND:", line)
    
    # Check for WARNING
    if "warning" in lower_line:
        warning_count += 1

print("\nSummary:")
print("Total ERROR logs:", error_count)
print("Total WARNING logs:", warning_count)