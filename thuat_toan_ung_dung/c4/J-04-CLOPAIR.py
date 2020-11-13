n = int(input())

list_point = []
for i in range(n):
    list_point.append([int(i) for i in input().split(' ')])

def euclid_dis(x, y):
    return (x[0] - y[0])**2 + (x[1] - y[1])**2
    
p1 = None
p2 = None

res = 1000000000000000
for i in range(n):
    for j in range(i+1, n):
        # print(i, j , list_point[i], list_point[j])
        if res > euclid_dis(list_point[i], list_point[j]):
            res = euclid_dis(list_point[i], list_point[j])
            p1 = i 
            p2 = j 
print(p1, p2 , '{:.6f}'.format(round(res**(1/2), 6)))