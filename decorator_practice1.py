# def mydecorator(func):
#     def wrapper():
#         print(')((((()))))')
#         func()
#         print('*')
#     return wrapper
# @mydecorator
# def hello():
#     print('Hey Bhavesh this side')

# def display():
#     print('Hello muskan hot girl')
# #a = mydecorator(hello)
# print(hello())
# #b=mydecorator(display)
# #print(type(a))
# #print(a())
# #print(b())


# #WAP TO CALUCULATE EXECUTION TIME OF ANY FUNCTION USING DECORATOR
# import time
# def timer(func):
#     def wrapper():
#         print('Time taken')
#         start = time.time()
#         func()
#         print('Time taken',func.__name__,time.time()-start,'secs')
#     return wrapper
# @timer
# def hello():
#     print('hello world')
#     time.sleep(2)
# @timer
# def bhavesh():
#     print('Hey bhavesh')
#     time.sleep(4)

# a = hello()
# print(a)
# # b=bhavesh()

# print(b)

# #One problem decorators are not generic if we want to make them generic , we have to use the functionality of args and kwards


# def timer(func):
#     def wrapper(*args):
#         start = time.time()
#         func(*args)
#         print('Time taken',func.__name__(),time.time()-start,'secs')
#     return wrapper

# def square(num):
#     return num **2
import time
def timer(func):
    def wrapper(*args):
        print('Time starts')
        start=time.time()
        func(*args)
        print('Time Taken',func.__name__,time.time() - start,'secs')
    return wrapper

@timer
def hello():
    time.sleep(2)
    print('Hey this side bhavesh')

def display():
    time.sleep(3)
    print("My name is bhavesh after time 2 seconds")
@timer
def sqaure(num):
    time.sleep(3)
    return num*2
a=hello()
print(a)
a1=sqaure(4)
print(a1)

def squareplus(num):
    for i in range(1,num+1):
        yield i**2
gen = squareplus(3)
print(next(gen))
for ij in gen:
    print(ij)