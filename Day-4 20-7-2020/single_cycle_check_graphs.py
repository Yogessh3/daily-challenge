def hasSingleCycle(array):
    numElementsVisited=0
    currentIdx=0
    while(numElementsVisited<len(array)):
        if(numElementsVisited>0 and currentIdx==0):
            return False
        numElementsVisited+=1
        currentIdx=getCurrentIdx(currentIdx,array)
    return currentIdx==0
def getCurrentIdx(currentIdx,array):
    jump=array[currentIdx]
    nextIdx=(currentIdx+jump)%len(array)
    if(nextIdx>=0):
        return nextIdx
    else:
        return nextIdx+len(array)
array=[2,3,1,-4,-4,2]
print(hasSingleCycle(array))
    
        
