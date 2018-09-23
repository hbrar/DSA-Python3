# for python 3.5+, use math.inf for lower versions float("inf")
# If you dont want to use infinity as sentinel, then just find the largest element in the array and add one to it

def mSort(A):
    if len(A) == 0:
        return A
    elif len(A) == 1:
        return A
    else:
        m = (len(A)-1)//2 
        L = mSort(A[:m+1])
        # print("Left",L)
        R = mSort(A[m+1:])
        # print("Right",R)
        result = merge(L, R)
        # print("Merged",result)
        return result
    
def merge(L, R):
    L.append(float("inf"))
    R.append(float("inf"))
    i = j = 0
    result = []
    
    while L[i] != float("inf") or R[j] != float("inf"):
        if L[i] <= R [j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1
    return result