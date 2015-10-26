import pickle
#load pairs
pairs = []
with open('new_pairs.txt','r') as fh:
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
    #response = None
    response = alchemyapi.sentiment_targeted('text', "%s %s" % (adj,noun), adj)
    try:
        sentiment = response['docSentiment']['type']
        score = response['docSentiment']['score']
    except:
        print(response)
        sentiment = 0
        score = 0
    if sentiment is None:
        sentiment = 0
        score = 0

    print("sentiment:", sentiment, "similarity:", similarity, "score:", score)

    rankings.append((adj, noun,sentiment,score,similarity))
    with open("rankings.pkl", "wb") as fp:
        pickle.dump(rankings, fp)
    with open("rankings.json", "w") as fp:
        json.dump(rankings, fp)
    print((adj, noun, sentiment,score,similarity))

#print(rankings)
rankings.sort(key=lambda l: l[-1])
rankings.reverse()

with open("rankings.txt","a") as fh:
    for r in rankings:
        adj, noun, sentiment,score,similarity = r
        fh.write("%s %s %s %s %s\n" % (adj, noun, sentiment,score,similarity))

