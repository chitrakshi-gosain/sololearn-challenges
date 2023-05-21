import re

SIZE = 5

map_2d = re.sub(',', '', input())

start = {
    'level': -1,
    'index': -1
}

end = {
    'level': -1,
    'index': -1
}

start['index'] = map_2d.index('P')
end['index'] = map_2d.index('P', start['index'] + 1)
start['level'], end['level']  = start['index'] // SIZE, end['index'] // SIZE
start['index'], end['index']  = start['index'] % SIZE, end['index'] % SIZE

print((end['level'] - start['level']) + abs(end['index'] - start['index']))

# def naive_solution():
#     def findall(string, pattern):
#         position = string.find(pattern)
#         while position != -1:
#             yield position
#             position = string.find(pattern, position + 1)

#     map_2d = input().split(',')

#     start = {
#         'level': -1,
#         'index': -1
#     }

#     end = {
#         'level': -1,
#         'index': -1
#     }

#     LOOKING_FOR_START = True
#     LOOKING_FOR_END = False

#     CURR_LEVEL = -1
#     for mapx in map_2d:
#         CURR_LEVEL += 1
#         if len(list(findall(mapx, 'P'))) > 1:
#             start['level'] = CURR_LEVEL
#             start['index'] = list(findall(mapx, 'P'))[0]
#             end['level'] = CURR_LEVEL
#             end['index'] = list(findall(mapx, 'P'))[1]
#         else:
#             if mapx.find('P') > -1 and LOOKING_FOR_START:
#                 LOOKING_FOR_START = False
#                 LOOKING_FOR_END = True
#                 start['level'] = CURR_LEVEL
#                 start['index'] = mapx.index('P')
#             elif mapx.find('P') > -1 and LOOKING_FOR_END:
#                 end['level'] = CURR_LEVEL
#                 end['index'] = mapx.index('P')
#             else:
#                 continue

#     print((end['level'] - start['level']) +abs (end['index'] - start['index']))
