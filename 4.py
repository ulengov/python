num =  [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

#dict = {i:num.count(i) for i in num}

res = [el for el in num if num.count(el) == 1]

print(res)
