from typing import Any

class Mydict:

    def __init__(self):
        self.__dict1 = {}

    def add(self,  name: Any, key: Any):
        self.__dict1[name] = key

    def delete(self, other: Any):
        if other in self.__dict1:
            self.__dict1.pop(other)
        else:
            pass

    def replace(self, name: Any, newkey: Any):
        if name in self.__dict1:
            self.__dict1[name] = newkey
        else:
            pass

    def clear(self):
        self.__dict1 = {}

    def __str__(self):
        return str(self.__dict1)

m=Mydict()
m.add("Name", "Sardor")
m.add("Age", "40")
m.add("Email", "siddikovs@.gmail.com")
m.add("Phone", 916730077)
m.delete("Phone")
m.replace("Email", "Sardors@gmail.com")
# m.clear()
print(m)
