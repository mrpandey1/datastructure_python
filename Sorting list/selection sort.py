def selectionSort(a):
    n=len(a)
    for i in range(n):
        for j in range(i+1,n):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
a=[7,6,5,4]
selectionSort(a)
print(a)
