n = int(input())
s = input().split(' ')
list_number = []

maxso = 0
maxend = 0
for number in s:
    # n_ = int(number)
    # x = int(number)
    maxend = max(maxend + int(number),  0)
    maxso = max(maxso , maxend)



print(maxso)


