import time
from Implementation import mSort

s =  time.time()
mSort(list(range(10000,0,-1)))
print(time.time() - s)
