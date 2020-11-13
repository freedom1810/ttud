while True:
    inp = input()
    if inp[0] == '0':
        # print('dasda', len(inp))
        break
    
    
    inp = inp.split(' ')
    num = int(inp[0])
    inp = [int(i) for i in inp[1:]]
 
    temp = []
    max_v = 0
    
    for i in range(num):
        s = inp[i]
        if s == 0:
            continue
 
 
 
        for j in range(i+1, num):
            if inp[j] >= inp[i]:
                s += inp[i]
            else:
                break
            
        for j in range(i-1, -1, -1 ):
            if inp[j] >= inp[i]:
                s += inp[i]
            else:
                break
 
        max_v = max(max_v, s)
            
 
 
    print(max_v)  