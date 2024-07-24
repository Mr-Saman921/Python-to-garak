
class Sort:

    @staticmethod
    def sort_dict(data):
        assert isinstance(data, dict), "Argument must be a dictionary"
        result = [value for value in data.values() if isinstance(value, int) and 100 <= value < 1000]
        return result

example_dict = {'a': 150, 'b': 2000, 'c': 305, 'd': 'not a number', 'e': 999}
sorted_list = Sort.sort_dict(example_dict)
print(sorted_list)

