# Task 1 Load and inspect the data.

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pandas as pd
from collections import Counter
import json
WW_Trends = json.loads(open('datasets/WWTrends.json').read())
US_Trends = json.loads(open('datasets/USTrends.json').read())
# print(WW_Trends)
# print(US_Trends)

# Task 2 Pretty-print the output.

ww_dmp = json.dumps(WW_Trends, indent=1)
us_dmp = json.dumps(US_Trends, indent=1)
# print(ww_dmp)
# print(us_dmp)


# Task 3 Extract the names of common trends.

world_trends = {item['name'] for item in WW_Trends[0]['trends']}
us_trends = {item['name'] for item in US_Trends[0]['trends']}
common_trends = world_trends.intersection(us_trends)
# print(world_trends, "\n")
# print(us_trends, "\n")
# print (len(common_trends), "common trends:", common_trends)
# print(common_trends)

# Task 4 Load and inspect the data.

tweets = json.loads(open('datasets/WeLoveTheEarth.json').read())

# Task 5 Extract texts, usernames and hashtags from the tweets.

texts = [item['text'] for item in tweets]
names = [user_mention['screen_name']
         for tweet in tweets for user_mention in tweet['entities']['user_mentions']]
hashtags = [hashtag['text']
            for tweet in tweets for hashtag in tweet['entities']['hashtags']]
# print (json.dumps(texts[0:5], indent=1),"\n")
# print (json.dumps(names[0:5], indent=1),"\n")
# print (json.dumps(hashtags[0:5], indent=1),"\n")
# Task 6 Creating frequency distribution.

for item in [names, hashtags]:
    c = Counter(item)
    # print (c.most_common(10), "\n")

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
# Task 7 Extracting data for retweets.
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
retweet_df = pd.DataFrame(
    retweets,
    columns=['Retweets', 'Favorites', 'Followers', 'ScreenName', 'Text']).groupby(
    ['ScreenName', 'Text', 'Followers']).sum().sort_values(by=['Followers'], ascending=False)

# Task 9 Extracting languages and plotting their frequency distribution.
tweets_languages = []
for tweet in tweets:
    tweets_languages.append(tweet['lang'])

plt.hist(tweets_languages)
plt.show()

# Task 10
# Sentiment Analysis


sid = SentimentIntensityAnalyzer()

D1_ww = pd.DataFrame([item['name']
                     for item in WW_Trends[0]['trends']], columns=['Text'])
D2_us = pd.DataFrame([item['name']
                     for item in US_Trends[0]['trends']], columns=['Text'])
sentiment_scores_of_ww = (D1_ww['Text']).apply(sid.polarity_scores)
sentiment_scores_of_us = (D2_us['Text']).apply(sid.polarity_scores)
sentiment_us = {"Negetive": sentiment_scores_of_us.apply(lambda X: X['neg']).mean(
), "Positive": sentiment_scores_of_us.apply(lambda X: X['pos']).mean(), "Neutral": sentiment_scores_of_us.apply(lambda X: X['neu']).mean()}
sentiment_ww = {"Negetive": sentiment_scores_of_ww.apply(lambda X: X['neg']).mean(
), "Positive": sentiment_scores_of_ww.apply(lambda X: X['pos']).mean(), "Neutral": sentiment_scores_of_ww.apply(lambda X: X['neu']).mean()}


X = np.arange(len(sentiment_us))
ax = plt.subplot(111)
ax.bar(X, sentiment_us.values(), width=0.2, color='r', align='center')
ax.bar(X-0.2, sentiment_ww.values(), width=0.2, color='b', align='center')
ax.legend(('US_Trends','WW_Trends'))
plt.xticks(X, sentiment_us.keys())
plt.title("Average Sentiment Score", fontsize=17)
plt.show()