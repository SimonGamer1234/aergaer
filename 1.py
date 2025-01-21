import os
import random
import requests

# Retrieve the environment variables
repo_var_one = os.getenv("REPO_VAR_ONE")
repo_var_two = os.getenv("REPO_VAR_TWO")
secret_var = os.getenv("SECRET_VAR")

# Print them or use them in your script
print(f"Repo Variable One: {repo_var_one}")
print(f"Repo Variable Two: {repo_var_two}")
print(f"Secret Variable: {secret_var}")

header = {"Authorization": secret_var}
payload = {"content": repo_var_one}

for link in repo_var_two:
    sleeptime = random.uniform(2,3)
    res = requests.post(link, data=payload, headers=header)
    print(f"Posted to {link}: {res.status_code}")  # Print response status
    print(f"waiting {sleeptime}")
    time.sleep(sleeptime)  # Wait 5 seconds before the next request
