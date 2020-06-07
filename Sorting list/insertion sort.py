def insertionSort(a):
    for i in range(1,len(a)):
        j=i-1
        key=a[i]
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j-=1
            print(a)
        a[j+1]=key
a=[1,3,5,6,4,2]
insertionSort(a)
print(a)
