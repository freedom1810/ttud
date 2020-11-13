n = int(input())
s = input().split(' ')

for i in range(n):
    s[i] = int(s[i])

s.sort()
for i in range(n):
    s[i] = str(s[i])

print(' '.join(s))