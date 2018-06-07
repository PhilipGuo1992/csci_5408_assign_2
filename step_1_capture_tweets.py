import tweepy
import time
import json
import csv


consumer_key = "z56cu40Jq1XxntXeGKLfhNZnk"
consumer_secret = "NWsAOtbQ4lVGPq7xooVbE21XEeMnDuFBtdTfyZzc85Czh4wKnm"
access_key = "1003752992171024386-lsvEB53AROSLhKGJgEchdgajkBJTIC"
access_secret = "NV7vVHJX3FrGJFm1fx7hivxKBLOfVom34gYAJeaUEklX1"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# def get_profile(zhenbang):
#     api = tweepy.API(auth)
#     try:
#         user_profile = api.get_user(zhenbang)
#     except tweepy.error.TweepError as e:
#         user_profile = json.loads(e.response.text)
#
#         return user_profile
#
# def get_trends(location_id):
#     api = tweepy.API(auth)
#     try:
#         trends = api.trends_place(location_id)
#     except tweepy.error.TweepError as e:
#         trends = json.loads(e.response.txt)
#
#     return trends

# code from lab.
def get_tweets(query):
    api= tweepy.API(auth)
    try:
        tweets = api.search(query)
    except tweepy.error.TweepError as e:
        tweets = [json.loads(e.response.text)]

    return tweets


queries = ["eminem", "love OR hare", "revival", "slim shady", "rap god", "trump", "donald", "concert"]

with open('tweets.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['id', 'user', 'created_at', 'text'])
    for query in queries:
        t = get_tweets(query)
        for tweet in t:
            writer.writerow([tweet.id_str, tweet.user.screen_name, tweet.created_at, tweet.text.encode('unicode-escape')])






























