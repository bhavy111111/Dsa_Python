L=[]

for i in range(1,11):
    L.append(i)

print(L)

## With the help of list comprehension

a = [x for x in range(1,11)]
print(a)

#Scalar Multiplication

v=[2,3,4]
s=-3
l=[]
for i in v:
    l.append(i*s)
print(l)

#List Comprehension
j=[i*s for i in v]
print(j) 

#- Print the number from 1 to 50 which are divisible by 5

a = [i for i in range(1,51) if i%5==0]


#- languages= ['java','python','php']

f = [language for language in languages if languages.startswith('p') ]