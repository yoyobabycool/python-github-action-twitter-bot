import os
import tweepy
import requests

consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_API_SECRET_KEY']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
client = tweepy.Client(consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret)

url_response = requests.get(os.environ['EMOJI_URL'])
if url_response.status_code == 200:
  image_data = url_response.json()
  image_url = image_data.get("url")
  image_path = f"emoji_image.png"
  if image_url:
    image_response = requests.get(image_url).content
    if image_response.status_code == 200:
      with open(image_path, "wb") as f:
          f.write(image_response)
        media_upload = api.media_upload(image_path)
        tweet_text = 'check this!'
        client.create_tweet(text = tweet_text, media_ids=[media_upload.media_id])
        os.remove(image_path)
        print("success")
    else:
      print("failed to download image")
  else:
    print("image url not found")
else:
  print("failed to get image url")
        
