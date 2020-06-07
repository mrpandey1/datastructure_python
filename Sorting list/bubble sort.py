def bubblesort(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
a=[7,6,5,4,3,2,9]
bubblesort(a)
print(a)
