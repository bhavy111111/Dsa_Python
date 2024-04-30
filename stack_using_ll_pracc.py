class Node:
    def __init__(self,value):
        self.data = value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
    
    def empty(self):
        return self.top==None
    
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top=new_node
    
    def peek(self):
        if(self.empty()):
            print('Print Stack is Empty')
        else:
            return self.top.data
    def pop(self):
        if(self.empty()):
            print('Stack is empty')
        else:
            data = self.top.data
            self.top = self.top.next
            return data
        
    def reversal(self,text):
        #Hello --> olleh
        s= Stack()
        for i in text:
            s.push(i) # H E L L O
        
        res=''

        while(not s.empty()):
            res = res + s.pop()
        
        print(res)
    
    def text_pattern(self,text,pattern):
        r = Stack()
        u=Stack()

        for i in text:
            u.push(i) #HELLO

        for i in pattern:
            if i == 'u':
                data = u.pop()
                r.push(data)
            
            else:
                data = r.pop()
                u.push(data)
            res=''
            while( not u.empty()):
                res = u.pop() + res
            
            print(res)
            


    
    def traverse(self):
        temp = self.top
        while temp!=None:
            print(temp.data)
            temp=temp.next
        
s1 =Stack()
'''
s1.push(1)
s1.push(2)
s1.push(3)
s1.push(4)
s1.push(5)
#s1.pop()
'''
s1.reversal('HELLO')
s1.traverse()
#s1.peek()

