import os
import tweepy
import json
import requests
from configparser import ConfigParser

class TwitterBot:
    def __init__(self, config_file='config.ini'):
        self.load_config(config_file)
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)

    def load_config(self, config_file):
        # Load API keys and other configurations from the config file
        config = ConfigParser()
        config.read(config_file)

        self.consumer_key = config.get('Twitter', 'consumer_key')
        self.consumer_secret = config.get('Twitter', 'consumer_secret')
        self.access_token = config.get('Twitter', 'access_token')
        self.access_token_secret = config.get('Twitter', 'access_token_secret')

    def load_quotes(self, quotes_file='quotes.json'):
        # Load the quotes list from the quotes file
        with open(quotes_file, 'r') as f:
            self.quotes = json.load(f)

    def load_last_tweet_index(self, index_file='last_tweet_index.txt'):
        # Load the last tweeted quote index from a file
        if os.path.exists(index_file):
            with open(index_file, 'r') as f:
                self.tweet_index = int(f.read().strip())
        else:
            self.tweet_index = -1

    def save_last_tweet_index(self, index_file='last_tweet_index.txt'):
        # Save the next tweet index to a file
        with open(index_file, 'w') as f:
            f.write(str(self.next_tweet_index))

    def get_next_tweet(self):
        # Get the next quote to tweet
        self.tweet_index = (self.tweet_index + 1) % len(self.quotes)
        return self.quotes[self.tweet_index]

    def download_image(self, url, filename):
        # Download the image and save it to the specified file
        image = requests.get(url).content
        with open(filename, 'wb') as f:
            f.write(image)

    def tweet(self, quote, image_filename):
        # Send a tweet
        tweet_text = f'"{quote["quote"]}" - {quote["character"]}'
        self.api.update_with_media(image_filename, tweet_text)

    def run(self):
        # Main execution function
        self.load_quotes()
        self.load_last_tweet_index()

        quote = self.get_next_tweet()
        image_filename = 'image.jpg'
        self.download_image(quote['image'], image_filename)
        self.tweet(quote, image_filename)

        self.next_tweet_index = (self.tweet_index + 1) % len(self.quotes)
        self.save_last_tweet_index()

if __name__ == '__main__':
    bot = TwitterBot()
    bot.run()
