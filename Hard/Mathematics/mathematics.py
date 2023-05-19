target = int(input())
math_expr = input().split(' ')

for expr in math_expr:
    if eval(expr) == target:
        print(f'index {math_expr.index(expr)}')
        break
else:
    print('none')
