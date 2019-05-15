
from tweepy import API
from tweepy import OAuthHandler
import tweepy as tw
import csv
import pandas as pd
import twitter_credentials

auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
api = tw.API(auth, wait_on_rate_limit=True)

csvFile = open('dejavu.csv','a')
csvWriter = csv.writer(csvFile)

search_words = "Specialty Coffee"
date_since = '2019-05-10'

tweets = tw.Cursor(api.search,q=search_words,since=date_since).items(100)
#users_locs = [[tweet.user.screen_name, tweet.text.encode('utf-8'), tweet.user.location] for tweet in tweets]

#tweet_table = pd.DataFrame(data=users_locs,columns=['username', 'tweet', "location"])
#print(tweet_table)

for tweet in tweets:
    csvWriter.writerow([tweet.created_at, tweet.user.screen_name, tweet.text.encode('utf-8'), tweet.user.location])
    print(tweet.user.screen_name, tweet.text.encode('utf-8'), tweet.user.location)
