#O(N) Time Complexity / O(N) Space Complexity
def isbalanced(array):
    opening="{[("
    closing="}])"
    matching={'}':'{',']':'[',')':'('}
    stack=[]
    for bracket in array:
        if bracket in opening:
            stack.append(bracket)
        elif bracket in closing:
            if len(stack)==0:
                return False
            elif stack[-1]==matching[bracket]:
                stack.pop()
            else:
                return False
    return len(stack)==0
brackets=list(input())
print(isbalanced(brackets))
        
