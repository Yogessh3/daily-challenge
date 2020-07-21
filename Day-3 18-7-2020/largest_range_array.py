def largest_range(array):
    best_range=[]
    longestLength=0
    nums={}
    for num in array:
        nums[num]=True
    for num in array:
        if nums[num]==False:
            continue
        currentLength=1
        left=num-1
        right=num+1
        while left in nums:
            nums[left]=False
            currentLength+=1
            left-=1
        while right in nums:
            nums[right]=False
            currentLength+=1
            right+=1
        if(currentLength>longestLength):
            longestLength=currentLength
            best_range=[left+1,right-1]
    return best_range
array=[0,1,11,12,13,14,9,10,5,6,7,2,3,4]
print(largest_range(array))
