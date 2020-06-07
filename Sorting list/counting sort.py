def countingSort(a):
    size=len(a)
    maxi=max(a)+1
    output=[0]*size
    count=[0]*maxi

    for i in range(0,size):
        count[a[i]]+=1

    for i in range(1,maxi):
        count[i]+=count[i-1]
    count[1:]=count[0:maxi-1]
    count[0]=0
    print(count)
    for i in range(size):
        output[count[a[i]]]=a[i]
        count[a[i]]+=1
    for i in range(size):
        a[i]=output[i]
a=[1,1,1,1,1,1,0,0,0,1]
countingSort(a)
print(a)
