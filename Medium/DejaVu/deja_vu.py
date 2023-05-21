input_str = input()

if len(input_str) == len(set(input_str)):
    print('Unique')
else:
    print('Deja Vu')
