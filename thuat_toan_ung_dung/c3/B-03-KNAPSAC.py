n, b = [int(i) for i in input().split(' ')]
objects = []
value = []
cost = []
for j in range(n):
    c, v = [int(i) for i in input().split(' ')]
    value.append(v)
    cost.append(c)



import sys
result = -sys.maxsize
max_value = 0
max_cost = 0
def back_track(i):
    global max_cost, max_value, n, b, result
    if i >= n:
        if result < max_value:
            result = max_value
        return 
    
    back_track(i+1)
    if max_cost + cost[i] <= b:
        max_value += value[i]
        max_cost += cost[i]

        back_track(i+1)
        max_value -= value[i]
        max_cost -= cost[i]

back_track(0)
if result != -sys.maxsize:
    print(result)
else:
    print(2)

