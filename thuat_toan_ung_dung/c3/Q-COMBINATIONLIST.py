n, m, k = [int(i) for i in input().split(' ')]

list_full_num = list(range(1, n+1))

k_factorial = 1
list_factorial = [1]
for i in range(1, m):
    k_factorial*= i
    list_factorial.append(k_factorial)

count = 0
check = False
check_1 = False
res = ''
for m_ in range(m):
    k_ = m - m_ - 1
    k_factorial = list_factorial[k_]

    n_ = len(list_full_num) 
    if n_ == 0:
        check = True
        break

    count_combination = 1
    for num in range(n_- k_ +1, n_+1):
        count_combination*= num
    count_combination/= k_factorial
    
    if check_1:
        check = True
        break

    check_1 = True
    for i in range(len(list_full_num)):
        n_temp = n_ - i
        
        if n_temp < k_:
            check = True
            break

        if n_temp == k_: count_combination = 1
        else:
            count_combination /= n_temp
            count_combination *= (n_temp - k_)

        if count + count_combination >= k:
            res = res + str(list_full_num[i]) +  ' '
            list_full_num = list_full_num[i+1:]
            check_1 = False
            break
        else:
            count += count_combination

    if check: break
    
if check:
    print(-1)
else:
    print(res)