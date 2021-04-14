import timeit
def partition(a,l,h):
    pivot=a[l]
    i=l
    j=h
    while i<j:
        while a[i]<=pivot and i<h:
            i+=1
        while a[j]>pivot and j>l:
            j-=1
        if i<j:
            a[i],a[j]=a[j],a[i]
    a[l],a[j]=a[j],a[l]
    return j
def quicksort(a,i,j):
    if i<j:
        k=partition(a,i,j)
        quicksort(a,i,k-1)
        quicksort(a,k+1,j)
a=[6,5,8,9,3,10,15,12,16]
starttime = timeit.default_timer()
print("The start time is :",starttime)
quicksort(a,0,len(a)-1)
print("The time difference is :", timeit.default_timer() - starttime)
print(a)


