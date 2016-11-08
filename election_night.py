from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

print("Hello World!")
#consumer key, consumer secret, access token, access secret.
#Contains confidential information, so replaced with "qwerty"
consumer_key = 'qwerty'
consumer_secret = 'qwerty'
accest_token = 'qwerty'
access_secret = 'qwerty'

#from twitterapistuff import * #Commented out because I couldn't find the library, and it doesn't seem to do anything
class listener(StreamListener):

    def on_data(self, data):

		all_data = json.loads(data)
		tweet = all_data["text"]
		sentiment_value, confidence = s.sentiment(tweet)
		print(tweet, sentiment_value, confidence)

		if confidence * 100 >= 80:
			output = open("election_out_test.txt","a")
			output.write(sentiment_value)
			output.write('\n')
			output.close()

		return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(accest_token, access_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Trump"]) # #election2016
