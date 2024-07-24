class Phone:
    def __init__(self, model, price, color):
        self._model = model  # protected attribute
        self.price = price  # public attribute
        self.color = color  # public attribute

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new_model):
        if isinstance(new_model, str):
            self._model = new_model
        else:
            raise ValueError("Model nomi yaroqli matn bo'lishi kerak")

    @model.deleter
    def model(self):
        del self._model

phone1 = Phone("iPhone 13", 999, "Black")
print(phone1.model)

phone1.model = "Samsung Galaxy S21"
print(phone1.model)

# del phone1.model
# print(phone1.model)

