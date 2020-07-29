#O(N) Time Complexity / O(N) Space Complexity
def shortenPath(path):
    startsWithSlash = path[0]=="/"
    tokens=filter(isImportantToken,path.split("/"))
    stack=[]
    if startsWithSlash:
        stack.append("")
    for token in tokens:
        if(token==".."):
            if(len(stack)==0 or stack[-1]==".."):
                stack.append(token)
            elif(stack[-1]!=""):
                stack.pop()
        else:
            stack.append(token)
    if(len(stack)==1 and stack[0]==""):
        return "/"
    return "/".join(stack)
def isImportantToken(token):
    return len(token)>0 and token!="."
path1="/foo/../test/../test/../foo//bar/./baz"
path2='../../foo'
path3="/../../../../foo"
print(shortenPath(path1))
print(shortenPath(path2))
print(shortenPath(path3))
