import os
import random
import requests
import time
import json

# Retrieve the environment variables
repo_var_one = os.getenv("REPO_VAR_ONE")
repo_var_two = os.getenv("REPO_VAR_TWO")
secret_var = os.getenv("SECRET_VAR")

urls = repo_war_two.split(',')

# Print them or use them in your script
print(f"Repo Variable One: {repo_var_one}")
print(f"Repo Variable Two: {repo_var_two}")
print(f"Secret Variable: {secret_var}")

header = {"Authorization": secret_var}
payload = {"content": repo_var_one}

# Loop through the links and make POST requests
for link in urls:
    sleeptime = random.uniform(2, 3)
    try:
        res = requests.post(link, data=payload, headers=header)
        print(f"Posted to {link}: {res.status_code}")  # Print response status
    except requests.RequestException as e:
        print(f"Error posting to {link}: {e}")
    print(f"Waiting {sleeptime} seconds...")
    time.sleep(sleeptime)
