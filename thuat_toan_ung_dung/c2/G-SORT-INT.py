# 5
# 7 4 1 2 3
n = int(input())
num_str = input().split(' ')
# list_num = [int(num) for num in num_str] 

list_num = list(map(lambda i: int(i), num_str))

list_num.sort()

for i in range(n):
    print(list_num[i], end = ' ')