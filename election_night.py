from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
#replaced with qwertqwertqwerty for privacy
consumer_key = "qwertqwertqwerty"
consumer_secret = "qwertqwertqwerty"
accest_token = "qwertqwertqwerty"
access_secret = "qwertqwertqwerty"

#from twitterapistuff import *

class listener(StreamListener):

    def on_data(self, data):

		all_data = json.loads(data)

		tweet = all_data["text"]
		sentiment_value, confidence = s.sentiment(tweet)
		print(tweet, sentiment_value, confidence)

		if confidence*100 >= 80:
			output = open("trump_sentiment0015.txt","a") #this is the most recent file being written to
			output.write(sentiment_value)
			output.write('\n')
			output.close()

		return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(accest_token, access_secret)

#Prevents crashing if tweet without text mined
while True:
    try:
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=["Trump"])
    except KeyError:
        print("I guess this tweet didn't have a key...")
