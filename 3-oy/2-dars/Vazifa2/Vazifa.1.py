class Rect:
    def __init__(self, heigh, width) -> None:
        self.high = heigh
        self.width = width
    def rect_area(self):
        print(self.high*self.width)
rect=Rect(heigh=int(input("Enter high: ")), width=int(input("Enter width: ")))
rect.rect_area()