from __future__ import absolute_import
from parkman.config import config
import tweepy


class TwitterGateway:
    def __init__(self):
        twitter_config = config.get('twitter')
        consumer_key = twitter_config.get('consumer_key')
        consumer_secret = twitter_config.get('consumer_secret')
        access_token = twitter_config.get('access_token')
        access_token_secret = twitter_config.get('access_token_secret')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)

    def get_my_tweets(self):
        public_tweets = self.api.home_timeline()
        return public_tweets

    def get_original_tweet(self, screen_name, number_of_tweets):
        statuses = self.api.user_timeline(screen_name=screen_name, count=number_of_tweets)
        original_ids = []
        for status in statuses:
            if status.in_reply_to_status_id:
                original_ids.append(status.in_reply_to_status_id)

        original_statuses = self.api.statuses_lookup(
            original_ids, 
            include_entities=False,
            trim_user=True)

        for question in original_statuses:
            print question.text