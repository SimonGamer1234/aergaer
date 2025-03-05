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
BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_VARIABLE = os.getenv("FINAL_VARIABLE")
GITHUB_TOKEN = os.getenv("GTOKEN")

author_ids = [1148657062599983237, 841925129323020298, 1285602869638070304, 1303383091468963841]
ids = IDS.split(',')
totalcount = 0
Ads = [AD1, AD2, AD3, AD4, AD5, AD6, AD7, AD8, AD9, AD10, AD11, AD12]
for Ad in Ads:
  for Ad2 in Ads:
    if Ad == Ad2:
      Ads.remove(Ad2)
    
print(Ads)
for Ad in Ads:
  Splitted_Ad = Ad.split("/n=divider/n")
  Text = Splitted_Ad[0]
  words = Ad.split()
  FirstThree = " ".join(words[:2])
  totalcount = 0
  header = {"Authorization": TOKEN3}   
  params = {"content": FirstThree, "author_id":author_ids, "limit": 25}
  for ID in ids:
    response = requests.get(f"https://discord.com/api/v10/channels/{ID}", headers=header)
    if response.status_code == 200:
      try:
        data = response.json()
        print(data)
        server_id = data['guild_id']
        intID = int(server_id)
        link = f"https://discord.com/api/v9/guilds/{intID}/messages/search"
        print(link)
        time.sleep(random.uniform(5,7))
        res = requests.get(link, params=params, headers=header)
        if res.status_code == 200:
          try:
            data = res.json()
            total_results = data.get("total_results", 0)
            totalcount += int(total_results)
            print(total_results)  # Parsed JSON response
          except requests.exceptions.JSONDecodeError:
            print("Response is not JSON. Raw response:")
            print(res.text)
        else:
          print(f"Request failed with status code {res.status_code}: {res.text}")
      except requests.exceptions.JSONDecodeError:
        print("Response is not JSON. Raw response:")
        print(res.text)
      
    else:
      print(f"Request failed with status code {response.status_code}: {response.text}")

  botheader = {"Authorization": f"Bot {BOT_TOKEN}"}
  CONTENT = f"Avertisement\n{Text}\n\n{totalcount}"
  payload = {"content": CONTENT}
  LINK = "https://discord.com/api/v9/channels/1302654558023057540/messages"
  post = requests.post(LINK, data=payload, headers=botheader)
  print(post.text)
def TimeReduce():
  for Ad in Ads:
    Splitted_ad = Ad.split("\n=divider=\n")
    Ad_Text = Splitted_ad[0]
    Ad_TotalPosts = Splitted_ad[1]
    Ad_RemainingTime = Splitted_ad[2]
    NewTime = Ad_RemainingTime - 1
    
 
