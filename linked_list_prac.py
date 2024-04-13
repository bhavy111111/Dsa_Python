# class Node:
#     def __init__(self,value):
#         self.data=value
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.n=0
#     #Length Linked List
#     def length(self):
#         return self.n
    
#     def insert_head(self,value):
#         #create new node
#         new_node=Node(value)
#         #insertion
#         new_node.next=self.head
#         self.head=new_node

#         self.n=self.n + 1
    
#     def insert_tail(self,value):
#         new_node=Node(value)

#         temp=self.head
#         while temp.next!=None:
#             temp=temp.next
#         temp.next=new_node
#         self.n =self.n+1
#     def middle_insert(self,value,after):
#         new_node=Node(value)
#         temp=self.head
#         while temp!=None:
#             if temp.data==after:
#                 break
#             temp=temp.next
#         #Casr 1:- You got the search item
#         if temp is not None:
#             new_node.next=temp.next
#             temp.next=new_node
#             self.n+=1
#         else:
#             print('Not found')
#         print(temp.data)

#     def delete_head(self):
#         if self.head==None:
#             print('Empty List')
#         else:
#             self.head=self.head.next
#             self.n=self.n-1

#     def delete_last(self):
#         temp=self.head
#         while temp.next.next!=None:
#             temp=temp.next
#         temp.next=None
#         self.n=self.n-1
    
#     def search(self,item):
#         temp=self.head
#         pos=0
#         while temp!=None:
#             if temp.data==item:
#                 return pos
#             temp=temp.next
#             pos=pos+1
#         return 'Not found'
   
#     def replace_max(self,value):
#         temp=self.head
#         max=temp
#         while temp!=None:
#             if temp.data>max.data:
#                 max=temp
#             temp=temp.next
#         max=value
#     def sum_odd_nodes(self):
#         temp=self.head
#         counter=0
#         result=0

#         while temp!=None:
#             if counter%2!=0:
#                 result+=temp.data
#             temp=temp.next
#             counter+=1
#         print(result)


#     def change_sentence(self):
#         temp=self.head

#         while temp!=None:
#             if temp.data=='/' or temp.data=='*':
#                 temp.data=' '
#             if temp.next.data=='/' or temp.next.data=='*':
#                 temp.next.next.data=temp.next.next.data.upper()
#                 temp.next=temp.next.next
        
#         temp=temp.next
        
    
#     def traverse(self):
#         temp=self.head

#         while (temp!=None):
#             print(str(temp.data)+'->')
#             temp=temp.next
#         return temp
# L =LinkedList()
# '''
# L.insert_head(1)
# L.insert_head(2)
# L.insert_head(3)
# L.insert_head(4)
# L.insert_tail(5)
# '''
# #L.middle_insert(6,1)
# #L.delete_last()
# #print(L.search(5))
# #print(L.sum_odd_nodes())
# L.insert_head('T')
# L.insert_head('h')
# L.insert_head('e')
# L.insert_head('/')
# L.insert_head('*')
# L.insert_head('s')
# L.insert_head('k')
# L.insert_head('y')
# L.insert_head('*')
# L.insert_head('i')
# L.insert_head('s')
# L.insert_head('*')
# L.insert_head('/')
# L.insert_head('b')
# L.insert_head('l')
# L.insert_head('u')
# L.insert_head('e')

# print(L.traverse())
# print(L.change_sentence())


class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.n=0
    
    def length(self):
        return self.n
    
    def insert_head(self,value):
        new_node = Node(value)
        new_node.next=self.head
        self.head=new_node

        self.n = self.n + 1
    
    def insert_tail(self,value):
        new_node=Node(value)
        temp=self.head
        while (temp.next!=None):
            temp = temp.next
        temp.next=new_node
        self.n=self.n+1
    
    def insert_mid(self,value,after):
        new_node=Node(value)
        temp=self.head
        while temp!=None:
            if temp.data==after:
                break
            temp=temp.next # Item will be stopped after getting temp
        if temp is not None:
            new_node.next=temp.next
            temp.next=new_node
            self.n = self.n+1
    
    def delete_head(self):
        if self.head==None:
            print('Empty list')
        self.head = self.head.next
        self.n = self.n - 1
    
    def delete_last(self):
        if self.head==None:
            print('Empty List')
        temp=self.head
        while temp.next.next!=None:
            temp=temp.next
        temp.next=1
        self. n = self.n -1
    
    def search(self,item):
        temp=self.head
        pos=0
        while temp!=None:
            if temp.data==item:
                return pos
            temp = temp.next
            pos=pos+1
        return 'Not Found'
    
    def sum_odd_nodes(self):
        temp = self.head
        counter=0
        res=0
        while temp!=None:
            if counter%2!=0:
                res+=temp.data
            counter+=1
            temp=temp.next
        print(res)

    def reversal(self):
        prev_node =None
        current_node=self.head

        while current_node!=None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node=next_node
        self.head=prev_node

    def remove_duplicates(self):
        current = self.head
        while ( current.next):
            if current.data== current.next.data:
                current.next = current.next.next
            else:
                current=current.next
         
    def display(self):
        temp = self.head
        while(temp!=None):
            print(str(temp.data),'->')
            temp=temp.next
        return temp

l1 = LinkedList()
l1.insert_head(1)
l1.insert_head(1)
l1.insert_head(1)
l1.insert_head(2)
l1.insert_head(3)
l1.insert_head(4)
l1.insert_head(5)
l1.insert_tail(10)
l1.insert_tail(11)
l1.insert_mid(88,3)
l1.search(88)
l1.sum_odd_nodes()
#l1.reversal()
#l1.delete_head() #5 will be deleted
#l1.delete_last()
print('--')
l1.remove_duplicates()
l1.display()
