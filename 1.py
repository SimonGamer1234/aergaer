import requests
import time
import random
import sys
import json

# Parse the input arguments
urls_string = sys.argv[3]  # The repository variable containing the URLs as a string
token = sys.argv[2]        # Authorization token
advertisement = sys.argv[1]  # The advertisement content

# Split the URLs string into a list of URLs
urls = [url.strip() for url in urls_string.split(",")]

# Prepare headers and payload
headers = {"Authorization": token}
payload = {"content": advertisement}

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