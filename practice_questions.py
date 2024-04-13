# import time 
# def timer(func):
#     def wrapper(*args):
#         start = time.time()
#         print(start)
#         func(*args)
#         print('Time taken by every function',func.__name__,time.time()-start,'secs')
#     return wrapper
# @timer
# def display():
#     print('Hey this is bhavesh')
# @timer
# def square(num):
#     time.sleep(2)
#     return num*2
    
# display()
# square(3)

# class Parent:
#     def __init__(self,num):
#         self.__num=num

#     def get_num(self):
#         return self.__num
# class Child(Parent):
#     def __init__(self,val,num):
#         self.__val = val
#     def get_val(self):
#         return self.__val
# c = Child(100,10)
# c.get_num('Parent insdie constructor',c.get_num())
class Shape:
    def area(self,radius):
        return 3.14*radius*radius
    def area(self,l,b):
        return l*b

s= Shape()
#s.area(2) #Error
print(s.area(3,4))

class Phone():
    def __init__(self,price,name,brand):
        self.price=price
        self.name=name
        self.brand=brand
    
    def buy():
        print('Please Buy phone from parent class')
class SmartPhone(Phone):
    def __init__(self,price,name,brand,os,ram,cpu):
        super().__init__(price,brand,name)
        self.os=os
        self.ram=ram
        self.cpu=cpu
    def bought():
        print('Smartphone has been bought')

s = SmartPhone(2000,'Apple','abc','Oxygen',12,8)
print(s.os)
print(s.brand)