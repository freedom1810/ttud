n, k = [int(i) for i in input().split(' ')]

duong = []
am = []
for i in range(n):
    input_ = [int(i) for i in input().split(' ')]
    if input_[0] < 0: 
        input_[0] = input_[0]*-1
        am.append(input_)
    else:
        duong.append(input_)

duong = sorted(duong, key=lambda x: -x[0])
am = sorted(am , key=lambda x: -x[0])
# print('duong {}'.format(duong))
# print('am {}'.format(am))

res = 0
k_ = k
pos = [0, 0]
while am or pos[1] != 0: 
    if pos[1] == 0 :
        pos = am.pop()
    
    if k_ == k:
        if k_ > pos[1]:
            k_ -= pos[1]
            pos[1] = 0
            if not am:
                res += 2 * pos[0]
        else:
            res += 2 * pos[0] * (pos[1] // k)
            pos[1] = pos[1] % k

    else:
        if k_ > pos[1]:
            k -= pos[1]
            pos[1] = 0
            if not am:
                res += 2 * pos[0]

        else:
            res += 2 * pos[0]
            pos[1] -= k_
            k_ = k

k_ = k
pos = [0, 0]
while duong or pos[1] != 0: 
    if pos[1] == 0 :
        pos = duong.pop()
    
    if k_ == k:
        if k_ > pos[1]:
            k_ -= pos[1]
            pos[1] = 0
            if not duong:
                res += 2 * pos[0]
        else:
            res += 2 * pos[0] * (pos[1] // k)
            pos[1] = pos[1] % k

    else:
        if k_ > pos[1]:
            k -= pos[1]
            pos[1] = 0
            if not duong:
                res += 2 * pos[0]

        else:
            res += 2 * pos[0]
            pos[1] -= k_
            k_ = k= k_
            k_ = k

    # 3 trường hợp 
    # 1 lần đi được 1 điểm , 
    # 1 lần đi được nhiều điểm, 
    # 1 lần k đi điểm nào
print(res)



