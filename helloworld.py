# Basic python
# 
# comments
'''
multiples lines comments
'''

"""
also multiples lines comments
"""

#!
print('Hello, world!')

#variables 
greet = 'Hello'

# access character from 1st index to 3rd index
print(greet[1:4])  # "ell"


x = 5
print(type(x))

print(greet[1])
print(len(greet))

#list
lista = ["banana","laranja","maça"]

#list size
print (len(lista))

print(lista)

#tuplos
tuplo1 = ("banana","laranja","maça")
print (tuplo1)
print (len(tuplo1))

#sets sem ordem e sem poder ter duplicados ou seja item repetidos são ignorados
set = {"banana","laranja","maça","maça"}
print (set)
print (len(set))

#dicionarios tb não permite duplicados
dictionary = {
"marca" : "Ford",
"modelo" : "focus",
"ano" : "2010",
"matricula" : "a7-34-fg"
}
print(dictionary)
print(len(dictionary))

print(dictionary["marca"])

#conditions
a = 100
b =  100

if a > b:
    print("a maior que b")
elif a == b:
    print("a igual a b")
else:
    
    print("b maior que a")

#while loop
i = 1

while (i <= 6):
    print(i)
    i += 1
    # condition option to break the cicle
    if (i == 5):
        break

#for loop

fruta = ["banana","laranja","maça"]

for x in fruta:
    print(x)
    #hipotese de quando acabar a interação
else:
    print("I'm done!")

#iteracao em string
for x in "banana":
    print(x)

for x in fruta:
    print(x)
    if (x == "banana"):
        break

#funtions
def funcao():
    print("sou uma função")

funcao()

# function with arguments
def funcaonome(nome):
    print(nome)

funcaonome("luis")

#objets
class minhaclass():
    x = 5

new = minhaclass()

print(new.x)