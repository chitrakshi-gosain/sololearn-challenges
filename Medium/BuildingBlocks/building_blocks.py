STUDENTS = 15

BLOCKS = {
    'blue': 0,
    'red': 0,
    'green': 0,
    'yellow': 0
}

TOTAL = 0
for block in BLOCKS:
    BLOCKS[block] = int(input())
    TOTAL += BLOCKS[block]
    BLOCKS[block] //= STUDENTS

print(TOTAL - sum(BLOCKS.values()) * 15)