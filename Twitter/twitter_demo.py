## Sample program to print the Tweets in your feed
import tweepy
import json
from pprint import pprint 

##Reading the login credentials that we have placed in a json file
config_file_location = 'C:/Users/sujee/Desktop/Keys/Twitter/tweet_config.json'
with open(config_file_location) as login_data:
    content = json.load(login_data)

##Setting up the credentials 
#Consumer key and secret are like login credentials into account
#access key and secret access key are used when an API request is made behalf of your App
consumer_key = content["API Key"]
consumer_secret_key = content["API Secret Key"]
access_token = content["Access Token"]
access_secret_token = content["Access Secret Token"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_secret_token)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

# To print the content from your feed
for tweet in public_tweets:
    print(tweet.text)

##User object for twitter

user = api.get_user('KurapatiSujeeth')
for friend in user.friends():
    print(friend.screen_name)
print(user.screen_name)
print(user.followers_count)


## Next Up we will read the config file from S3 bucket
