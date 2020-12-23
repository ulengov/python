vir = int(input('Выручка: '))
izd = int(input('Издержки: '))

if vir>izd:
    print('Фирма отработала с прибылью ' + str(vir - izd))
    print('Реньабельность ' + str(vir/izd))
    sot = int(input('Число сотрудников: '))
    print('Прибыль на 1 сотрудника ' + str((vir-izd)/sot))

elif vir<izd:
    print('Фирма отработала с убытком ' + str(izd - vir))

else:
    print('Фирма отработала в ноль')





