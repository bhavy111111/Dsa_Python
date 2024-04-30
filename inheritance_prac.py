class User:
    def __init__(self):
        self.name='Bhavesh'
    def login(self):
        print('login')
class Student(User):
    def display(self):
        print('Display')

s= Student()
s.login()
print(s.name)

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

s1 = SmartPhone(2000,'Iphone','Apple')
print(s1.buy())

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




###Polymorphism

# class amazon:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def info(self):
#         print("This is product and am class is invoked. The name is {self.name}. This costs {self.price} rupees.")
# class flipkart:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def info(self):
#         print("This is product and fli class is invoked. The name is {self.name}. This costs {self.price} rupees.")
# FLP = flipkart("Iphone", 2.5)
# AMZ = amazon("Iphone", 4)
# for product1 in (FLP, AMZ):
#     product1.info()


class Amazon:
    def __init__(self,price,name):
        self.price =price
        self.name=name
    def info(self):
        print('The name of product of amazon',self.name)
class Flipkart:
    def __init__(self,price,name):
        self.price=price
        self.name=name
    def info(self):
        print('The name of the product of flipkart',self.name)
a=Amazon(200,'Belt')
f = Flipkart(400,'Toy')

for i in (a,f):
    print(i.info())

