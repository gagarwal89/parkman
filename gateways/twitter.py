from __future__ import absolute_import
from parkman.config import config
import tweepy
from tweepy import (
    TweepError
)

class TwitterGateway:
    def __init__(self):
        twitter_config = config.get('twitter')
        consumer_key = twitter_config.get('consumer_key')
        consumer_secret = twitter_config.get('consumer_secret')
        access_token = twitter_config.get('access_token')
        access_token_secret = twitter_config.get('access_token_secret')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth, wait_on_rate_limit=True)

    def get_my_tweets(self):
        public_tweets = self.api.home_timeline()
        return public_tweets

    def get_original_tweet(self, screen_name, number_of_tweets):
        original_tweets = []
        for status in tweepy.Cursor(self.api.user_timeline, screen_name=screen_name).items(number_of_tweets):
            
            # process status here
            if status.in_reply_to_status_id:
                original_tweet = self.process_status(status)

                if original_tweet:
                    print original_tweet

    def process_status(self, status):
        if not status.in_reply_to_status_id:
            return status.text
        else:
            try:
                status = self.api.get_status(status.in_reply_to_status_id)
                return self.process_status(status)
            except TweepError as e:
                return None
