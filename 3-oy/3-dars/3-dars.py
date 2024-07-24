class Room:
    def __init__(self, name: str, price: float, color: str, size: float):
        self.name = name
        self.price = price
        self.color = color
        self._size = size

    @property
    def size(self):
        return self._size

    @size.deleter
    def size(self):
        raise AttributeError("Cannot delete the 'size' attribute")


if __name__ == "__main__":
    living_room = Room("Living Room", 1500.0, "Blue", 25.0)
    print(f"Size of the {living_room.name}: {living_room.size} sq. meters")
