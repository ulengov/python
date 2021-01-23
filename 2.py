class Road:
    def __init__(self,lenght, widht):
        self._lenght = lenght
        self._widht = widht

    def rashet(self, massa, hight):
        return self._lenght * self._widht * massa * hight

doroga = Road(5000,20)

print(f'Необходимо {doroga.rashet(25,5)/1000} тонн')
