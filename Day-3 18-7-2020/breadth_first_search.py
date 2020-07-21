#O(v + e) Time Complexity / O(V) Space Complexity
class Node:
    def __init__(self,name):
        self.name=name
        self.children=[]
    def add_child(self,name):
        self.children.append(Node(name))
    def breadth_first_search(self,array):
        queue=[self]
        while(len(queue)>0):
            current=queue.pop(0)
            array.append(current.name)
            print(current.name,*current.children)
            for child in current.children:
                queue.append(child)
        return array
result=[]
test1=Node("A")
test1.add_child("B")
test1.add_child("C")
test1.children[1].add_child("D")
print(test1.breadth_first_search(result))
