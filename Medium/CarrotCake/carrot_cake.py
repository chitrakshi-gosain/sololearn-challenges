CARROTS_FOR_CAKE = 7

count_carrots, count_boxes = int(input()), int(input())

carrots_left = count_carrots % count_boxes

if carrots_left < CARROTS_FOR_CAKE:
    print(f'I need to buy {7 - carrots_left} more')
else:
    print('Cake Time')
