#O(N) Time Complexity / O(N) space complexity
def duplicates(array):
    count={}
    for i in range(len(array)):
        if array[i] in count:
            count[array[i]]+=1
        else:
            count[array[i]]=1
    for i in count.keys():
        if(count[i]>1):
            print(i,end=" ")
array=[8,6,2,8,5,5]
duplicates(array)
