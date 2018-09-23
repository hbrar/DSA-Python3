import time
from Implementation import iSort

s =  time.time()
iSort(list(range(10000,0,-1)))
print(time.time() - s)
