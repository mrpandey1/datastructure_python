import timeit
def mergesort(arr):
    if len(arr) >1: 
        mid = len(arr)//2
        L = arr[:mid]  
        R = arr[mid:]
        mergesort(L)
        mergesort(R) 
        i = j = k = 0
        while i<len(L) and j<len(R):
            if L[i]<R[k]:
                arr[i]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            k+=1
            j+=1
a=[4,5,2,1,4,1]
starttime = timeit.default_timer()
print("The start time is :",starttime)
mergesort(a)
print("The time difference is :", timeit.default_timer() - starttime)
print(a)
