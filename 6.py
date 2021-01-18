dict = {}

with open("6.txt") as f1:

    for line in f1:
        sum = 0
        pars = line.split(' ')
        for i in range(1,len(pars)):
            try:
                sum = sum + int(pars[i].split('(')[0])
            except ValueError:
                None

        dict[pars[0]] = sum

    print(dict)
