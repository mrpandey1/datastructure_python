def insertionSort(a):
    for i in range(1,len(a)):
        j=i-1
        key=a[i]
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j-=1
            print(a)
        a[j+1]=key
    return a
def bucketSort(a):
    bucket=[[] for i in range(len(a))]
    for j in a:
        ind=int(10*j)
        bucket[ind].append(j)
    for i in range(len(a)):
        try:
            bucket[i]=insertionSort(bucket[i])
        except:
            pass
    k=0
    for i in range(len(a)):
        for j in range(len(bucket[i])):
            a[k]=bucket[i][j]
            k+=1
    print(a)
bucketSort([.42, .32, .33, .52, .37, .47, .51])

