import os
import json
import random
import tweepy
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def verify_credentials():
    """Verify Twitter API credentials"""
    credentials = {
        'TWITTER_API_KEY': os.getenv('TWITTER_API_KEY'),
        'TWITTER_API_SECRET_KEY': os.getenv('TWITTER_API_SECRET_KEY'),
        'TWITTER_ACCESS_TOKEN': os.getenv('TWITTER_ACCESS_TOKEN'),
        'TWITTER_ACCESS_TOKEN_SECRET': os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
    }
    
    # Validate credential formats
    expected_lengths = {
        'TWITTER_API_KEY': (25, 25),        # API Key should be exactly 25 chars
        'TWITTER_API_SECRET_KEY': (50, 50),  # API Secret should be exactly 50 chars
        'TWITTER_ACCESS_TOKEN': (50, 50),    # Access Token should be exactly 50 chars
        'TWITTER_ACCESS_TOKEN_SECRET': (45, 45)  # Access Secret should be exactly 45 chars
    }
    
    for key, value in credentials.items():
        if not value:
            raise ValueError(f"Missing {key}")
        
        min_len, max_len = expected_lengths[key]
        if not (min_len <= len(value) <= max_len):
            raise ValueError(
                f"{key} length is {len(value)} chars, "
                f"expected between {min_len} and {max_len} chars"
            )
        
        # Check for invalid characters
        if not value.replace('-', '').isalnum():
            raise ValueError(f"{key} contains invalid characters")
    
    print("\nCredential Format Validation:")
    for key, value in credentials.items():
        print(f"{key}: {'*' * (len(value)-8)}{value[-8:]}")
    
    return credentials

def get_random_quote():
    """Get a random quote from quotes.json"""
    try:
        with open('quotes.json', 'r', encoding='utf-8') as file:
            quotes = json.load(file)
            return random.choice(quotes)
    except Exception as e:
        print(f"Error reading quotes file: {e}")
        return None

def tweet_quote():
    """Tweet a random quote"""
    try:
        print("\nDebug: Environment Variables")
        credentials = verify_credentials()
        
        print("\nSetting up Twitter client...")
        auth = tweepy.OAuthHandler(
            credentials['TWITTER_API_KEY'], 
            credentials['TWITTER_API_SECRET_KEY']
        )
        auth.set_access_token(
            credentials['TWITTER_ACCESS_TOKEN'], 
            credentials['TWITTER_ACCESS_TOKEN_SECRET']
        )
        
        # Set up both API and Client
        api = tweepy.API(auth)
        client = tweepy.Client(
            consumer_key=credentials['TWITTER_API_KEY'],
            consumer_secret=credentials['TWITTER_API_SECRET_KEY'],
            access_token=credentials['TWITTER_ACCESS_TOKEN'],
            access_token_secret=credentials['TWITTER_ACCESS_TOKEN_SECRET']
        )
        
        # Test API connection
        user = api.verify_credentials()
        print(f"Successfully authenticated as: @{user.screen_name}")

        # Get and format quote
        quote = get_random_quote()
        if quote:
            print(f"Quote data: {quote}")
            
            tweet_text = f'"{quote["quote"]}"'
            if quote.get('character'):
                tweet_text += f' - {quote["character"]}'

            print(f"Attempting to post tweet: {tweet_text}")
            
            # Post tweet using client
            response = client.create_tweet(text=tweet_text)
            print(f"Tweet posted successfully!")
            return True
        else:
            print("No quote available to tweet")
            return False

    except Exception as e:
        print(f"Error posting tweet: {e}")
        import traceback
        print(traceback.format_exc())
        return False

if __name__ == "__main__":
    tweet_quote()
