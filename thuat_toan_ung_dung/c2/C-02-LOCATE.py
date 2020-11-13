# import time


t = int(input())
# tic = time.time()

for _ in range(t):
    
    l , c = [int(i) for i in input().split()]

    list_nghi_ngo = []
    map_1 = [] 
    for index_l in range(l):
        map_1.append([int(i) for i in input().split()])
        
        for index_c in range(c):
            if map_1[index_l][index_c] == 1:
 
                list_nghi_ngo.append([index_l, index_c])
 
    map_2 = [] 
    list_nghi_ngo_2 = []
    for index_l in range(l):
        map_2.append([int(i) for i in input().split()])
        for index_c in range(c):
            if map_2[index_l][index_c] == 1:
 
                list_nghi_ngo_2.append([index_l, index_c])

    max_res = 12
    dict_res = {}
    for p1 in list_nghi_ngo:
        for p2 in list_nghi_ngo_2:
            key = "{}_{}".format(p1[0] - p2[0], p1[1] - p2[1])
            # print(key)
            if key not in dict_res:
                dict_res[key] = 1
            else:
                dict_res[key] += 1
    
    for value in dict_res.values():
        max_res = max(max_res, value)
    print(max_res)

# print('time : {}'.format(time.time() - tic))