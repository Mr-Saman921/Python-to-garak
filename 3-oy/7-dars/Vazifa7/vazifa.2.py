class TupleSort:

    @staticmethod
    def sort_tuple(tuple1, tuple2):
        assert isinstance(tuple1, tuple) and isinstance(tuple2, tuple), "Both arguments must be tuples"
        common_elements = list(set(tuple1) & set(tuple2))
        return common_elements

tuple1 = (19, 17, 13, 2, 9)
tuple2 = (7, 8, 15, 19, 13)
common_list = TupleSort.sort_tuple(tuple1, tuple2)
print(common_list)
