from itertools import permutations 
import math
from sys import setrecursionlimit
setrecursionlimit(100000) 


n, k  = [int(i) for i in input().split()]

temp = 0
factorial = 1
list_factorial = []
check = True
for i in range(1, n+1):
    factorial *= i

    if factorial > k:
        temp = i
        check = False
        break

    list_factorial.append(factorial)

if check:
    print(-1)
else:
    list_num = []

    for i in range(temp):
        list_num.append(n - temp + i + 1)
    for i in range(n-temp):
        print(i+1, end=" ")

    count = 0
    check2= False

    for factorial in list_factorial[::-1]:
        
        for num_index in range(len(list_num)):
            # print('list_num ', list_num)
            if count + (num_index + 1) * factorial >= k:
                print(list_num[num_index], end=" ")
                count += (num_index) * factorial
                del list_num[num_index]
                break

    for num in list_num:
        print(num, end=" ")




