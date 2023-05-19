paint_colors = int(input())

COSTS = {
    'canvas': 40,
    'paint': 5
}

print(round((COSTS['canvas'] + COSTS['paint'] * paint_colors) * 1.1))
