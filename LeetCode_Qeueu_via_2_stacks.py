class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class stack:
    def __init__(self):
        self.top=None
        self.n=0
    
    def empty(self):
        return self.top==None
    def push(self,value):
        new_node = Node(value)

        new_node.next = self.top
        self.top=new_node
        self.n+=1

    def pop(self):


        data = self.top.data
        self.top = self.top.next
        return data
    
    def queue_via_stack(self,value):
        a = stack()
        b=stack()
        def enqeue(value):
            a.push(value)
        
        def deque():
            if(not b.empty()):
                b.pop()
            else:
                if(a.empty()):
                    print('A Stack is empty')
                else:
                    while (not a.empty()):
                        data = a.pop()
                        b.push(data)
                    b.pop()
    
    def traversal(self):
        temp=self.top

        while temp!=None:
            print(str(temp.data),'->')
            temp=temp.next
    
s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.pop()
s.traversal()

