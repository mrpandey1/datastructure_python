def merge(a,low,mid,high):
    i=low
    k=0
    j=mid+1
    temp=[0 for i in range(high+1)]
    while i<=mid and j<=high:
        if a[i]<=a[j]:
            temp[k]=a[i]
            i+=1
        else:
            temp[k]=a[j]
            j+=1
        k+=1
    while i<=mid:
        temp[k]=a[i]
        i+=1
        k+=1
    while j<=high:
        temp[k]=a[j]
        j+=1
        k+=1
    for i in range(low,high+1):
        a[i]=temp[i-low]
def mergeSort(a,i,j):
    if i<j:
        mid=int((i+j)/2)
        mergeSort(a,i,mid)
        mergeSort(a,mid+1,j)
        merge(a,i,mid,j)
a=[-1,-1,-2,-3,4,5]
mergeSort(a,0,len(a)-1)
print(a)
