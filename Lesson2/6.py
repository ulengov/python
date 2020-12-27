market = []

i = 0
exit = 'нет'

while exit !='да':
    i +=1
    name = input('Название: ')
    pric = float(input('цена: '))
    koll = int(input('количество: '))
    edin = input('единица: ')

    market.append((i,{"название": name,"цена": pric,"количество": koll,"ед": edin}))

    exit = input('Закончить ввод? (да): ')

name = set()
pric = set()
koll = set()
edin = set()

for i in market:
    name.add(i[1].get("название"))
    pric.add(i[1].get("цена"))
    koll.add(i[1].get("количество"))
    edin.add(i[1].get("ед"))

anlz = {"название": list(name),"цена": list(pric),"количество": list(koll),"ед": list(edin)}

print(anlz)
