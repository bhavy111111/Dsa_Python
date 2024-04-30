from abc import ABC , abstractmethod

class Car(ABC):
    def push_on(self):
        print('Car is on')
    
    @abstractmethod
    def engine(self):
        pass
class BMW(Car):
    def push_on(self):
        print('Bmw is on')
    def engine(self):
        print('Engine is on')
b = BMW()
b.engine()

#Abstraction means 
# Your car is a great example of abstraction. You can start a car by turning the key or 
# pressing the start button. You don't need to know how the engine is getting started, 
# what all components your car has

#For Abstract Class - There should be one abstract method  and concrete method also
