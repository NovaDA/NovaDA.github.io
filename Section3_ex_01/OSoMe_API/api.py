import requests
from social_media_data import SocialMediaData

# TweetsCounts - result url - job ID
# Tweeds ID - file [] - job ID
# TimeSeries - result url - job ID

#-------------------------#
# url
# start - end date
# # hashtags

def RetriveData(endpoints, hashtags, startdate, enddate):

 
    url = f"https://osome-public.p.rapidapi.com/{endpoints}"

    querystring = {"start":f"{startdate}","end":f"{enddate}","q":f"{hashtags}"}

    headers = {
	"X-RapidAPI-Key": "2de025c91fmsh1fddbc9b4b37c96p110dc9jsn420dbcfa5637",
	"X-RapidAPI-Host": "osome-public.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return SocialMediaData(response.json())

    