import requests
import time
import random
import sys
import json

# Ensure the correct number of arguments are passed
if len(sys.argv) != 4:
    print("Usage: python3 script.py <Advertisement> <Token> <URLs_JSON>")
    sys.exit(1)

# Get inputs from command-line arguments
Advertisement = sys.argv[1]
token = sys.argv[2]

# Parse the URLs passed as a JSON string
try:
    urls = json.loads(sys.argv[3])
    if not isinstance(urls, list):
        raise ValueError("URLs must be a list.")
except Exception as e:
    print(f"Error parsing URLs: {e}")
    sys.exit(1)

# Prepare headers and payload
headers = {"Authorization": token}
payload = {"content": Advertisement}

# Post the ad to each URL
for url in urls:
    sleeptime = random.uniform(2, 5)  # Random delay between posts
    try:
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:
            print(f"Successfully posted to {url}")
        else:
            print(f"Failed to post to {url}: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error posting to {url}: {e}")
    time.sleep(sleeptime)
