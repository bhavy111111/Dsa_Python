class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        #address is a complex - your address , pincode , landmark
        self.address=address
    def print_address(self):
        print(self.address.get_city(),self.address.pin,self.address.state)

class Address:
    def __init__(self,city,pin,state):
        self.__city=city
        self.pin=pin
        self.state=state
    
    def get_city(self):
        return self.__city
add1 = Address('Rohini','110085','Delhi')
cust = Customer('Bhavesh','male',add1)
cust.print_address()
#passing object to class constructor


