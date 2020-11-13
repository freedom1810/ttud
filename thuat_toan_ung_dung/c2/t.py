import numpy as np
import time

l = []



for i in range(1000):
    l.append([])
    
    for j in range(1000):
        l[i].append(j)

tic = time.time()        
arr = np.array(l)
print('convert ', time.time() - tic)

tic = time.time()  
for i in range(1000):
    for j in range(1000):
        x = l[i][j]
print('list ', time.time() - tic)


tic = time.time()  
for i in range(1000):
    for j in range(1000):
        x = arr[i][j]
print('numpy array ', time.time() - tic)