# Task 1 Load and inspect the data.

import json
WW_Trends = json.loads(open('datasets/WWTrends.json').read())
US_Trends = json.loads(open('datasets/USTrends.json').read())
# print(WW_Trends)
# print(US_Trends)

# Task 2 Pretty-print the output.

ww_dmp = json.dumps(WW_Trends,indent = 1)
us_dmp = json.dumps(US_Trends,indent = 1)
# print(ww_dmp)
# print(us_dmp)


# Task 3 Extract the names of common trends.

world_trends = {item['name'] for item in WW_Trends[0]['trends']}
us_trends = {item['name'] for item in US_Trends[0]['trends']}
common_trends = world_trends.intersection(us_trends)
# print(common_trends)

# Task 4 Load and inspect the data.

tweets = json.loads(open('datasets/WeLoveTheEarth.json').read())

# Task 5 Extract texts, usernames and hashtags from the tweets.

texts = [item['text'] for item in tweets]
names = [user_mention['screen_name'] for tweet in tweets for  user_mention in tweet['entities']['user_mentions']]
hashtags = [hashtag['text'] for tweet in tweets for  hashtag in tweet['entities']['hashtags']]

# Task 6 Creating frequency distribution.

from collections import Counter
names_count = Counter(names)
hashtags_counts = Counter(hashtags)

# Task 7 Extracting data for retweets.

# retweets =[]
# for tweet in tweets:
#     try : 
#         retweets.append(tweet['retweet_count'], 
#               tweet['retweeted_status']['favorite_count'],
#               tweet['retweeted_status']['user']['followers_count'],
#               tweet['retweeted_status']['user']['screen_name'],
#               tweet['text']) 

#     except:
#         pass
retweets = [
             (tweet['retweet_count'], 
              tweet['retweeted_status']['favorite_count'],
              tweet['retweeted_status']['user']['followers_count'],
              tweet['retweeted_status']['user']['screen_name'],
              tweet['text']) 
            
            for tweet in tweets 
                if 'retweeted_status' in tweet
           ]


# Task 8 Creating a table with insights.
import pandas as pd
retweet_df = pd.DataFrame(
    retweets, 
    columns=['Retweets','Favorites','Followers','ScreenName','Text']).groupby(
    ['ScreenName','Text','Followers']).sum().sort_values(by=['Followers'], ascending=False)

# Task 9 Extracting languages and plotting their frequency distribution.
import matplotlib
import matplotlib.pyplot as plt
tweets_languages = []
for tweet in tweets:
        tweets_languages.append(tweet['lang'])

plt.hist(tweets_languages)
plt.show()

