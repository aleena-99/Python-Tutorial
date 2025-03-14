def separate_types(lst):
    integers = [x for x in lst if isinstance(x, int)]
    floats = [x for x in lst if isinstance(x, float)]
    strings = [x for x in lst if isinstance(x, str)]
    return integers, floats, strings

print(separate_types([1, 2.5, "hello", 3, 4.7, "world"]))
