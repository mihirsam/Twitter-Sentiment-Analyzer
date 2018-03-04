import tweepy
from textblob import TextBlob
import numpy as np
import csv
import codecs

# Authentication
c_key = 'Consumer Key (API Key)'
c_secret = 'Consumer Secret (API Secret'

a_key_token = 'Access Token'
a_secret_token = 'Access Token Secret'

auth = tweepy.OAuthHandler(c_key, c_secret)
auth.set_access_token(a_key_token, a_secret_token)

api = tweepy.API(auth)

search = input("Enter text to search : ")

public_tweets  = api.search(search)
data= []

final_array =  np.array(['Tweets', 'Polarity', 'Subjectivity'])
for tweet in public_tweets:
    #tweets
    #tweet.text
    data.append(tweet.text)

    analysis = TextBlob(tweet.text)

    #Polarity
    data.append(analysis.sentiment[0])

    #Subjectivity
    data.append(analysis.sentiment[1])

    data_array = np.array(data)
    final_array = np.vstack([final_array, data_array])
    data = []

csv1 = codecs.open('report.csv', 'w+', encoding= 'UTF-8', errors = 'ignore')
csv1.close()

csv1 = codecs.open('report.csv', 'w', encoding= 'UTF-8', errors = 'ignore')
with csv1:
    writer = csv.writer(csv1)
    writer.writerows(final_array)

print("Completed!")
