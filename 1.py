import time
import itertools

class TrafficLight:
    __color = [['red',7], ['yelow',2], ['green',7], ['yelow', 7]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print("\r" + light[0], end ="")
            time.sleep(light[1])

traf = TrafficLight()
traf.running()
