import tweepy
from tweepy import OAuthHandler
import json

consumerKey = 'consumer key here'
consumerSecret = 'consumer secret here'
accessToken = 'access token here'
accessTokenSecret = 'access token secret here'

auth = OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)


def showTweets(screenName, numberOfTweets=200):
    '''
    returns the 'numberOfTweets=200' 
    last tweets of 
    a twitter user in a list
    '''
    tweets = api.user_timeline(screen_name = screenName, 
        count = numberOfTweets, 
        include_rts = True,
        tweet_mode='extended')

    result = []
    for status in tweets:
        text = status._json['full_text']
        result.append(text)
    return result

def international_relations(username):
    '''
    a function to check a country's
    international relations based on
    a politician's twitter page.

    Takes 'username' as an argument (str)
    '''
    from helper import countries
    counter = 0
    for tweet in showTweets(username):
        lowered = tweet.lower()
        split = lowered.split(' ')
        for word in split:
            if word in countries:
                counter += 1
                print('- '+tweet)
                break
    print('_________________')
    print()
    print(str((counter/200)*100)+"% of "+username+"'s last 200 tweets contain a country's name")



#international_relations('realdonaldtrump')