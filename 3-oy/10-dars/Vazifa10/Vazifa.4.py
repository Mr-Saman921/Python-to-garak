from Vazifa3 import Home


class Window(Home):
    def __init__(self, name, address, num_windows):
        super().__init__(name, address)
        self.name = name
        self.address = address
        self.num_windows = num_windows

    def open_window(self):
        return f"{self.num_windows} windows are now open"


class Door(Home):
    def __init__(self, name, address, num_doors):
        super().__init__(name, address)
        self.name = name
        self.address = address
        self.num_doors = num_doors

    def open_door(self):
        return f"{self.num_doors} doors are now open"


class Room(Home):
    def __init__(self, name, address, num_rooms):
        super().__init__(name, address)
        self.name = name
        self.address = address
        self.num_rooms = num_rooms

    def clean_room(self):
        return f"{self.num_rooms} rooms are now clean"

home_window = Window("Home with Windows", "123 Window St", 4)
home_door = Door("Home with Doors", "456 Door Ave", 2)
home_room = Room("Home with Rooms", "789 Room Blvd", 3)

print(home_window.name)
print(home_door.address)
print(home_room.name)

print(home_window.open_window())
print(home_door.open_door())
print(home_room.clean_room())

