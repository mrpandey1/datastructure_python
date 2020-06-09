def oddEvenSort(a,n):
    isSorted=0
    while isSorted==0:
        isSorted=1
        temp=0
        for i in range(1,n-1,2):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                isSorted=0
        for i in range(0,n-1,2):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                isSorted=0
    return
a=[5,4,3,2,1]
oddEvenSort(a,len(a))
print(a)
            
