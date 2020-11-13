n = int(input())
num = input()
num = [int(i) for i in num.split(' ')]
res = ''
for i in range(n-1):

    for j in range(n -1, i-1, -1):
        if j == i:
            res = res + '-1 '
            break
        if num[j] < num[i]:
            res = res + str(j - i - 1) + ' '
            break

res = res + '-1'
print(res)
        