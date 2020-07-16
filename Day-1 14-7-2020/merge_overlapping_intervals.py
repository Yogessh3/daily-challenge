#O(n Log n) Time Complexity (Traversal-n & sorting-n Log n)
#O(N) Space Complexity
def merge_intervals(array):
    array.sort(key=lambda x:x[0])
    stack=[array[0]]
    for i in range(1,len(array)):
        top=stack[-1]
        if(top[1]<array[i][0]):
            stack.append(array[i])
        elif(top[1]<array[i][1]):
            top[1]=array[i][1]
            stack.pop()
            stack.append(top)
    return stack
intervals=[[1,3],[2,4],[5,7],[6,8]]
merged_interval=merge_intervals(intervals)
for i in merged_interval:
    print(i,end=" ")

'''
top=[1,3]
3<2
3<4
top=[1,4]
stack=[[1,3]]
stack=[]
stack=[[1,4]]
top=[1,4]
4<5
stack=[[1,4],[5,7]]
top=[5,7]
7<6
7<8
top=[5,8]
stack=[[1,4],[5,8]]
'''
