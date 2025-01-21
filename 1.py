import requests
import time
import random
import sys
import json
import os
# Parse the input arguments
urls_string = sys.argv[3]  # The repository variable containing the URLs as a string
token = sys.argv[2]        # Authorization token
advertisement = sys.argv[1]  
tracker_file = "ad_tracker.txt"
# Split the URLs string into a list of URLs
urls = [url.strip() for url in urls_string.split(",")]
# Prepare headers and payload
headers = {"Authorization": token}
payload = {"content": advertisement}
# Check the current ad number from the tracker file
if not os.path.exists(tracker_file):
    with open(tracker_file, "w") as file:
        file.write("0")  # Initialize with 0
with open(tracker_file, "r") as file:
    current_ad = int(file.read().strip())
# Post the ad
sleeptime = random.uniform(2, 5)  # Random delay between posts
try:
    for url in urls:
        res = requests.post(url, data=payload, headers=headers)
        if res.status_code == 200:
            print(f"Successfully posted to {url}")
        else:
            print(f"Failed to post to {url}: {res.status_code} - {res.text}")
        time.sleep(sleeptime)
    # Update the tracker file with the next ad number
    with open(tracker_file, "w") as file:
        file.write(str((current_ad + 1) % 12))  # Assuming 12 ads in total (0-11)
except Exception as e:
    print(f"Error posting to URLs: {e}")
