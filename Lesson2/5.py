spis = [25, 17, 15, 9, 7, 5]

inp = 0

while inp != 999:
    print(spis)
    inp = int(input('Введите натуральное число либо 999: '))
    if inp != 999:
        spis.append(inp)
        spis.sort(reverse=True)


