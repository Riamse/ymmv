#!/usr/bin/python

dick = { }
second = { }
with open("pairs.txt","r") as fh:
    for line in fh:
       pair = str(line).split(" ")
       adj, noun = pair

       if adj in dick:
           dick[adj] += 1
       else:
           dick[adj] = 0
       second[adj] = noun

for adj in dick:
    if dick[adj] < 5:
        print( ("%s %s" % (adj,second[adj])).strip())

#end
