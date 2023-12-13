import os
import tweepy
import datetime
import json
import requests

consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_API_SECRET_KEY']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
#api = tweepy.API(auth)
#api.update_status(status='test')
#print("images tweeted")
with open('quotes.json', 'r') as f:
    quotes = json.load(f)
    
# Load last tweeted quote index from a file
if os.path.exists('last_tweet_index.txt'):
    with open('last_tweet_index.txt', 'r') as f:
        tweet_index = int(f.read().strip())
else:
    tweet_index = -1

print(f'index : {tweet_index}')
# Get the quote to tweet
quote = quotes[tweet_index]
# Compose the tweet text
tweet_text = f'"{quote["quote"]}" - {quote["character"]}'
#image_url = quote['image']
#filename = f"image.jpg"
#image = requests.get(image_url).content
#with open(filename, "wb") as f:
#    f.write(image)
#media_upload = api.media_upload(filename)
#tweet_media_id = media_upload.media_id
#api.update_status(status=tweet_text, media_ids=[tweet_media_id])
#api.update_status(status=tweet_text)
client = tweepy.Client(consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret)
# Replace the text with whatever you want to Tweet about
response = client.create_tweet(text=tweet_text)
print(f'Tweeted: {tweet_text}')
next_tweet_index = (tweet_index + 1) 
if next_tweet_index not in range(0, 15):
     next_tweet_index = 0
with open('last_tweet_index.txt', 'w') as f:
    f.write(str(next_tweet_index))
