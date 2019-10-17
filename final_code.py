import re
import tweepy
from time import sleep
import matplotlib.pyplot as plt
from tweepy import OAuthHandler
from textblob import TextBlob
from tkinter import *
import emoji
from googletrans import Translator
google_translator = Translator()

class TwitterClient(object):
    def __init__(self):         #constructor function of class or initializer or handle twitter authentication
       
        access_token = '***************************************************'
        access_token_secret = '*********************************************'
        consumer_key = '***********************************'
        consumer_secret = '******************************************'
 
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
 
    def clean_tweet(self, tweet):  #to get cleen tweets i.e without any Links or special characters
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    def get_tweet_sentiment(self, tweet):       #gives the sentiment value between -1 to 1 i.
        tweet=emoji.demojize(tweet)
        translated = google_translator.translate(tweet)
        tweet = translated.text
        lis = ["not" , "no", "bad", "dirty", "wait", "don't"]
        for i in range(0,len(lis)):
            res = tweet.find(lis[i]) 
            if res >= 0:
                return 'negative'
        
        analysis = TextBlob(self.clean_tweet(tweet)) #textblob is natural language processing library uses Naive bayes classifier algorithm
                                                    #tokenize tweets
        if analysis.sentiment.polarity >= 0.05:
            return 'positive'
        elif ((analysis.sentiment.polarity > -0.05) and (analysis.sentiment.polarity < 0.05)):
            return 'neutral'
        else:
            return 'negative'
 
    def get_tweets(self, query, count): #takes query and fetch tweets from api in fetched tweets
        tweets = []
        try:
            fetched_tweets = self.api.search(q = query, count = count)
 
            for tweet in fetched_tweets:
                parsed_tweet = {}

                parsed_tweet['text'] = tweet.text
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) #It passes to get_get_sentiment
 
                if tweet.retweet_count > 0:
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
 
            return tweets
 
        except tweepy.TweepError as e:
            print("Error : " + str(e))

def analyze():
    Slist1.delete(0,END)
    api = TwitterClient()
    strq=e1.get()
    n=e2.get()
    tweets = api.get_tweets(query = strq, count = n)
    

    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    if len(ptweets)!=0:
        pt=format(100*len(ptweets)/len(tweets))
        print(pt)
    else:
        pt=format(100*len(ptweets))
        print(pt)    
    a="Positive tweets % "
    Slist1.insert(END,a)
    Slist1.insert(END,pt)
   
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    if len(ntweets)!=0:
        nt=format(100*len(ntweets)/len(tweets))
        print(nt)
    else:
        nt=format(100*len(ntweets))
        print(nt)
    b="negative tweets % "
    Slist1.insert(END,b)
    Slist1.insert(END,nt)
   
    nutweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
    nut=format(100*(len(tweets)-len(ntweets)-len(ptweets))/len(tweets))
    c="Neutral tweets % "
    print(nut)
    Slist1.insert(END,c)
    Slist1.insert(END,nut)
   
    print("\n\nPositive tweets:")
    for tweet in ptweets[::1]:
        print(tweet['text'])
 
    print("\n\nNegative tweets:")
    for tweet in ntweets[::1]:
        print(tweet['text'])
        
    print("\n\nNeutral tweets:")
    for tweet in nutweets[::1]:
        print(tweet['text'])
       
       
       
    labels = 'Positive', 'Negative','Neutral'
    sizes = [pt,nt,nut]
    explode = (0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=70)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()   
       
        
   
window=Tk() #GUI design

window.wm_title("Sentimetal Analysis for Feedback Sentiments")

l11=Label(window,text="Instructions : ")
l11.grid(row=0,column=0)

l12=Label(window,text="1)Enter Tags")
l12.grid(row=1,column=0)

l13=Label(window,text="2)Enter from how many tweets you want to analyze result.")
l13.grid(row=3,column=0)


e1=Entry(window,fg="darkorchid4")
e1.grid(row=1,column=1)

e2=Entry(window,fg="green")
e2.grid(row=3,column=1)

b1=Button(window,text="Analyze",fg="khaki1",bg="blue",command=analyze)
b1.grid(row=5,column=1)

Slist1=Listbox(window, height=20,width=80,bg="brown",fg="ivory2")
Slist1.grid(row=10,column=0,rowspan=8,columnspan=4)

window.mainloop()
