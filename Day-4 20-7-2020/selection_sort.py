#O(N^2) Time Complexity / O(1) Space Complexity
def selectionSort(array):
    currentIdx=0
    while(currentIdx<len(array)-1):
        smallestIdx=currentIdx
        for i in range(currentIdx+1,len(array)):
            if(array[smallestIdx]>array[i]):
                smallestIdx=i
        swap(currentIdx,smallestIdx,array)
        currentIdx+=1
    return array
def swap(i,j,array):
    array[i],array[j]=array[j],array[i]
    return array
array=[9,8,66,89,10,-2]
print(selectionSort(array))
