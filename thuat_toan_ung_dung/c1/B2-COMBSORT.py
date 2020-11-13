n = int(input())
x = input().split(' ')
list_num = [float(i) for i in x]

gap = int(n/1.3)

while gap >0:
    for i in range(n - gap):
        if list_num[i]  > list_num[i+gap]:
            list_num[i], list_num[i+gap] = list_num[i+gap], list_num[i]
    gap = int(gap/1.3)

for  i in range(n):
    list_num[i] = str(list_num[i])
print(' '.join(list_num))