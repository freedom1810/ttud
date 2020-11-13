n = int(input())
s = input().split(' ')
list_number = []

sum_ = 0
for num in s:
    sum_ += int(num)

print(sum_ % (10**9 + 7))
