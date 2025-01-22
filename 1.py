import os
import random
import requests
import time
import json

# Retrieve the environment variables
AD1 = os.getenv("REPO_VAR_1")
AD2 = os.getenv("REPO_VAR_2")
AD3 = os.getenv("REPO_VAR_3")
AD4 = os.getenv("REPO_VAR_4")
AD5 = os.getenv("REPO_VAR_5")
AD6 = os.getenv("REPO_VAR_6")
AD7 = os.getenv("REPO_VAR_7")
AD8 = os.getenv("REPO_VAR_8")
AD9 = os.getenv("REPO_VAR_9")
AD10 = os.getenv("REPO_VAR_10")
AD11 = os.getenv("REPO_VAR_11")
AD12 = os.getenv("REPO_VAR_12")
URLS = os.getenv("URLS")
TOKEN1 = os.getenv("ACCOUNT_1_TOKEN")
TOKEN2 = os.getenv("ACCOUNT_2_TOKEN")
TOKEN3 = os.getenv("ACCOUNT_3_TOKEN")
TOKEN4 = os.getenv("ACCOUNT_4_TOKEN")

urls = URLS.split(',')

Ads = [AD1, AD2, AD3, AD4, AD5, AD6, AD7, AD8, AD9, AD10, AD11, AD12]
Tokens = [TOKEN1, TOKEN2, TOKEN3, TOKEN4]
tracker_file = "ad_tracker.txt"

if not os.path.exists(tracker_file):
    with open(tracker_file, "w") as file:
        file.write("0")  # Initialize with 0
with open(tracker_file, "r") as file:
    current_ad = int(file.read().strip())

Token = Tokens[current_ad%4]
print = current_ad%4
CurrentAd = Ads[current_ad]

# Print them or use them in your script
print(f"Repo Variable Two: {repo_var_two}")
print(f"Secret Variable: {secret_var}")

header = {"Authorization": secret_var}
payload = {"content": CurrentAd}

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
