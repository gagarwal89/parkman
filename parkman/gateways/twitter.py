from __future__ import absolute_import
from parkman.config import config
from parkman.utils.collection import CollectionUtil
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

        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def get_my_tweets(self):
        public_tweets = self.api.home_timeline()
        return public_tweets

    def get_original_tweets(self, screen_name, number_of_tweets):
        for status in tweepy.Cursor(self.api.user_timeline, screen_name=screen_name).items(number_of_tweets):
            
            # process status here
            if status.in_reply_to_status_id:
                yield status.in_reply_to_status_id

    def get_all_tweets_for_user(self, screen_name):
        # Download all tweets for a user
        for status in tweepy.Cursor(self.api.user_timeline, screen_name=screen_name).items():
            yield status

    def get_bulk_statuses(self, status_ids):
        max_size = 100 # Max size twitter allows
        for batch_ids in CollectionUtil.generate_batches(status_ids, max_size):
            for status in self.api.statuses_lookup(batch_ids):
                yield status