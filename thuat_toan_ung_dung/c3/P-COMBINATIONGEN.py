n, m = [int(i) for i in input().split(' ')]
list_num = [int(i) for i in input().split(' ')]

list_full_num = list(range(1, n+1))
i = -1
j = -1

count = 0 
while i != -m - 1:
    if list_num[i] == list_full_num[j]:
        i -= 1
        j -= 1
        count += 1
    elif list_num[i] < list_full_num[j]:
        while list_num[i] < list_full_num[j]:
            j -= 1
        list_num[i] = list_full_num[j+1]
        while i != -1:
            if list_num[i] + 1< list_num[i+1] :
                list_num[i+1] = list_num[i] + 1
                i+=1
            else:
                break
        break
if count == m:
    print(-1)
else:
    for num in list_num:
        print(num, end=' ')
    
