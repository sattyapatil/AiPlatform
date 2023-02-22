import tweepy
from config import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET


class TwitterService:
    def __init__(self):
        auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)

    def get_trending_tweets(self, query, count):
        try:
            trending_tweets = self.api.search_tweets(q=query, count=count)
            return [tweet._json for tweet in trending_tweets]
        except tweepy.TweepError as e:
            # log error here
            return []

    def get_user_tweets(self, user_id):
        try:
            user_tweets = self.api.user_timeline(user_id=user_id)
            return [tweet._json for tweet in user_tweets]
        except tweepy.TweepError as e:
            # log error here
            return []
