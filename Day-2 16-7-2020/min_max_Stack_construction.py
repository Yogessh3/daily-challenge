'''Overall Time Complexity 0(1) (i.e) Get min and max at o(1) Time
Space Complexity O(N) (i.e) Stack memory allocation
'''
class minMaxStack:
    def __init__(self):
        self.stack=[]
        self.minMaxstack=[]
    def peek(self):
        return self.stack[-1]
    def pop(self):
        self.minMaxstack.pop()
        return self.stack.pop()
    def push(self,number):
        newMinMax={"min":number,"max":number}
        if(len(self.minMaxstack)):
            lastMinMax=self.minMaxstack[-1]
            newMinMax["min"]=min(lastMinMax['min'],newMinMax['min'])
            newMinMax["max"]=max(lastMinMax['max'],newMinMax['max'])
        self.minMaxstack.append(newMinMax)
        self.stack.append(number)
    def getMin(self):
        return self.minMaxstack[-1]['min']
    def getMax(self):
        return self.minMaxstack[-1]['max']
m=minMaxStack()
m.push(3)
m.push(5)
m.push(2)
m.pop()
print(m.getMin())
print(m.getMax())
print(m.peek())
    
                            
            
    
