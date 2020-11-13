n = int(input())


for i in range(n):
    s = input()
    x = len(s)
    if x <= 10:
        print(s)
    else:
        print('{}{}{}'.format(s[0], x - 2, s[-1]))
