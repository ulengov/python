f1 = open("3.txt", 'r')

sum = 0
cnt = 0

for line in f1:
     pars = line.split(' ')
     okl = int(pars[1])
     cnt +=1
     sum += okl
     if okl < 20000:
         print(pars[0])

print(f"Среднее: {round(sum/cnt)}")

f1.close()
