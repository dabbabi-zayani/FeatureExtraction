# this file contains elemantary functions to map a tweet into a vector
# e.g : emoticons score, POS tags counts ...
from __future__ import division
import re
# emoticons scores by category , change weighting if needed
def createEmoticonDictionary():
    emo_scores = {'Positive': 3, 'Extremely-Positive': 4, 'Negative':1,'Extremely-Negative': 0,'Neutral': 2}
    emo_score_list={}
    fi = open("../resources/emoticon.txt","r")
    l=fi.readline()

    while l:
        l=l.replace("\xc2\xa0"," ")
        li=l.split(" ")
        l2=li[:-1]
        l2.append(li[len(li)-1].split("\t")[0])
        sentiment=li[len(li)-1].split("\t")[1][:-1]
        score=emo_scores[sentiment]
        l2.append(score)
        for i in range(0,len(l2)-1):
            emo_score_list[l2[i]]=l2[len(l2)-1]
        l=fi.readline()
    return emo_score_list

def emoticonScore(tweet):
    "calculate the aggregate score of emoticons in a tweet"
    s=0;
    d=createEmoticonDictionary()
    l=tweet.split(" ")
    for i in range(0,len(l)):
        if l[i] in d.keys():
            print d[l[i]]
            s=s+d[l[i]]
    return s

def lenTweet(tweet):
    return len(tweet)

def upperCase(tweet): # returns 1 if there is uppercase words in tweet, 0 otherwise
    result=0
    for w in tweet.split():
        if w.isupper():
            result=1
    return result

def exclamationTest(tweet):
    result=0
    if ("!" in tweet):
        result=1
    return result

def exclamationCount(tweet):
    return tweet.count("!")

def questionTest(tweet):
    result=0
    if ("?" in tweet):
        result=1
    return result

def questionCount(tweet):
    return tweet.count("?")

def freqCapital(tweet): # ratio of number of capitalized letters to the length of tweet
    count=0
    for c in tweet:
        if (str(c).isupper()):
            count=count+1
    return count/len(tweet)
    
    

#t=raw_input("tweet :")
#print emoticonScore(t)
