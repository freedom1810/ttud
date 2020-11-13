n = int(input())
s = input().split(' ')

for i in range(n):
    s[i] = float(s[i])

for i in range(n-1):
    for j in range(n-1):
        if s[j] > s[j+1]:
            s[j], s[j+1] = s[j+1], s[j]


for i in range(n):
    s[i] = str(s[i])

print(' '.join(s))