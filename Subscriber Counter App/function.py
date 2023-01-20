
import requests
import json
import time 

# api key , channel id of youtube channel we are trying to get data of , and the endpoint to hit
key = "AIzaSyAioHF3G-HzJVclWm7vhePMFGaqkB1xFK4"
channel_id = "UCL7pUfWNL7NvR2yxwgfw1-w" 
endpoint =  "https://www.googleapis.com/youtube/v3/channels"

params={
    "key" : key,
    "part" : "statistics",
    "id" : channel_id
}

response = requests.get(endpoint,params=params) 

# convert json response into a dictionary 
dict= json.loads(response.content)

# navigating through the dictionary to get subscriber Count 
sub_count = dict['items'][0]['statistics']['subscriberCount']


def printSubCount():
    while True:
        print(f"Sanjay Silwal Gupta Subscribers: {sub_count}") 
        time.sleep(3)

