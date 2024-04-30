#Interchange first and last element in list 

# #[12,1,2,4]
# #[4,1,2,12]

# def swap_ele(l):

#     l[0],l[-1]=l[-1],l[0]
#     return l

# l=[12,1,2,4]
# print(swap_ele(l))

# #Swap two elements in a list

# def swap_pos(l1 , pos,pos1):
#     l1[pos],l1[pos1] = l1[pos1],l1[pos] 
#     return l1
# l1 = [1,2,3,4,5]
# pos,pos1=1,3
# l1 = swap_pos(l1,1,3)

# #Maximum of two number
# def max(a,b):
#     if a>=b:
#         return a
#     else:
#         return b
    
# print(max(2,3))

# #Minimum of two number

# def min(a,b):
#     if a<=b:
#         return a 
#     else:
#         return b

# #Check if the element exist or not

# test_list=[1,6,3,5,4]

# for i in test_list:
#     if i==3:
#         print('Element exist')

# #Count unique values from list 

# list_1 = [1,2,3,2,4,5]
# l11=[]
# counter=0

# for item in list_1:
#     if item not in l11:
#         counter+=1
#         l11.append(item)
# print('No of unique elements',counter)

# #Reverse all strings in a list

# l09 = ['geeks','for','geeks']

# lk = [i[::-1] for i in l09]
# print('Reversing the string ',lk)

# #
# lkj = ['geeksforgeeks','is','best','for','geeks']
# k=20
# inx=0
# for i in lkj:
#     if inx + len(i) > k:
#         print(k - inx )
#     el

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.n=0
    
    def insert_head(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
        self.n+=1
    def insert_tail(self,value):
        new_node=Node(value)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
        self.n+=1
    
    def middle_insert(self,value,after):
        new_node=Node(value)
        temp=self.head
        while temp!=None:
            if temp.data==after:
                break
            temp = temp.next
        
        if temp is not None:
            new_node.next = temp.next
            temp.next=new_node
            self.n+=1

    def delete_head(self):
        self.head = self.head.next
        self.n-=1
    
    def search(self,item):
        temp=self.head
        pos=0
        while temp!=None:
            if temp.data==item:
                print(pos)
            temp=temp.next
            pos+=1
        return 'Not Found'
    def sum_off_odd_nodes(self):
        temp=self.head
        counter=0
        result=0
        while temp!=None:
            if counter %2!=0:
                result = result + temp.data
            counter+=1
            temp=temp.next
    def remove(self,value):
        temp=self.head
        while temp!=None:
            if temp.data==value:
                break
            temp=temp.next
        
        temp.next=temp
    




    
    def traverse(self):
        temp=self.head
        while temp!=None:
            print(str(temp.data))
            temp=temp.next
            return temp
        