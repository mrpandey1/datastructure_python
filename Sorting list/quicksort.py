import timeit
def quicksort(a,l,h):
    if l<h:
        pivot=l
        i=l
        j=h
        while i<j:
            while a[i]<=a[pivot] and i<h:
                i+=1
            while a[j]>a[pivot]:
                j-=1
            if i<j:
                a[i],a[j]=a[j],a[i]
        a[pivot],a[j]=a[j],a[pivot]
        quicksort(a,l,j-1)
        quicksort(a,j+1,h)
a=[4,5,2,1,4,1]
starttime = timeit.default_timer()
print("The start time is :",starttime)
quicksort(a,0,len(a)-1)
print("The time difference is :", timeit.default_timer() - starttime)
print(a)
