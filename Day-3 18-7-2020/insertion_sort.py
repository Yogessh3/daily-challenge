def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i
        while(j>0 and arr[j]<arr[j-1]):
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    return arr
array=[0,5,8,3,4,2]
print(insertion_sort(array))