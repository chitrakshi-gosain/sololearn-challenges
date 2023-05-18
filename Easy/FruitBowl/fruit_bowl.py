from math import floor

APPLES_PROBABILITY = 2
APPLES_REQ = 3

fruit_count = int(input())

print(floor(fruit_count/(APPLES_PROBABILITY * APPLES_REQ)))
