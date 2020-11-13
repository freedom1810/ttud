a = input().split(' ')
x = int(a[0])
y = int(a[1])


def expmod(x, y):
    if  y == 1:
        return x % (10**9 + 7)
    if y % 2 == 0:
        return expmod(x, y//2)**2 % (10 **9 + 7)
    else:
        return expmod(x, 1) * expmod(x, y//2)**2  % (10 **9 + 7)

print(expmod(x, y))