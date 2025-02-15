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
IDS = os.getenv("URLS")
TOKEN3 = os.getenv("TOKEN_SCRT_3")

author_ids = [1148657062599983237, 841925129323020298, 1285602869638070304, 1303383091468963841]
ids = IDS.split(',')
Ads = [AD1, AD2, AD3, AD4, AD5, AD6, AD7, AD8, AD9, AD10, AD11, AD12]
for Ad in Ads:
  for Ad2 in Ads:
    if Ad == Ad2:
      Ads.remove(Ad2)
    
print(Ads)
for Ad in Ads:
  header = {"Authorization": TOKEN3}   
  params = {"content": Ad, "author_id":author_ids, "limit": 100}
  for ID in ids:
    intID = int(ID)
    link = f"https://discord.com/api/v9/guilds/{intID}/messages/search"
    print(link)
    time.sleep(random.uniform(2,3))
    res = requests.get(link, params=params, headers=header)
    if res.status_code == 200:
        try:
            data = res.json()
            total_results = data.get("total_results", 0)
            totalcount += int(total_results)
            print(total_results)  # Parsed JSON response
            print(totalcount)
        except requests.exceptions.JSONDecodeError:
            print("Response is not JSON. Raw response:")
            print(res.text)
    else:
        print(f"Request failed with status code {res.status_code}: {res.text}")
