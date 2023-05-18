from math import ceil

DOLLAR_PROBABILITY = 2

houses_count = int(input())

print(ceil((DOLLAR_PROBABILITY / houses_count) * 100))
