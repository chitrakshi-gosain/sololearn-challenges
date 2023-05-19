bowls = []

for bowl_index in range(0,6):
    bowls.append(int(input()))

for bowl in bowls:
    if bowl % 3:
        if bowl % 2:
            print('Snap', end = ' ')
        else:
            print('Crackle', end = ' ')
    else:
        print('Pop', end = ' ')
 
