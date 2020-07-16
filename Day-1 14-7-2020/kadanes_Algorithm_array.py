#O(N) Time Complexity / O(1) Space Complexity
#Applications: Maximum/Minimum sum in a subarray
def kadanes_Algorithm(array):
    maxEndingHere=array[0]
    maxsoFar=array[0]
    for i in range(1,len(array)):
        maxEndingHere=max(array[i],maxEndingHere+array[i])
        maxsoFar=max(maxEndingHere,maxsoFar)
    return maxsoFar
array=[-2,3,7,-8,6,10]
print(kadanes_Algorithm(array))
'''
maxEndingHere=max(3,1)=3
maxsoFar=max(3,-2)=3
maxEndingHere=max(7,10)=10
maxsoFar=max(10,3)=10
maxEndingHere=max(-8,-8+10)=2
maxsoFar=max(10,2)=10
maxEndingHere=max(6,6+2)=8
maxsoFar=max(10,8)=10
maxEndingHere=max(10,10+8)=18
maxsoFar=max(18,10)=18
'''
