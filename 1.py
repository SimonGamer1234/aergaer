import requests
import time
import random
import sys
import json

# Parse the list of URLs passed as a command-line argument
urls = [ sys.argv[3] ]

token = sys.argv[2]
Advertisement = sys.argv[1]

# Prepare headers and payload
headers = {"Authorization": token}
payload = {"content": Advertisement}

# Post the ad to each URL
for url in urls:
    sleeptime = random.uniform(2, 5)  # Random delay between posts
    try:
        res = requests.post(url, data=payload, headers=headers)
        if res.status_code == 200:
            print(f"Successfully posted to {url}")
        else:
            print(f"Failed to post to {url}: {res.status_code} - {res.text}")
    except Exception as e:
        print(f"Error posting to {url}: {e}")
    time.sleep(sleeptime)
