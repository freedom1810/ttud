n = int(input())
binary_string = list(input())
# print(binary_string)
if '0' not in binary_string: print(-1)
else:
    temp = 1
    for i in range(n - 1, -1 , -1):
        if temp == 0:
            break
        if temp == 1:
            if binary_string[i] == '1':
                binary_string[i] = '0'
            else:
                binary_string[i] = '1'
                temp = 0
    print(''.join(binary_string))