def findall(string, pattern):
    position = string.find(pattern)
    while position != -1:
        yield position
        position = string.find(pattern, position + 1)

casino_layout = input()

money_pos = casino_layout.index('$')
guard_pos = [g_pos for g_pos in findall(casino_layout, 'G')]
thief_pos = casino_layout.index('T')

for g_pos in guard_pos:
    if (thief_pos < g_pos < money_pos) or (thief_pos > g_pos > money_pos):
        print('quiet')
        break
else:
    print('ALARM')
