import sys
from itertools import permutations 
import math
from sys import setrecursionlimit
setrecursionlimit(100000) 

n = int(input())
list_num = [int(i) for i in input().split(' ')]

temp = -1
list_num2 = []
while list_num:
    if temp < list_num[-1]:
        temp = list_num.pop()
        list_num2.append(temp)
    else:
        break

if len(list_num) == 0:
    print(-1)
else:
    for i in range(len(list_num2)):
        if list_num2[i] > list_num[-1]:
            list_num[-1] , list_num2[i] = list_num2[i] , list_num[-1]

            list_num = list_num + list_num2

            break
    for num in list_num:
        print(num, end=' ')

