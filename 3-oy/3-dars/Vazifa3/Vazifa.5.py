class Float:
    def __init__(self, value):
        self.value = value
    @property
    def value(self):
        return self.__dict__['value']
    @value.setter
    def value(self, value):
        if isinstance(value, float):
            self.__dict__['value'] = value
        else:
            raise TypeError

f=Float(10.5)
f=Float(1.5)
print(f.value)
