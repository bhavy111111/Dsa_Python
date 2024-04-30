#Single Inheritance



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
s = SmartPhone(2000,'Apple','abc')
print(s.brand)
s.buy()

#Multilevel Inheritance

class Product:
    def review(self):
        print('Product Customer review')

class Phone(Product):
    def __init__(self,price,brand,name):
        print('Inside phone constructor')
        self.__price=price
        self.brand=brand
        self.name=name

    def buy(self):
        print('Buying Phone')
class SmartPhone(Phone):
    pass
s=SmartPhone(2000,'Apple','Iphone12')
s.buy()
s.review()

#Hierarchical 

class Phone(Product):
    def __init__(self,price,brand,name):
        print('Inside phone constructor')
        self.__price=price
        self.brand=brand
        self.name=name
    def buy(self):
        print('Buying a cell phone')
class SmartPhone(Phone):
    pass
class FeaturePhone(Phone):
    pass

f = FeaturePhone(1000,'Samsung','12').buy()


#Diamond Problem

class Phone:
    def __init__(self, price , name, brand):
        self.__price=price
        self.brand=brand
        self.name=name
    
    def buy(self):
        print('Phone has been bought')
class Product:
    def buy(self):
        print('Product has been bought')

#In Java We will get an error becoz of ambuiguity , But in Python We use the concept of Method Resolution Order 
#First Class which is written , that constructor will be callled 
class SmartPhone(Product,Phone):
    pass

s=SmartPhone(2000,'Apple','Iphone12')
s.buy()