points_scored, tickets_req = int(input()), int(input())

if points_scored // 12 >= tickets_req:
    print('Buy it!')
else:
    print('Try again')
