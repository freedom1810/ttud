n, b = [int(i) for i in input().split()]
list_num = [int(i) for i in input().split()]


for_ward = []
back_ward = []
max_fw = -1
max_bw = -1


for i in range(n):
    if max_fw - list_num[i] >= b:
        for_ward.append(max_fw - list_num[i])
    else:
        for_ward.append(-1)
    max_fw = max(max_fw, list_num[i])


for i in range(1, n+1):
    if max_bw - list_num[-i] >= b:
        back_ward.append(max_bw - list_num[-i])
    else:
        back_ward.append(-1)
    max_bw = max(max_bw, list_num[-i])

back_ward = back_ward[::-1]
# print(for_ward, back_ward)
res_max = -1
for i in range(1, n-1):
    if back_ward[i] > 0 and for_ward[i] > 0:
        res_max = max(for_ward[i] +  back_ward[i], res_max)
print(res_max)

 


