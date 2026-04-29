# Write a Python program using a while loop that simulates retrying a deployment until it succeeds or reaches 5 attempts.

# 👉 Conditions:

# Print "Attempt X failed" for first 4 tries
# On 5th attempt, print "Deployment successful" and stop

attempt = 1
max_attempts = 5
while attempt <= max_attempts:
    if attempt < max_attempts:
        print(f"Attempt {attempt} failed")
    else:
        print("Deployment successful")
        break
    attempt += 1