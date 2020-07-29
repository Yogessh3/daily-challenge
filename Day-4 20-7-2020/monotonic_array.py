#O(N) Time Complexity / O(1) Space Complexity
def isMonotonic(array):
    isNonIncreasing=True
    isNonDecreasing=True
    for i in range(1,len(array)):
        if(array[i-1]<array[i]):
            isNonIncreasing=False
        elif(array[i-1]>array[i]):
            isNonDecreasing=False
    print(isNonDecreasing)
    print(isNonIncreasing)
    return isNonIncreasing or isNonDecreasing
array=[-1,-5,-10,-1100,-1100,-1101,-1102,-9001]
print(isMonotonic(array))
