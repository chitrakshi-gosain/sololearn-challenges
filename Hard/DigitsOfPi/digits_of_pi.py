from mpmath import mp

index = int(input())

mp.dps = 1001
print(list(str(mp.pi).split('.')[1])[index - 1])
