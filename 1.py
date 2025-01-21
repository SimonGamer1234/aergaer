import os
import random
import requests
import time
import json

# Retrieve the environment variables
repo_var_one = os.getenv("REPO_VAR_ONE")
repo_var_two = os.getenv("REPO_VAR_TWO")
secret_var = os.getenv("SECRET_VAR")

# Parse repo_var_two as JSON
try:
    repo_var_two = json.loads(repo_var_two)
except json.JSONDecodeError:
    print("Error: REPO_VAR_TWO is not valid JSON.")
    exit(1)

# Print them or use them in your script
print(f"Repo Variable One: {repo_var_one}")
print(f"Repo Variable Two: {repo_var_two}")
print(f"Secret Variable: {secret_var}")

header = {"Authorization": secret_var}
payload = {"content": repo_var_one}

# Loop through the links and make POST requests
for link in repo_var_two:
    sleeptime = random.uniform(2, 3)
    try:
        res = requests.post(link, data=payload, headers=header)
        print(f"Posted to {link}: {res.status_code}")  # Print response status
    except requests.RequestException as e:
        print(f"Error posting to {link}: {e}")
    print(f"Waiting {sleeptime} seconds...")
    time.sleep(sleeptime)
