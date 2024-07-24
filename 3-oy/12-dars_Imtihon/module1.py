
def calculator(a, b):
    x = a + b
    return x

class ValidateProduct:
    @staticmethod
    def check_title(title):
        if len(title) > 5:
            return True
        else:
            return False

    @staticmethod
    def check_rating(rating):
        if rating == 0:
            return True
        else:
            return False

v = ValidateProduct()
print(v.check_title('Python'))
print(v.check_rating(0))

