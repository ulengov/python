spis = []

inp = '1'

while inp != '0':
    inp = input('Введите элемент списка либо 0: ')
    if inp != '0':
        spis.append(inp)

print(spis)

for i,a in enumerate(spis):
    if i % 2 == 1:
        spis[i-1],spis[i] = spis[i],spis[i-1]

print(spis)
