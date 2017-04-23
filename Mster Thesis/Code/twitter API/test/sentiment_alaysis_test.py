""" Twitter Sentimetn Analysis """
""" Test app for Twitter API connection based on Siraj Raval """
""" It is able to search twitter for a list of tweets about any topic """
""" Then analyze each tweet to see how positive or negative it's emotion is """

import tweepy
from textblob import TextBlob

consumer_key = '2zqaRrlnTi7AQrk6gD1lqsoqo'
consumer_key_secret = 'EvGH0LPCjC7lyjt4uszT4s2lQmnd2om7rArDftYibtJ6yoRl8z'

access_token = '4415191522-OuA6gF4Zub4c0bTn4UwunHO2GSH8w1aYEdY9ZHf'
access_token_secret = 'N1jVLY2szClSxJ0zIpkREThkuSWYiiY3ItNKxTN8MJydx'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)

    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
