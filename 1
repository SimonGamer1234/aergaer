import requests
import time
import random
import sys
import os


# API URLs to post to
urls = ["https://discord.com/api/v9/channels/1302654530474737770/messages",
"https://discord.com/api/v9/channels/1302654558023057540/messages",
"https://discord.com/api/v9/channels/1302654581758496809/messages",]
# Parse arguments
if len(sys.argv) != 3:
    print("Usage: python3 Scheduler.py <ad_index> <token>")
    sys.exit(1)


token = sys.argv[2]

# Validate ad index
if ad_index < 1 or ad_index > 12:
    print("Invalid ad index. Must be between 1 and 12.")
    sys.exit(1)

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
