vir = int(input('Выручка: '))
izd = int(input('Издержки: '))
prb = vir - izd

if vir>izd:
    print('Фирма отработала с прибылью ' + str(prb))
    print('Реньабельность ' + str(prb/izd))
    sot = int(input('Число сотрудников: '))
    print('Прибыль на 1 сотрудника ' + str((prb)/sot))

elif vir<izd:
    print('Фирма отработала с убытком ' + str(-prb))

else:
    print('Фирма отработала в ноль')





