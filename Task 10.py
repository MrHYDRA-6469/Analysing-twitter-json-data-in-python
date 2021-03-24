# Task 10
# Sentiment Analysis
import sys 
import os
sys.path.append(os.path.abspath("C:\Users\apyad\OneDrive\Documents\MTE\source.py"))
from source import *

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

D1_ww = pd.DataFrame([item['name'] for item in WW_Trends[0]['trends']],columns = ['Text'])
D2_us = pd.DataFrame([item['name'] for item in US_Trends[0]['trends']],columns = ['Text'])
sentiment_scores_of_ww = (D1_ww['Text']).apply(sid.polarity_scores)
sentiment_scores_of_us = (D2_us['Text']).apply(sid.polarity_scores)
sentiment_us = sentiment_scores_of_us.apply(lambda X : X['compound'])
sentiment_ww = sentiment_scores_of_ww.apply(lambda X : X['compound'])