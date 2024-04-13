class Person:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def buy(self):
        print('Person has been bought')

p = Person('Bhavesh','Male')
#p is the refrence variable which keeps the address of the object of the class
q=p
print('The name of p is ',p.name)
print('The name of the q is ',q.name)

# p & q are point to same address hence they will have same output

q.name='ankit'
print(q.name)
print(p.name)


class Student:
    def __init__(self, name , gender):
        self.__name=name
        self.gender=gender


h= Student('bhaveshii','female')
h.__name='shivani'
print('Private attribute name of the objects',h.__name)