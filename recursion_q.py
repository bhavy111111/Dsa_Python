#Function call itself - Recursions
#3*4  -  Repeation addition of number -  3+3+3+3 = 12 
def multiplication(a,b):
    result=0
    for i in range(b):
        result=result+a
    print(result)
multiplication(5,6)

# Recursion 

def multi(a,b):
    if b==1:
        return a 
    else:
        return a + multi(a,b-1)
print(multi(3,4))

#Factorial
def fact(number):
    if number ==1:
        return 1
    else:
        return number * fact(number-1)

print(fact(6))

#Palindrome 
#Madam
def palin(text):
    if len(text)==1:
        print('Already a Palindrome')
    else:
        if text[0]==text[-1]:
            palin(text[1:-1])
        else:
            print('Not a Palindrome')
palin('madam')
palin('python')

#Rabbit Problem - Fibonacci series ans

#0 1 2 3 5 8 

def fib(m):
    if m==0 or m==1:
        return 1
    else:
        return fib(m-1)+fib(m-2)
print(fib(12))