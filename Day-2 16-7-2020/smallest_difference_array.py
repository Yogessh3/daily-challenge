'''
Time Complexity O(n log n + m log m) (i.e) To sort 2 arrays
Space Complexity O(1)
'''
def smallest_diff(array1,array2):
    array1.sort()
    array2.sort()
    Idxone=0
    Idxtwo=0
    smallest_diff=float("inf")
    current_diff=float("inf")
    smallpair=[]
    while(Idxone<len(array1) and Idxtwo<len(array2)):
        first_num=array1[Idxone]
        second_num=array2[Idxtwo]
        if(first_num<second_num):
            current_diff=second_num-first_num
            Idxone+=1
        elif(second_num<first_num):
            current_diff=first_num-second_num
            Idxtwo+=1
        else:
            return [first_num,second_num]
        if(smallest_diff>current_diff):
            smallest_diff=current_diff
            smallpair=[first_num,second_num]
    return smallpair
array1=[-1,5,10,20,28,3]
array2=[26,134,135,15,17]
print(smallest_diff(array1,array2))
    
            
            
