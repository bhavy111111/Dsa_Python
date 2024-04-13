class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Stack:

    def __init__(self):
        #top is the head of stack
        self.top=None
    
    def isempty(self):
        return self.top == None
    
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node

    #return top element
    def peek(self):

        if(self.isempty()):
            return 'Stack is Empty'
        else:
            return self.top.data
    
    def pop(self):

        if(self.isempty()):
            return 'Stack is already empty'
        else:
            data = self.top.data
            self.top=self.top.next
            return data

    #Question-1
    def reverse_string(self,text):
        s= Stack()
        for i in text:
            s.push(i) 
        #H E L L O
        res = ''

        while(not s.isempty()):
            res =  res + s.pop() 
        
        print(res)
        #O L L E H
    
    def text_editor(self,text,pattern):
        u=Stack()
        r=Stack()

        #Text will come as H E L L O
        for i in text:
            u.push(i)
        
        for i in pattern:
            if i =='u':
                data = u.pop()
                r.push(data)
            else:
                data = r.pop()
                u.push(data)
        res =''
        while (not u.isempty()):
            res = u.pop()+res
        print(res)

    #Find the celeb
    # l=[
    #     [0,0,1,1],
    #     [0,0,1,0],
    #     [0,0,0,0],
    #     [0,0,1,0]
    # ]

    # def find_celeb(l):
    #     s= Stack()

    #     for i in range(len(l)):
    #         s.push(i)
    #         #Stack - 0 1 2 3
    #     while s.size() >=2:
    #         i = s.pop() #3
    #         j=s.pop()  #2

    #         if l[i][j]==0:
    #             #j is not celebrity
    #             s.push(i)
    #         else:
    #             #i is not celeb
    #             s.push(j)
    #     print(s.traverse())
        
    def isBalanced(self,expr):
        stack=[]

        for char in expr:
            if char in ['(' , '{','[']:
                stack.push(char)
            else:
                #It means it start with closing brackets
                if not stack:
                    return False
                



        







    def traverse(self):
        temp=self.top

        while temp!=None:
            print(temp.data)
            temp=temp.next

s1 = Stack()
#s.isempty()
s1.push(2)
s1.push(3)
s1.push(4)
s1.reverse_string('HELLO')
s1.text_editor('HELLO','uuurr')
print(s1.traverse())






#n = Node(3)
