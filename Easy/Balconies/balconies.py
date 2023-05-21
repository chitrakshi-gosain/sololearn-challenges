[apartment_a_h, apartment_a_w] = [int(dimension) for dimension in input().split(',')]
[apartment_b_h, apartment_b_w] = [int(dimension) for dimension in input().split(',')]

print('Apartment', end= ' ')
if apartment_a_h * apartment_a_w > apartment_b_h * apartment_b_w:
    print('A')
else:
    print('B')
