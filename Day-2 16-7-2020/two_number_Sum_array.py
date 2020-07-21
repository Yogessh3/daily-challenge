#O(N log N) Time Complexity / O(1) Space Complexity
def two_number_sum(array,targetsum):
    array.sort()
    left=0
    right=len(array)-1
    while(left<right):
        currentsum=array[left]+array[right]
        if(currentsum==targetsum):
            return [array[left],array[right]]
        elif(currentsum<targetsum):
            left+=1
        else:
            right-=1
    return []
array=[1,8,-4,-1,9,0,5]
target=14
print(two_number_sum(array,target))
