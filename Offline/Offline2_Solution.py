#Radosław Benedykciński
#algorithm creates a list of the first p elements, sorts it with quicksort then for each element(from 0 to n-p)
#searches it binary and removes it from the array
#then searches binary for a place for the i+p-th element, inserts it and adds to the sum the k-th largest element in the list

#time complexity is O(n*p*logp) and memory complexity is O(plogp)
def binarysearch(T,x,p):    #function returns the index at which element x is located
    left = 0
    right = p-1
    while left <= right:
        i = (left + right)//2
        if T[i] == x:
            return i
        if T[i] < x:
            left = i+1
        else:
            right = i-1
    return i

def binaryplace(T,x,p):     #function returns the index at which element x would be located
    left = 0
    right = p-1
    if x < T[0]:
        return 0
    if x > T[p-1]:
        return p
    while left <= right:
        i = (left + right) // 2
        if T[i-1] <= x and x <= T[i]:
            return i
        if T[i-1] > x:
            right = i-1
        else:
            left = i + 1
    return i

def insertionsort(T,left,right):
    for i in range(left + 1,right + 1):
        key = T[i]
        j = i
        while j > left and key < T[j-1]:
            T[j] = T[j-1]
            j -= 1
        T[j] = key

def partition(T,left,right):
    i = left-1
    for j in range(left,right):
        if T[j] <= T[right]:
            i += 1
            T[i],T[j] = T[j],T[i]
    T[i+1],T[right] = T[right],T[i+1]
    return i+1
def quicksort(T,left,right,p):  #quicksort with insertion sort optimization
    while left<right:
        if right - left <= 392:
            insertionsort(T,left,right)
            break
        else:
            mid = partition(T,left,right)
            quicksort(T, left, mid - 1,p)
            left = mid+1

def ksum(T, k, p):
    n = len(T)
    pmax = T[:p]    #array of first p elements
    quicksort(pmax,0,p-1,p)   #pmax gets quicksorted
    sum = pmax[-k]
    for i in range(1,n-p+1):
        idx = binarysearch(pmax,T[i-1],p)
        pmax.pop(idx)     #removing T[i-1] from pmax
        idx = binaryplace(pmax,T[i+p-1],p-1)
        pmax.insert(idx,T[i+p-1])     #inserting T[i+p-1] into pmax
        sum += pmax[-k]     #adding k-th largest element from pmax to sum
    return sum