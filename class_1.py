# #1. Decorators :- Decorator in python is  a function that takes another function as an input , addd some decoration anad returns to it

# def mydecorator(func):
#     def wrapper():
#         print('++++')
#         #print('Hello')
#         func()
#     return wrapper

# @mydecorator
# def hello():
#     print('Hello')

# h = hello()
# print(h)

# import time
# def timer(func):
#     def wrapper(*args):
#         print('Time taken')
#         start=time.time()
#         func(*args)
#         print('Time Taken',func.__name__,time.time()-start,'secs')
#     return wrapper
# @timer
# def hello():
#     time.sleep(1)
#     print('Helo this is bhavehs')
# @timer
# def display(num):
#     time.sleep(3)
#     return num**2

# h1=hello()
# print(h1)


# d = display(2)
# print(d)

#Generators are the special form of iterators 

L=[i**2 for i in range(1,10)]

import sys
print(sys.getsizeof(L))

x = range(10)
print(sys.getsizeof(x))

#It will take one memory at a time and dump it before getting the second one
def gen_demo():
    yield 'First Comment'
    yield 'Second Comment'
    yield 'Third Comment'
gen = gen_demo()
for i in gen:
    print(i)