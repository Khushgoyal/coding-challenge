import os
import tweepy as tw
from github_search import *
from variables import *

#Accessing token for the twitter api
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#output json file path goes in the directory 
output_filepath = '../output.json'

#function to get the top tweets where cutoff is 10 means top 10 tweets.
def get_top_tweets(search_query, cutoff=10):
    ret_list = []
    tweets = tw.Cursor(api.search,q=search_query ,result_type="recent").items(cutoff)
    for t in tweets:
        screen_name = t._json['user']['screen_name']
        tweet_text = t.text
        ret_list.append((screen_name,tweet_text))
    return ret_list

#Taking output_json varibale to store tweets
output_json = {}
for query in search_words:
    tweets_list = get_top_tweets(query)
    output_json[query] = tweets_list

#Save the tweets in the file.
with open(output_filepath,'w') as filep:
    json.dump(output_json,filep)


