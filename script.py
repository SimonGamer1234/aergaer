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
BOT_TOKEN = f"Bot {os.getenv("BOT_TOKEN")}"
OWNER = "SimonGamer1234"
REPO = "aergaer"
GITHUB_TOKEN = os.getenv("GTOKEN")

author_ids = [1148657062599983237, 841925129323020298, 1285602869638070304, 1303383091468963841]
ids = IDS.split(',')
totalcount = 0
Ads = [AD1, AD2, AD3, AD4, AD5, AD6, AD7, AD8, AD9, AD10, AD11, AD12]
print(Ads)

def GetGuildIds(ids):
    GuildIds = []
    for ID in ids:
      header = {"Authorization": TOKEN3}
      response = requests.get(f"https://discord.com/api/v10/channels/{ID}", headers=header)
      if response.status_code == 200:
        data = response.json()
        guildId = int(data["guild_id"])
        GuildIds.append(guildId)
      else:
        print(f"Error with AdvertisingChannel Id: {ID} {response.status_code}")
    return GuildIds

def SearchForPosts(Keyword, ids, author_ids):
  print(ids)
  totalcount = 0
  header = {"Authorization": TOKEN3}
  params = {"content": Keyword, "author_id": author_ids, "limit": 25}
  for ID in ids:
    ID = int(ID)
    link = f"https://discord.com/api/v9/guilds/{ID}/messages/search"
    print(link)
    time.sleep(random.uniform(5,10))
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
  print(f"Total count: {totalcount} Ad: {Keyword}")
  return totalcount

def SplitAd(Ad):
  Splitted1 = Ad.split("\n=divider=\n")
  Splitted2 = Ad.split("\r\n=divider=\r\n")
  if len(Splitted1) == 4:
    print(Splitted1)
    AdContent = Splitted1[0]
    TotalPosts = Splitted1[1]
    DaysLeft = Splitted1[2]
    KeyWords = Splitted1[3]
    return KeyWords, DaysLeft, TotalPosts, AdContent
  elif len(Splitted2) == 4:
    print(Splitted2)
    AdContent = Splitted2[0]
    TotalPosts = Splitted2[1]
    DaysLeft = Splitted2[2]
    KeyWords = Splitted2[3]
    return KeyWords, DaysLeft, TotalPosts, AdContent
  else:
     print("Error wiht splitting")
     print(Ad)

def UpdateVariable(KeyWords, DaysLeft, TotalPosts, AdContent, Ad):
  if TotalPosts == "Base_Variable":
      print("Base Variable")
      return "Base_Variable", "Base_Variable", "Base_Variable", "Base_Variable"
  else:   
    NewDays = int(DaysLeft) - 1
    if NewDays == 0:
      SendMessage(f"Ad {AdContent} has expired", BOT_TOKEN, "https://discord.com/api/v9/channels/1302654558023057540/messages")
    NAME = f"AD_{Ads.index(Ad) + 1}"
    Text = f"{AdContent}\n=divider=\n{TotalPosts}\n=divider=\n{NewDays}\n=divider=\n{KeyWords}"
    headers = {
      'Accept': 'application/vnd.github+json',
      'Authorization': f'Bearer {GITHUB_TOKEN}',
      'X-GitHub-Api-Version': '2022-11-28',
      'Content-Type': 'application/json',}
    data = {"value": Text}
    response = requests.patch(f'https://api.github.com/repos/{OWNER}/{REPO}/actions/variables/{NAME}', headers=headers, json=data)
    print(response.status_code)


def SendMessage(Message, Account, ChannelID):
  header = {"Authorization": Account}
  payload = {"content": Message}
  link = f"https://discord.com/api/v9/channels/{ChannelID}/messages"
  res = requests.post(link, data=payload, headers=header)
  print(f"Posted to {link} : {res.status_code}")  # Print response status

def DeleteIfMultiple():
  Ads2 = Ads
  for Ad in Ads:
    KeyWords, DaysLeft, TotalPosts, AdContent = SplitAd(Ad)
    for Ad1 in Ads:
      KeyWords1, DaysLeft1, TotalPosts1, AdContent1 = SplitAd(Ad1)
      if KeyWords == KeyWords1:
         Ads2.remove(Ad1)
  print(Ads2)
  return Ads2

def main(Ads2):
   for Ad in Ads2:
      KeyWords, DaysLeft, TotalPosts, AdContent  = SplitAd(Ad)
      if KeyWords == "Base_Variable":
        print("Base Variable")
        continue
      else:
        totalcount = SearchForPosts(KeyWords, GetGuildIds(ids), author_ids)
        PostsLeft = int(TotalPosts) - totalcount
        for Ad1 in Ads:
          KeyWords1, DaysLeft1, TotalPosts1, AdContent1  = SplitAd(Ad1)
          if KeyWords == KeyWords1:
            UpdateVariable(KeyWords1, DaysLeft1, TotalPosts1, AdContent1, Ad1)
          else:
            continue
        if PostsLeft > 0:
          Message = f"Advertisement:\n\n{Ad1}\n\n Days Left:\n{DaysLeft1}\n Total Posts: \n{TotalPosts}\n Posts left: {PostsLeft}"
          SendMessage(Message, BOT_TOKEN, 1300080137097711677)
        else:
          Message = f"Advertisement:\n\n{Ad1}\n\n Can be DELETED"
          SendMessage(Message, BOT_TOKEN, 1300080137097711677)
          

          
main(DeleteIfMultiple())      
           
