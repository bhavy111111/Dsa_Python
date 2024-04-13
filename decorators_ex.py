#It is a function that receives another function as input and add some functionality(decoration) to and it and returns it.
'''
def my_decorator(func):
    def wrapper():
        print('+++++++++++++++')
        func()
        print('+++++++++++')
    return wrapper

def hello():
    print('hello')

def display():
    print('Hey BHAVESH THIS SIDE')

a = my_decorator(hello)
a()

b = my_decorator(display)
b()
'''
#Better SYntax

'''
def my_decorator(func):
    def wrapper():
        print('+++++++++++++++')
        func()
        print('+++++++++++')
    return wrapper
@my_decorator 
def hello():
    print('hello')

def display():
    print('Hey BHAVESH THIS SIDE')

hello()
'''
#Closure- That inner function can access the variable of parent function from memory after removal of outer function 
'''
def outer():
    a=5
    def inner():
        print(a)
    return inner
a=outer()
a()
'''

#WAP to give execution time to any of the function
'''
import time
def timer(func):
    #def wrapper():
    def wrapper(*args):

        start = time.time()
        print(start)
        func(*args)
        print('Time Taken by',func.__name__,time.time()-start,'secs')
    return wrapper
@timer
def hello():
    print('Hello world ')
    time.sleep(2)
    
@timer
def display():
    print('desplaying soomething')
    time.sleep(4)

@timer
def square(num):
    time.sleep(1)
    return num**2

@timer
def power(a,b):
    print(a**b)

#hello()
#display()
square(2)
power(2,3)
'''


def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(args[0])==data_type:
                func(*args)
            else:
                raise TypeError('This wont work')
        return inner_wrapper
    return outer_wrapper
@sanity_check(int)
def square(num):
    print(num**2)
square('Hello')