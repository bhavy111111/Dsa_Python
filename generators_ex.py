#Python generator are simple way of creating iteratros
#Suppose you want to take out the square btwen 1 se 1 laj
#WHY??
L = [x for x in range(100000)]

#for i in L:
#    print(i**2)

import sys
print(sys.getsizeof(L))


x =  range(100000000000)
print(sys.getsizeof(x))
#Use of range concept:- It will take one memory at a time , before picking 2 one it will dump first from memory

#Simple example of generator
#Generatro func will alway return gen object
def gen_demo():
    yield 'first_statement'
    yield 'second statemet'
    yield 'third statement'

gen=gen_demo()
for i in gen:
    print(i)
#print(next(gen))
#print(next(gen))
#print(next(gen))
#Nomrla have return , they have yiedl
#generator whenever call , it will give gen object 
#Normla function over after done with function , It temporary pause the state and remember the previous state 


def square(num):
    for i in range(1,num+1):
        yield i**2
gen = square(10)
print('1',next(gen))
print('2',next(gen))

for i in gen:
    print(i)


#Generatro expression
    
L = [i**2 for i in range(1,101)]
print(L)

gen1 = (i **2 for i in range(1,101))
print(next(gen1))
print(next(gen1))

for i in gen1:
    print(i)
