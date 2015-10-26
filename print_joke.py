import time
from random import *

SLP = 2.2
#SLP = 0
if False: '''
with open("rankings.txt") as fp:
    for line in fp:
        adj, noun,sent,score, simil= line.strip().split()
        print("your momma is so", adj, "she's a ",  noun, "similar=",simil,"sentiment=", sent,"Score=", score)
        '''

def printranks(l):
    for line in l:
        adj, noun,sent,score, simil= line
        print("your momma", end=' ')
        time.sleep(random() * SLP)
        print("is so" + 'o' * randrange(0, 4), end=' ')
        time.sleep(random() * SLP)
        print(adj)
        if noun[0] in 'aoeui':
            print("she's an",end=' ')
        else:
            print("she's a", end=' ')
        time.sleep(random() * SLP)
        print(noun)
        time.sleep(random() * SLP)
        #print("your momma is so", adj, "she's a ",  noun, "similar=",simil,"sentiment=", sent,"Score=", score)
      

import pickle
with open("rankings.pkl", "rb") as fp:
    rankings = pickle.load(fp)

rankings.sort(key=lambda x: float(x[-2]) * x[-1])
printranks(rankings)
