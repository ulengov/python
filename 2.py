arg = int(input('Введите время в секундах: '))

hour = arg // 3600
min = (arg - hour * 3600) // 60
sec = arg % 60

print(f'{hour:02}:{min:02}:{sec:02}')

