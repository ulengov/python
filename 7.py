import json

dict = {}
sum = 0
cnt = 0

with open("7.txt") as f1:

    for line in f1:
        cnt +=1
        pars = line.split(' ')
        prb = int(pars[2]) - int(pars[3])
        sum = sum + (prb if prb>0 else 0)
        dict[pars[0]] = prb

    spis = [dict, {"average_profit": sum/cnt}]

with open("7.json", "w") as f2:
    json.dump(spis, f2)

