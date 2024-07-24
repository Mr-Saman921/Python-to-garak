from abc import ABC, abstractmethod


class Tv(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

class Remote_control(Tv):
    def __init__(self, brand):
        self.brand = brand
        self.__state = 'off'

    @staticmethod
    def check_power():
        return True

    def on(self):
        if self.check_power():
            if self.__state == 'off':
                self.__state = 'on'
                print('Tv is on')
            else:
                print('Tv is alredy on')
        else:
            print('Power is null')

    def off(self):
        if self.__state == 'on':
            self.__state = 'off'
            print('Tv is off')
        else:
            print('Tv is alredy off')

r = Remote_control('Artel')

r.on()
r.on()

r.off()
r.off()
