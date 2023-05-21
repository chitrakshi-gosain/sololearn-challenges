def findall(string, pattern):
    position = string.find(pattern)
    while position != -1:
        yield position
        position = string.find(pattern, position + 1)

map_2d = input().split(',')

start = {
    'level': -1,
    'index': -1
}

end = {
    'level': -1,
    'index': -1
}

LOOKING_FOR_START = True
LOOKING_FOR_END = False

LEVEL = -1
for mapx in map_2d:
    LEVEL += 1
    if len(list(findall(mapx, 'P'))) > 1:
        start['level'] = LEVEL
        start['index'] = list(findall(mapx, 'P'))[0]
        end['level'] = LEVEL
        end['index'] = list(findall(mapx, 'P'))[1]
    else:
        if mapx.find('P') > -1 and LOOKING_FOR_START:
            LOOKING_FOR_START = False
            LOOKING_FOR_END = True
            start['level'] = LEVEL
            start['index'] = mapx.index('P')
        elif mapx.find('P') > -1 and LOOKING_FOR_END:
            end['level'] = LEVEL
            end['index'] = mapx.index('P')
        else:
            continue

print((end['level'] - start['level']) +abs (end['index'] - start['index']))
