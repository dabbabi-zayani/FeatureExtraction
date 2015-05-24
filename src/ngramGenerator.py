# N-gram generator based on nltk module
# K-most frequent words in a class od tweets
import nltk
import operator # for sorting dictionnares

# getting word frequencies from training data for a given class

def getTweetWords(tweet):
    all_words = []
    sTweet=tweet.split()
    return sTweet

def get_word_features(wordlist): # from a list of words returns a dictionnary with word, freq as key, value
    wordlist = nltk.FreqDist(wordlist)
    result=[]
    for k in wordlist.keys():
        result.append([k,wordlist[k]])
    return result

def ngramText(filename): # generate vector of ngrams in text file
    textWords=[]
    f=open(filename,"r")
    line=f.readline()
    while line:
        textWords.extend(getTweetWords(line))
        line=f.readline()
    f.close()
    return textWords

def sortList(x):
    return list(reversed(sorted(x, key=operator.itemgetter(1))))

#def suvDict(d,k): # extract k most frequent words


filename="../data/tweets.txt"
ngram=ngramText(filename)

#print get_words_in_tweets(tweets)
#print ngram
d=get_word_features(ngram)
print sortList(d)
#word_features = get_word_features(get_words_in_tweets(tweets))
