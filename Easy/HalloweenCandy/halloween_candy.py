from math import ceil

houses_count = int(input())
DOLLAR_PROBABILITY = 2

print(ceil((DOLLAR_PROBABILITY / houses_count) * 100))
