#It is an methadology where we can restrict the access to methods and variables
#To prevent the data access of the class from outside or same class , is known as encapsulation
#It protects the internal data of class from unauthorised access and modification

class Employee:
    def __init__(self,emp_id , emp_name,emp_salary):
        self._emp_id = emp_id
        self._emp_name=emp_name
        self._emp_salary=emp_salary
    
    def get_user_details(self):
        """ Get Emplyoee details"""
        return f'ID:{self._emp_id} , Name: {self._emp_name} , Salary : {self._emp_salary}'

    def increase_salary(self,amount):
        if amount>0:
            self._emp_salary = amount
        else:
            print('Invalid amount')
    def change_name(self,new_name):
        """Chnaging employee name"""
        self._emp_name = new_name
emp1 = Employee(101,'Bhavesh',200000)
emp2 = Employee(102,'Sharma',300000)
print(emp1.get_user_details())
emp1.increase_salary(2000)
print(emp1.get_user_details())        
emp1.change_name("Sexxy1")
print(emp1.get_user_details())    
    
    


