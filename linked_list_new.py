class Node:
    def __init__(self,value):
        self.data= value
        self.next=None

class LinkedList:
    def __init__(self):
        #Empty Linked list
        self.head=None
        #n - number of nodes
        self.n=0
    #Length of Linked List
    def __len__(self):
        return self.n
    
    def insert_head(self,value):
        #new node
        new_node=Node(value)
        #create connection
        new_node.next=self.head
        #reassign head
        self.head=new_node
        #increment
        self.n = self.n +1
    def traverse(self):
        temp=self.head
        
        while temp!=None:
            print(str(temp.data) +'->')
            temp=temp.next
        return temp
    
    def insert_tail(self,value):
        new_node=Node(value)
        
        if self.head==None:
            self.head = new_node
            self.n = self.n + 1
            return
        
        temp=self.head
        while (temp.next!=None):
            temp=temp.next
        
        #you are at last node
        temp.next=new_node
        self.n  = self.n +1

    def insert_middle(self,after,value):
        new_node = Node(value)
        temp=self.head
        while(temp!=None):
            if temp.data==after:
                break
            temp=temp.next

        # Case1:- You got the search item
        if temp is not None:
            new_node.next=temp.next
            temp.next=new_node
            self.n =self.n +1
        else:
            print('Not found')

            
        #Case 2: Loop Pura chala -> temp is None
            
        print(temp.data)

    def delete_head(self):
        if self.head==None:
            print('empty list')
        self.head = self.head.next
        self.n = self.n-1

    def delete_tail(self):
        temp=self.head
        while temp.next.next!=None:
            temp=temp.next
        #head ka second last node
        temp.next=None
        self.n = self.n -1 
    def remove(self,value):
        temp = self.head
        while temp.next!=None:
            if temp.next.data==value:
                break
            temp=temp.next

        #item not found
        if temp.next==None:
            return 'not found'
        else:
            temp.next==temp.next.next
    #search by item
    def search(self,item):
        temp=self.head
        pos=0
        while temp!=None:
            if temp.data==item:
                #break
                print('The position lied',pos)
            temp=temp.next
            pos+=1
        return 'Not found'
    
    #search by index position

    def __getitem__(self,index):
        pos=0
        temp=self.head
        while temp!=None:
            if pos==index:
                print('Temp data via index',temp.data)
        temp=temp.next
        pos+=1

    def replace_max(self,value):
        temp=self.head
        max=temp

        while temp!=None:
            if temp.data>max.data:
                max=temp
            temp=temp.next
        max.data=value

    #sum of odd position items sum
    def sum_odd_nodes(self):
        temp=self.head
        counter=0
        result=0
        while temp!=None:
            if counter%2!=0:
                result = result+temp.data
            counter+=1
            temp=temp.next
        print('Odd nodes sum has been printed',result)

    def reverse(self):
        prev_node=None
        curr_node=self.head

        while curr_node!=None:
            next_node=curr_node.next # Will save 4 to the next node
            curr_node.next=prev_node #Break the connection
            prev_node = curr_node
            curr_node = next_node
        self.head=prev_node


        
L= LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
#L.insert_tail(5)
#L.insert_tail(6)
#L.insert_middle(5,100)
#L.delete_tail()

#L.remove(1)
L.search(2)
L.replace_max(21)
L.sum_odd_nodes()
#print(len(L))

print(L.traverse())
    
#node_obj  = Node(1)
#b = Node(2)
#c = Node(3)
'''
node_obj.next=b
b.next=c
print(b.next)
print(node_obj.next)
'''