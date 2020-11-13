n = int(input())

for i in range(n):
    s = input()
    x = []
    check = False
    for i in s:
        if i in '([{':
            x.append(i)
        if i in ')]}':
            if len(x) == 0:
                check = True
                break
            t = x.pop()

            # print('t {} i {}'.format(t== '}', i != '{'))

            if t == '(':
                if i != ')':
                    check = True
                    break
            if t == '[':
                if i != ']':
                    check = True
                    break
            if t == '{':
                if i != '}':
                    check = True
                    break
    
    if len(x) > 0 or check:
        
        print(0)
    else:
        print(1)