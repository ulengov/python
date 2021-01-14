num = [300, 2, 12, 44, 1, 1, 4, 10, 7, 78, 123, 55]

new = [el for i,el in enumerate(num) if i > 0 and num[i] > num[i-1]]

print(new)
