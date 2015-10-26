rankings = []
with open("rankings.txt") as fp:
    for line in fp:
        line = line.strip().split(" ")
        if len(line) != 4:
            print("WHAT THE SHIT")
        rankings.append(tuple(line))

for rankshit in rankings:
    adj,noun,x,y = rankshit
    print(("Your momma is so %s, she's a %s" % (adj,noun)))

