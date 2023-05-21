CAP = 20

prices_euro = [float(price) for price in input().split(' ')]

for item in prices_euro:
    if item * 1.1 > CAP:
        print('Back to the store')
        break
else:
    print('On to the terminal')
