def x(d):
    seen_values = {}
    l = []

    for key, value in d.items():
        if value in seen_values:
            if value not in l:
                l.append(value)
        else:
            seen_values[value] = key

    return l

if __name__ == "__main__":
    d = {'a': 1,'b': 2,'c': 3,'d': 2,'e': 1,'f': 4,'g': 3}
    print("Duplicate values:", x(d))
