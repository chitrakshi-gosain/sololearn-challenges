signs = []

for sign_index in range(0,4):
    signs.append(input())

for sign in signs:
    if sign == sign[::-1]:
        print('Open')
        break
else:
    print('Trash')
