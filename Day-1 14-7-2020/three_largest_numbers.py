#O(N) Time Complexity / O(1) Space Complexity
def find_three_largest(array):
    threeLargest=[None,None,None]
    for num in array:
        update(threeLargest,num)
    return threeLargest
def update(threeLargest,num):
    if(threeLargest[2] is None or num > threeLargest[2]):
        shiftandupdate(threeLargest,num,2)
    elif(threeLargest[1] is None or num > threeLargest[1]):
        shiftandupdate(threeLargest,num,1)
    elif(threeLargest[0] is None or num > threeLargest[0]):
        shiftandupdate(threeLargest,num,0)
def shiftandupdate(threeLargest,num,idx):
    for i in range(idx+1):
        if(i==idx):
            threeLargest[i]=num
        else:
            threeLargest[i]=threeLargest[i+1]
array=[45,7,87,90,54,124,104,115]
print(find_three_largest(array))
