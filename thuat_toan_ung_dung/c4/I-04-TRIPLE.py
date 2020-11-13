from itertools import combinations 
n, k = [int(i) for i in input().split(' ')]
list_num = [int(i) for i in input().split(' ')]

check = [0] * (10**5 + 1)
check[list_num[0]] = 1
res = 0
for i in range(1, len(list_num)):
    for j in range(i+1, len(list_num)):
        if check[k - list_num[i] - list_num[j]] > 0:
            res += check[k - list_num[i] - list_num[j]] 
    check[list_num[i]] += 1

print(res)

