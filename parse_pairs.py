import nltk

def split(l):
    copy_l=list(l)
    i = 0
    while True:
        try:
            i = copy_l.index('.')
            yield nltk.pos_tag(copy_l[0:i] + ['.'])
            del copy_l[0:i+1]
        except ValueError:
            return

def parse(parsed):
    for i in range(len(parsed) - 1):
        if {parsed[i][1], parsed[i+1][1][:-1]} == {"JJ", "NN"}:
            return (parsed[i][0], parsed[i+1][0],)

#main

#emma = nltk.corpus.gutenberg.words('')
with open("article.txt", errors='ignore') as fp: emma= nltk.tokenize.word_tokenize(fp.read())

i = 0
for sentence in split(emma):
    a = parse(sentence)
    if a == None:
        continue
    adj = a[0]
    noun = a[1]
    print("JJ: %s, NN: %s" % (adj, noun))
    i += 1
    with open("pairs.txt", "a") as fp:
        fp.write("%s %s\n" % (adj, noun))


#load pairs
pairs = []
with open('pairs.txt','r') as fh:
    for line in fh:
        pair = str(line).split(" ")
        pair = [ s.strip("\n") for s in pair ]
        pairs.append(pair)

from nltk.stem import *
wnl = WordNetLemmatizer()

len(pairs)
pairs = [ (pair[0], wnl.lemmatize(pair[1],'n')) for pair in pairs]

print(pairs)
from nltk.corpus import wordnet as wn
from alchemyapi import AlchemyAPI
import json

alchemyapi = AlchemyAPI()

momma = wn.synsets("mom")[0]
rankings = []
for pair in pairs:
    adj,noun = pair

    #wn similarity
    syn = wn.synsets(noun)
    if len(syn)==0:
        similarity =0
    else:
        similarity = momma.path_similarity(syn[0])
    if similarity is None:
        similarity = 0

    #sentiment
    response = None
    #response = alchemyapi.sentiment_targeted('text', "%s %s" % (adj,noun), adj)
    try:
        sentiment = response['docSentiment']['type']
    except:
        print(response)
        sentiment = 0
    if sentiment is None:
        sentiment = 0

    rankings.append((adj, noun,sentiment,similarity))
    print((adj, noun, sentiment,similarity))

print(rankings)
rankings.sort(key=lambda l: l[-1])
rankings.reverse()

with open("rankings.txt","a") as fh:
    for r in rankings:
        adj, noun, sentiment,similarity = r
        fh.write("%s %s %s %s\n" % (adj, noun, sentiment,similarity))

#print out the found pair
for rank in rankings:
    adj,noun,x,y = rank
    print(("Your momma is so %s, she's a %s" % (adj,noun)))
#end
