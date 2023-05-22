from functools import reduce

def change_case(camel_string):
    return reduce(
        lambda x, y: x + ("_" if y.isupper() else "") + y, camel_string
    ).casefold()

print(change_case(input()))