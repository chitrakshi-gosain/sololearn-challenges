CONCESSION_ITEMS = {
    'Nachos': 6,
    'Pizza': 6,
    'Cheeseburger': 10,
    'Water': 4,
    'Coke': 5,
}

TAX = 1.07

def main():
    order = input().split(' ')
    total_cost = 0

    for item in order:
        if item in CONCESSION_ITEMS:
            total_cost += CONCESSION_ITEMS[item]
        else:
            total_cost += CONCESSION_ITEMS['Coke']

    total_cost *= 1.07

    print(f'{total_cost:.2f}')

if __name__ == '__main__':
    main()
