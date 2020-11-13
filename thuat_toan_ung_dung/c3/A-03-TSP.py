n, m = [int(i) for i in input().split(' ')]

check_visited = [False] * n

map_ = []
for i in range(n):
    x = [0] * n
    map_.append(x)

import sys
min_dis =  sys.maxsize
for _ in range(m):
    src, des , c = [int(i) for i in input().split(' ')]
    map_[src - 1][des - 1] = c
    min_dis = min(min_dis, c)

result = sys.maxsize

def de_quy(current_position, count, cost, n, check_visited):
    global result
    if count == n and map_[current_position][0] > 0:
        result = min(result, cost + map_[current_position][0])

    for i in range(1, n):
        if not check_visited[i] and map_[current_position][i] > 0: 
            check_visited[i] = True
            if cost + (n - count + 1)*min_dis < result:
                de_quy(i, count + 1, cost + map_[current_position][i], n , check_visited)
            check_visited[i] = False

de_quy(0, 1, 0, n, check_visited)
if result != sys.maxsize:
    print(result)
else:
    print(-1)
