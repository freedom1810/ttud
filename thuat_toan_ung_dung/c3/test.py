n, m, k = [int(i) for i in input().split(' ')]

# k_factorial = 1
# for i in range(1, k+1):
#     k_factorial *= i

list_full_num = list(range(1, n+1))

count = 0
check = False
for m_ in range(m):
    k_ = m - m_ -1
    k_factorial = 1
    for i in range(1, k_ + 1):
        k_factorial*= i


    for i in range(len(list_full_num)):
        n_ = len(list_full_num) - i - 1
   
        count_combination = 1
        for num in range(n_- k_ +1, n_+1):
            count_combination*= num
        count_combination/= k_factorial

        if count + count_combination >= k:
            print(list_full_num[i], end=' ')
            list_full_num = list_full_num[i+1:]
            break
        else:
            count += count_combination