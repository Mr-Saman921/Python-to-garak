class Phone:
    def __init__(self, model, price, color):
        self.model = model
        self.price = price
        self.color = color
    def phone_info(self):
        print(f"Model-{self.model}\nPrice-{self.price}\nColor-{self.color}")
phone=Phone(model="Iphone 14 pro", price="1000$", color="Black")
phone.phone_info()