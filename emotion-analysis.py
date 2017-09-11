#ComPilED by AdiTya MoHaN

import tweepy
from textblob import TextBlob
import csv
import matplotlib.pyplot as plt

consumer_key= 'tn2zlRaR9kqrPc10nAmlyRuWS'
consumer_secret= 'ZCStbkI2JqgjEfIXoJlwU31IJ9TXjIpxPxT19mMmQlEdeMFWSD'

access_token='853412742723710976-GnRdTjLyRQWAk2NwciA6HhDCuDNSCVD'
access_token_secret='KHWCYDz5tIuTGfEuj4EHOq1EFYOKJufaf8TsFNVdN8Fmr'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('immigrants')

csvfile = open('twitter_sentiment.csv', 'wb')
writer = csv.writer(csvfile)   

count_positive = 0 ;
count_negative = 0 ;

for tweet in public_tweets:
    foo = tweet.text.encode('utf-8').strip()  

    analysis = TextBlob(tweet.text).sentiment
    emotion = analysis.polarity
    if emotion > 0:
       count_positive = count_positive +1
       writer.writerow([foo,"positive",analysis]) 
    else : 
       count_negative = count_negative +1
       writer.writerow([foo,"negative",analysis])         
    
csvfile.close()

labels = 'Positive Reviews', 'Negative Reviews'
sizes = [count_positive, count_negative]
colors = ['lightcoral', 'lightskyblue']
explode = (0.1, 0)  
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()

print("ENtire process completed successfully ! Open your CSV file and look at the results.")
