def int_func(world):
    return world.title()

str = 'yturyeut rtureteruty owtorituoeriut oweuiioweut woeiuwoit'

spis = str.split(' ')
res = ''

for i, world in enumerate(spis):
    res = res+int_func(world)+' '

print(res)
