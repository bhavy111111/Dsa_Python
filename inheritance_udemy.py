#parent
class User:
    def __init__(self):
        self.name='Bhavesh'
    def login(self):
        print('login')
#child
class Student(User):
    # def __init__(self):
    #     self.roll_no=100
    def enroll(self):
        print('enroll')
u=User()
s=Student()
print(s.login())
print(s.name)
#s will go to child constructor , if it wont be there it will go directly to parent constructor



class Phone:
    def __init__(self , price , name , brand):
        print('Inside Parent Constructor')
        self.price=price
        self.name=name
        self.brand=brand
    def buy(self):
        print('Phone has been bought')
    
class SmartPhone(Phone):
    pass
    #In Python if child doesnt have the constuctor it will definetly go to parent constructor for validation
    #In Python , if child has the constructor then parent constructor wont be called
s=SmartPhone(2000,'Iphone12','Apple')
# buy can be bought becoz public method
s.buy()
###################CISCO CONSTRUCTOR QUESTION#############################3
class Parent:
    def __init__(self,num):
        self.__num=num

    def get_num(self):
        return self.__num
class Child(Parent):
    def __init__(self,val,num):
        self.__val = val
    def get_val(self):
        return self.__val
c = Child(100,10)
c.get_num('Parent insdie constructor',c.get_num())
############################################################################


#METHOD OVERIDDING - If the parent and child have same method , always child method will be called 

class Phone:
    def __init__(self , price , name , brand):
        print('Inside Parent Constructor')
        self.price=price
        self.name=name
        self.brand=brand
    def buy(self):
        print('Phone has been bought')
    
class SmartPhone(Phone):
    def buy(self):
        print('Smartphone has been bought')

s = SmartPhone(2000,'Apple','abc')
s.buy()
#ANS- Smartphone has been bought

#METHOD OVERLOADING  -  Its is a concept inside class , where multiple function with same name but output is different

class Shape:
    def area(self,radius):
        return 3.14*radius*radius
    def area(self,l,b):
        return l*b

s= Shape()
s.area(2) #Error
s.area(3,4)
    

####SUPER#####

class Phone:
    def __init__(self , price , name , brand):
        print('Inside Parent Constructor')
        self.price=price
        self.name=name
        self.brand=brand
    def buy(self):
        print('Phone has been bought')
    
class SmartPhone(Phone):

    def __init__(self,price , name , brand , os , ram , camera):
        print('Inside Smartphone class')
        super().__init__(price,name,brand)
        self.os=os
        self.ram=ram
        self.camera=camera

s = SmartPhone(2000,'Apple','abc','Oxygen',12,8)
print(s.os)
print(s.brand)
s.buy()