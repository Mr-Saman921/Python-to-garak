from typing import Any

class Mylist:

    def __init__(self):
        self.__list1=[]

    def add(self,  other: Any):
        self.__list1.append(other)

    def delete(self, _index: int):
        if isinstance(_index, int):
            self.__list1.remove(self.__list1[_index])

    def replace(self, _index: int, other: Any):
        if isinstance(_index, int) and len(self.__list1)>_index:
            self.__list1[_index]=other
        else:
            pass

    def clear(self):
        self.__list1=[]

    def __str__(self):
        return str(self.__list1)

mylist=Mylist()
mylist.add("Ali")
mylist.add("Bobur")
mylist.add("Vali")
mylist.delete(1)
mylist.replace(1, "Aziz")
# mylist.clear()
print(mylist)