import datetime
import random
import requests
import pprint
from api import RetriveData
from social_media_data import SocialMediaData


#counts 
#tweet-id
#time-series
user_input = []  # endpoint
hash_tags_input = [] # hastag
start_date_input = [] 
end_date_input = []


def HashTag():
    hash_tags_input = input("enter hashtags followed by comma : EX: #yolo,  \n").lower()
        
    verify_hash_tags = hash_tags_input.split(",")
    verify_hash_tags = ' '.join(verify_hash_tags).split()
    new_tags = []
    for tag in verify_hash_tags:
        if tag[0] != '#':
            new_tag = '#' + tag
            new_tags.append(new_tag)
        else:
            new_tags.append(tag)

    hash_tags_input = ",".join(new_tags) 
    print(hash_tags_input)
    return hash_tags_input

def date():
    
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2020, 2, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    
    return random_date

    

def printStatistics():
    result_count = statistics.result_url

    respo = requests.request("GET", result_count)
    data = respo.text
    count_list = data.splitlines()
    print(result_count)

    # 1
    # method to split hash tags in key pair // used for the tweets and time-series
    table = dict(h.split('\t') for h in count_list )
    pprint.pprint(table)

def printfile():
    for texts in statistics.files:
        respo = requests.get(texts)
        data = respo.text
        length = data.count('\n')
        print(data)
        print(f'N/month and tweets are {length}') 



while True:
    user_input = input(f"< SELECT : [COUNTS] [TWEET-ID] [TIME-SERIES] [EXIT]\n ").lower()

    if user_input == 'counts':    
        #date()
        hash = HashTag()
        statistics = RetriveData("counts", hash, "2020-01-01T00:00:00", "2020-01-01T23:59:59")
        printStatistics()
    elif user_input == 'tweet-id':
       # date()
        hash = HashTag()
        statistics = RetriveData("tweet-id", hash,  "2020-01-01T00:00:00", "2020-01-01T23:59:59")
        printfile()
    elif user_input == 'time-series':
        #date()
        hash = HashTag()
        statistics = RetriveData("time-series", hash,  "2020-01-01T00:00:00", "2020-01-01T23:59:59")
        printStatistics()
    elif user_input == "exit":
        break
    else:
        print("WRONG COMMAND TRY AGAIN !!!!")



