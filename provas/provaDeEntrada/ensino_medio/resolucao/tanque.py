c = int(input())
d = int(input())
t = int(input())

gasto = d/c
if gasto <= t:
    print(0.0)
    
if gasto > t:
    print(round(gasto - t, 1))

