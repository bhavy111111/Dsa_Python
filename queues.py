#FIFO , Just like in a movie theatre

#Insertion always from tail 
#Deletion alwats from head
#Head always front
#Rear always tail

#Insertion - enqueue
#Deletion - dequeue

#Why we use two pointer in queue because queue is FIFO ( First In First Out) , Insertion will be from tail side , So time complexity will
# be bigger o(n) . Thats we are using two pointer approach

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class queue:
    
    def __init__(self):
        self.front = None
        self.rear=None
        self.n=0
    def enequeu(self,value):
        #Insertion from tail
        new_node = Node(value)
        if self.rear ==None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.n = self.n + 1

    def dequeque(self):
        #Deletion from head
        if self.front=='None':
            return 'List is empty'
        else:
            self.front = self.front.next
    
    def empty(self):
        if self.front==None:
            return 'Queue is empty'
    
    def size_of_queue(self):
        #It will identify size of the qeueue
        temp= self.front
        counter=0
        while temp!=None:
            counter+=1
            temp = temp.next
        return counter


    def traversal(self):
        temp = self.front

        while (temp!=None):
            print(temp.data)
            temp = temp.next

q1 = queue()
q1.enequeu(1)
q1.enequeu(2)
q1.enequeu(3)
q1.enequeu(4)
q1.enequeu(5)
q1.enequeu(6)

q1.dequeque()

q1.traversal()

        