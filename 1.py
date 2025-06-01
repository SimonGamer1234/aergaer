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
TOKEN1 = os.getenv("TOKEN_SCRT_1")
TOKEN2 = os.getenv("TOKEN_SCRT_2")
TOKEN3 = os.getenv("TOKEN_SCRT_3")
TOKEN4 = os.getenv("TOKEN_SCRT_4")
BOT_TOKEN = os.getenv("BOT_TOKEN")

ids = IDS.split(',')
ids = [1300080161827586148] # Example channel ID, replace with actual IDs
Errors = []
Ads = [AD1, AD2, AD3, AD4, AD5, AD6, AD7, AD8, AD9, AD10, AD11, AD12]
Tokens = [TOKEN1, TOKEN2, TOKEN3, TOKEN4]
tracker_file = "ad_tracker.txt"

if not os.path.exists(tracker_file):
    with open(tracker_file, "w") as file:
        file.write("0")  # Initialize with 0
with open(tracker_file, "r") as file:
    current_ad = int(file.read().strip())

token_index = current_ad % 4  # Use a descriptive variable name
print(current_ad)
print(token_index)
Token = Tokens[token_index]
CurrentAd = Ads[current_ad]

def ContentSetter(CurrentAd):
    SPLIT_AD = CurrentAd.split("\n=divider=\n")
    SPLIT_AD2 = CurrentAd.split("\r\n=divider=\r\n")
    if len(SPLIT_AD) > 1:
        return SPLIT_AD[0], SPLIT_AD[1], SPLIT_AD[2], SPLIT_AD[3], SPLIT_AD[4]
    elif len(SPLIT_AD2) > 1:
        return SPLIT_AD2[0], SPLIT_AD2[1], SPLIT_AD2[2], SPLIT_AD2[3], SPLIT_AD2[4]
    else:
        print("Error: No divider found in ad")
        exit(1)

def SendMessageFromAccount(Token, ChannelID, Content):
    header = {"Authorization": Token}
    payload = {"content": Content}
    link = f"https://discord.com/api/v9/channels/{ChannelID}/messages"
    try:
        res = requests.post(link, data=payload, headers=header)
        print(f"Posted to {link} : {res.status_code}")  # Print response status
        print(res.text)
        if res.status_code != 200:
            Errors.append((link, res.status_code, token_index, "Normal"))
        return res.status_code
    except requests.RequestException as e:
        print(f"Error posting to {link}: {e}")
        return None

def SendMessageFromBot(BotToken, ChannelID, Content):
    header = {"Authorization": f"Bot {BotToken}"}
    payload = {"content": Content}  
    link = f"https://discord.com/api/v9/channels/{ChannelID}/messages"
    try:
        res = requests.post(link, json=payload, headers=header)
        print(f"Posted to {link} : {res.status_code}")  # Print response status
        if res.status_code != 200:
            Errors.append((link, res.status_code, token_index, "Bot"))
        return res.status_code
    except requests.RequestException as e:
        print(f"Error posting to {link}: {e}")
        return None
    

def Posting(Ids, Content):
    unauthorized = 0
    for ID in Ids:
        sleeptime = random.uniform(2, 3)
        time.sleep(sleeptime)  # Sleep for a random time between 2 and 3 seconds
        status_code = SendMessageFromAccount(Token, ID, Content)
        if status_code == 401:
            unauthorized = 1
            break  # Stop if unauthorized
    return unauthorized

def ReportMainChannel(unauthorized, Content, token_index):
    if unauthorized == 1:
        ReportContent = f"TOKEN {token_index} UNAUTHORIZED - Normal - <@1148657062599983237>\n\nContent: {Content}"
    else:
        ReportContent = f" {str(Errors)}\n\nContent: {Content}"
    MessageStatus = SendMessageFromBot(BOT_TOKEN, "1300080115945836696", ReportContent)
    return MessageStatus
    

def ReportTicket(TicketID, unauthorized):
    if unauthorized == 1:
        ReportContent = f"There was a porblem with the ad posting. The Owner has been notified. He will provide more info <@1148657062599983237>"
    else:
        ReportContent = f"We have posted your ad. The posting was successful."
    MessageStatus = SendMessageFromBot(BOT_TOKEN, TicketID, ReportContent)
    return MessageStatus
    

def main():
    CONTENT,totalposts, daysleft, Keywords, TICKETID  = ContentSetter(CurrentAd)
    unauthorized = Posting(ids, CONTENT)
    MainChannelMessageStatus = ReportMainChannel(unauthorized, CONTENT, token_index)
    TicketMessageStatus = ReportTicket(TICKETID, unauthorized)
    print(f"Main Channel Message Status: {MainChannelMessageStatus}")
    print(f"Ticket Message Status: {TicketMessageStatus}")

main()