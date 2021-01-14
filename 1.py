from sys import argv

name, x, y, z = argv

try:
    print(int(x) * int(y) + int(z))

except ValueError:

    print('ValueError')
