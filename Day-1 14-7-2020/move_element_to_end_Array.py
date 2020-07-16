#O(N) Time Complexity / O(1) Space Complexity
def move_element(array,toMove):
    i=0
    j=len(array)-1
    while(i<j):
        while(i<j and array[j]==toMove):
            j-=1
        if(array[i]==toMove):
            array[i],array[j]=array[j],array[i]
        i+=1
    return array
array=[2,4,3,2,1,1,3,3,4,1,3,2,2]
elmt_to_move=3
print(move_element(array,elmt_to_move))

    
