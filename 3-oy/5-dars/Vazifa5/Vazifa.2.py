class Counter:
    def __init__(self):
        self.count()

    def count(self):
        try:
            with open('count.txt', 'r') as file:
                current_count = int(file.read())
        except FileNotFoundError:
            current_count = 0
        current_count += 1
        with open('count.txt', 'w') as file:
            file.write(str(current_count))

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
