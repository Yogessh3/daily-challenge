#O(N) Time Complexity / O(1) Space Complexity
def find_num(arr):
    for i in range(len(arr)):
        if(arr[abs(arr[i])-1]>=0):
            arr[abs(arr[i])-1]=-arr[abs(arr[i])-1]
        else:
            print(abs(arr[i]),end=" ")
    print()
    for i in range(len(arr)):
        if(arr[i]>0):
            print(i+1,end=" ")
array=[1,2,2,3,5]
find_num(array)

    
