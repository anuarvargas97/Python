#DATA TYPES
#integers - int - whole numbers: 3, 300, 200
#floating point - float - numbers with a decimal point: 2.4, 4.6, 100.0
#strings - str - ordered sequence of characters: 'hello', 'sammy', '2000'
#booleans - bool - logical value indicating true or false

#DATA STRUCTURES
#lists - list - ordered sequence of objects: [10,'hello',200.3]
#dictionaries - dict - unordered key-value pairs: {'my_key':'value', 'name':'Frank'}
#tuples - tup - ordered inmutable sequence of objects: (10,'hello',200.3)
#sets - set - unordered collection of unique objects: {'a', 'b'}

#METHODS
#.append() #Añade un nuevo elemento al final de la lista.
#.extend() #Añade un grupo de elementos (iterables) al final de la lista.
#.insert(indice, elemento) #Inserta un elemento en una posición concreta de la lista.
#.remove(elemento) #Elimina la primera ocurrencia del elemento en la lista.
#.pop([i]) #Obtiene y elimina el elemento de la lista en la posición i. Si no se especifica, obtiene y elimina el último elemento.
#.clear() #Borra todos los elementos de la lista.
#.index(elemento) #Obtiene el índice de la primera ocurrencia del elemento en la lista. Si el elemento no se encuentra, se lanza la excepción ValueError.
#.count(elemento) #Devuelve el número de ocurrencias del elemento en la lista.
#.sort()	#Ordena los elementos de la lista utilizando el operador <.
#.reverse() #Obtiene los elementos de la lista en orden inverso.
#.copy()	#Devuelve una copia poco profunda de la lista.

#SLICING
#[start:stop:step] - 'start' starts count on 0, 'stop' starts count on 1
#In phrases, blank spaces count

numbers = [1,2,3,4,5,6]
print(numbers[::2])
numbers[3]


print('Anuar \nVargas') #'\n' basically tells python to print the rest of the string in another line


#--------------------------------------------------------------STRINGS--------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#Strings are ordered sequence of characters

my_string = 'abcdefg'
my_string[-1] #This is indexing
my_string[:3] #This is slicing
my_string[2:5]
my_string[::-1] #This is the easiest way to reverse strings (since you can't use 'reverse' built in function)

name = 'Anuar Vargas'
print(name[:7])

print('Anuar \nVargas') #'\n' basically tells python to print the rest of the string in another line

#Immutability
my_name = 'Sam'
my_name[0] = 'P' #We can't change values of strings since they are immutable

#String concatenation
my_name = 'Sam'
last_letters = my_name[1:]
new_name = 'P' + last_letters #Now we are able to change the first letter by concatenating 'P' with the new variable we created earlier
print(new_name)

2+3 #Arithmetic operation 
'2'+'3' #String concatenation

#String methods
#To know the methods available for a variable, just write '.' and a list of them will appear
x = 'Hello World'
x_two = 'Hi this is a list'
x.upper()
x.split()
x.lower()
x_two.split('i')
x.swapcase()

#String formatting for printing
#String interpolation is when you want to 'inject' a variable into your string for printing. We can achive this in two different ways (methods)
#.format()
#f-strings

#.format() syntax -> 'string here {} then also {}'.format('something1','something2')
print('Hi, my name is {} and I live in {}'.format('Alexis','Queretaro'))


#We can also use indexing with .format() or assing key words or variable assignment
print('The {} {} {}'.format('is','quick','fox'))
print('The {2} {0} {1}'.format('is','quick','fox')) #Using indexing
print('The {1} {1} {2}'.format('is','quick','fox'))
print('The {a} {b} {c}'.format(b='is',c='quick',a='fox')) #Variable assignment


#.format() formatting -> {value:width.precisionf}
#In order to use this technique, you need to previously assing a varuable to the format
result = 100/777
result
print('The result was {}'.format(result))
print('The result was {r:1.4f}'.format(r=result))


#¿Qué son las f-string de Python?
#Las f-string se construyen como una cadena de texto normar el Python, pero precedidas de una f o F. Lo que hace que sea posible 
# interpolar código encerrando este en llaves ({}) dentro de la cadena. Obteniendo como resultado una cadena de texto. 

nombre = 'Alexis'
cumpleaños = '20 de Mayo del 97'
datos = f'El cumpleaños de {nombre} es el {cumpleaños}' #f string
print(datos)


nombre = 'Alexis'
cumpleaños = '20 de Mayo del 97'
datos = f'El cumpleaños de {nombre} es el {cumpleaños}' #f string
print('datos is filled with the following information: {}'.format(datos))


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f'My first bicycle was a {bicycles[0].title()}!'
print(message)


#Interpolación de variables
a = 10
b = 20
suma = f'La suma de {a} + {b} es {a+b}'
print(suma)


#Formatos numéricos de las f-string
#f para indicar números decimales
#% para indicar porcentajes
#e para el formato exponencial

number = 0.123456789
print(f'Formatear el valor con cuatro dígitos: {number:.4f}')
print(f'Imprimir el valor como un porcentaje: {number:.2%}')
print(f'Formato exponencial: {number:e}')

#------------------------------------------------------MORE ABOUT STRINGS-----------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#When trying yo change values inside a string, we can do it directly by using indexing and assigning a new value.
#Theres two ways to do it

#Converting it into a list, change the value and then join it again
string = "abracadabra"
string = list(string)
print(string)
string[0] = 'A'
string = ''.join(string)
string

#Or slice the string and join it back
string = "abracadabra"
string = 'A' + string[1:]
string

#Using a for loop, we can change an specific value inside the string using 'replace'
string = "abracadabra"
for i in list(string):
    if i == 'a':
        string = string.replace('a', 'A')   
string

#Using a function
string = "anuaralexisvargasmedina"
def replacing(string):
    for i in list(string):
        if i == 'a':
            string = string.replace('a', 'A')
    return string
replacing(string)


#Changing lower to upper and viceversa
string = "AnUaRaLexIsVarGasMeDinA"
string.swapcase()

    


#For strings '+' means concatenate
#When strings contain numbers, it is still a string
#We can convert numbers in a string into numbers using 'int()'
str1 = 'Hello'
str2 = 'Techiman'
str3 = str1 + str2
print(str3)

str4 = '123'
str5 = str4 + 1 #This won't work bcuz str4 is string type

str5 = int(str4) + 1 #Here, we used int() to convert strings into numbers
print(str5)

fruit = 'apple'
fruit_letter = fruit[0] #This will bring the first letter of the word assigned to 'fruit'
print(fruit_letter)
print(len(fruit)) #The built-in function len() gives us the lenght of a string

for n in 'apple':
    print(n)

#-----------------------------------------------------------------------------------------------------------------------------------
#Looping through strings
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1


fruit_dos = 'cherry'
for letter in fruit_dos:
    print(letter)


#-----------------------------------------------------------------------------------------------------------------------------------
#Looping and counting
word = 'parangaracutirimicuaro'
count = 0
for i in word:
    if i == 'a':
        count = count + 1
print(count)


#-----------------------------------------------------------------------------------------------------------------------------------
#Slicing strings
s = 'Monty Python'
print(s[:5])
print(s[6:])
print(s[:])


#Using in as a logical operator
'nty' in s #This will tell us if 'nty' is insude 's'

s = 'Monty Python'
if 'nty' in s:
    print('Its part of the word!')


#String comparison
s = 'Monty Python'
if s == 'Monty Python':
    print('It is the same!')


#String library - string methods
greet = 'Hello Bob'
print(greet.upper())
print(greet.lower())
print(len(greet))
type(greet)

dir(greet) #dir() is a powerful built in function in Python3, which returns a list of the attributes and methods of any object 
#(say functions , modules, strings, lists, dictionaries etc.)


#Searching a string
s = 'Monty Python'
busqueda = s.find('Pyth')
print(busqueda)


#Search and replace
greet = 'Hello Bob'
new_greet = greet.replace('Bob', 'Techiman')
print(new_greet)

greet = 'Hello Techiman'
greet_t = greet.replace('a', 'x')
print(greet_t)


#Removing whitespaces
#lstrip() and rstrip() remove whitespaces at the left or right
#strip() removes both beginning and ending whitespace
greet = '   Hello Bob   '
print(greet)
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())    


#Prefixes
line = 'Please'
print(line.startswith('P'))
print(line.startswith('p')) #It will be false since python is case sensitive


#Parsing and extracting
data = 'From aa_vargasmedina@tcs.mx.qro Sat Jan 23 22:47:50 2022'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos) #This will bring the index of the first space after '@'
print(sppos)

host2 = data[21:32] #This is another way to print the same result as the previous lines of code
print(host2)

#Syntax for find: find(sub: Text, start: Optional[int]=..., end:
host = data[atpos+1 : sppos] #We add one since we want to start one position after the 'a' character. This is a way to slice
print(host)


#--------------------------------------------------------------LISTS----------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#Lists are ORDERED sequence of objects; can hold a variety of object types. MUTABLE
#They use square brackets [] and commas to separate objects in the list [1,2,3,4,5]
#Lists support indexing and slicing. Lists can be nested and also have a variety of methods 

my_list = ['string', 100, 10.23]
print(my_list)
len(my_list)
my_list[:]
my_list[0]

numb = ['one', 'two', 'three']
numb_two = ['four', 'five', 'six']
new_numb = numb + numb_two #List concatenation

new_numb[0] = 'UNO' #Changing a value of a list using indexing
new_numb.append('SEIS') #append method will add values to the list
new_numb[6] = 'SIETE'
new_numb.pop() #pop method will delete the last element
popped_item = new_numb.pop() #This will save the popped item into the variable
new_numb.pop(2) #Here we popped the second index, so 'three' was removed from the list
print(new_numb)
print(popped_item)

new_list = ['a','e','c','b','d']
new_list.sort()
new_list.reverse() #Reverse method do work with lists, but not with strings
print(new_list)

#What if we want to convert a list of items into one single string?
#We can do it by using the .join() method

greet = ['Hello','World']
new_greet = ' '.join(greet) #Inside quotes, we specify the way we want to separate items in list to become a single string
new_greet

new_greet = '--'.join(greet)
new_greet


#When we use a method, we cannot re assign the values like the example below. What we need to do is the following
new_numbers = [1,3,7,4,2,6,5]
new_numbers_sorted = new_numbers.sort() #This won't print anything since the sort is occuring in place
type(new_numbers_sorted) #This is a NoneType

new_numbers = [1,3,7,4,2,6,5]
new_numbers.sort()
new_numbers_sorted = new_numbers
new_numbers_sorted

#Nested lists
nested_list = [1, 2, [1,3]]
#Get the number '3'
nested_list[2][1] #This will get you the number '3'


#--------------------------------------------------------MORE ABOUT LISTS-----------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#Acciones con listas:
#Crear lista
lst = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
print(lst)

if 'diez' in lst: #'in' se utiliza para comprobar si algun elemento se encuentra dentro de una lista
    print('Uno si está en lst')
else:
    print('No hay ningun elemento de esas caracteristicas')

#Some lists methods
lst.reverse()
lst.extend(['seis', 'siete'])
lst.insert(0, 'cero')
lst.remove('cinco')
lst.clear()
lst.index('dos')
lst.count('cuatro')
lst.sort()
lst.split()

abc = 'Anuar Alexis Vargas Medina'
abc_splitted = abc.split()
print(abc_splitted)
print(len(abc_splitted))
print(abc_splitted[0])
abc_splitted.append('Taurus')
abc_splitted

#You can also specify what delimiter character to use in the splitting
thing = 'first;second;third;fourth'
thing.split(';')

#Double split pattern:
email = 'From anuar.vargas@uaq.qro.mx Mon April 18 22:36:15 2022'
words = email.split()
print(words)
mail = words[1]
print(mail)
pieces = mail.split('@')
print(pieces)
print(pieces[1])

#Built-in functions for lists
nums = [3,41,12,20,18,53,90]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

nombres = ['Vanessa', 'Alejandro', 'Raul']
nombres.sort()
print(nombres)

#Convertir a mayusculas los elementos de una lista
lst =  ['uno', 'dos', 'tres', 'cuatro', 'cinco']
for i in range(len(lst)): #The len() function returns the number of items in an object. 
                          #When the object is a string, the len() function returns the number of characters in the string.
    lst[i] = lst[i].upper()

print(lst)

#Cambiar, extender y eliminar elementos de una lista
lst_1 = ['uno', 'dos', 'tres', 'cuatro', 'cinco']

lst_1[2] = 'Alexis' #Modificar algun valor
print(lst_1)

lst_2 = lst_1 + ['Techisman','Vargas'] #Extender
print(lst_2)

del(lst_2[:2]) #Elimina los elementos elegidos con el slicing

#Contar o encontrar elementos en una lista
example_list = [1,2, 'Alexis',3,4,1,'Vargas',1,5,10,40,100,20,97]

len(example_list) #Con len se contara el numero de elementos en la lista
example_list.index('Alexis') #Con el metodo index, obtendremos la posicion del elemento buscado
example_list.count(1) #Con el metodo count, obtendremos el numero total de veces que se repite cierto elemento
example_list.append('Data Science') #Con append se agregan elementos a la lista
print(example_list)

#-----------------------------------------------------------------------------------------------------------------------------------
#Crear una lista con rango
sequence = list(range(1,11))
print(sequence)
#-----------------------------------------------------------------------------------------------------------------------------------
#Crear una lista con numpy utilizando arange
from cmath import polar
from itertools import permutations
import pwd
from symbol import decorated
from venv import create
import numpy as np
sequence1 = np.arange(1,11)
print(sequence1)
#-----------------------------------------------------------------------------------------------------------------------------------
#Esto genera una iteracion de la lista de elementos en sequence1
for i in sequence1:
    print(i)


#--------------------------------------------------------DICTIONARIES---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#Dictionaries are UNORDERED mappings for storing objects
#Dictionaries use KEY-VALUE pairing
#Key-value pairing allows users to quickly grab objects without needing to know an index location
#Uses curly braces and colons -> {'key1':'value1', 'key2':'value2'}
#Dictionaries cannot be ordered since are mappings and not sequences

#When to use dictionaries or lists:
#Dictionaries: objects retrieved by key name
#Lists: Objects retrieved by location. Ordered sequence can be indexed or sliced

my_dict = {'key1':'value1', 'key2':'value2'}
my_dict
my_dict['key2']


price_lookup = {
    'apple': 2.99,
    'oranges': 1.99,
    'milk': 5.80
}
price_lookup['apple'] #Here we are indexing our dictionary


d = {
    'k1': 123,
    'k2': [0,1,2],
    'k3':{'insideKey':100} #This is a dictionary inside a dictionary
} #This dictionary has multiple data types

d['k2'] 
d['k2'][2] #This will bring the number 2 os the list inside the 'k2' key
d['k3']['insideKey']


#Make the letter 'c' uppercase
d_two = {'k1':['a','b','c']}
my_dict = d_two['k1']
my_letter = my_dict[2]
my_letter.upper()

upper_letter = d_two['k1'][2].upper()
upper_letter

#Add a value into a dictionary
d = {
    'k1':100,
    'k2':200
}
d['k3'] = 300
d #When printing, now dictinary will have k3


#Overwrite a valye
d = {
    'k1':100,
    'k2':200,
    'k3':300
}
d['k3'] = 'Techiman'
d #When printing, k3 value now will be 'Techiman'


#Useful methods for dictionaries
d = {
    'k1':100,
    'k2':200,
    'k3':300
}

d.keys() #This will bring all the keys of the dictionary
d.values() #This will bring all the values of the dictionary
d.items() #This will bring all the items of the dictionary


#---------------------------------------------------MORE ABOUT DICTIONARIES---------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
purse  = dict() #This is the syntax to create an empty dictionary
purse ['money'] = 2000
purse ['candy'] = 'Pulparindo'
purse ['medicine'] = 'Aspirina'
print(purse)
purse['money'] = 1500 #Once we have the data, we can change it by specifying the new value
purse ['money'] = purse['money'] - 500
print(purse['money'])

#Dictionary literals (constants)
#Dictionary literal use curly braces and have a list of key:value pairs

people = [
    {'name':'Alexis', 'last_name':'Vargas', 'age':24, 'city':'Queretaro'},
    {'name':'Alondra', 'last_name':'Rivera', 'age':25, 'city':'Queretaro'},
    {'name':'Alejandro', 'last_name':'Partida', 'age':54, 'city':'Leon'},
]
print(people)


#COUNTING ON DICTIONARIES:
#When we encounter new data, we need to add a new entry in the dictionary and if this is the second or later time that we see
#this value, we simply add one to the count inside the dictionary under that name

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

#'get' method allow us to check if a key is already in the dictionary 
x = counts.get('cwen', 0) #The second parameter assigns a default value in case theres no information
print(x)


#Simplified counting with .get()
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)


#--------------------------------------------------------------TUPLES---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#Tuples are very similar to a lists, they are ORDERED sequence of objects, however there's one key difference, they are IMMUTABLE.
#Once an element is inside a tuple, it can't be reassigned
#Tuples use parenthesis: (1,2,3)
#tuples can also contain different types of objects
#Tuples are very useful when you pass objects into a program and you need to make sure that they wont change. Provides data integrity
#Tuples only have 2 methods available, count and index

t = (1,2,3)
type(t)

tup = (1,2,[1,2])
type(tup)

my_list = [1,2,3]
type(my_list)

len(t)
t = ('one',2,3.01)
t[-1]

t = ('a','a','c','d')
t.count('a')
t.index('d')

t
my_list

t[0] = 'NEW' #TypeError: 'tuple' object does not support item assignment
my_list[0] = 'NEW' #[1, 2, 3] -> ['NEW', 2, 3]


#---------------------------------------------------------------SETS----------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#Sets are UNORDERED collections of UNIQUE elements, this means it can only be one representative of the same object
#sets will print with curly braces, but they are not dictionaries since they are not using key-pairs

my_set = set() #This will start an empty set
my_set
my_set.add(1) #You can only add one item per instruction
my_set.add(2)
my_set.add(2) #This second '2' won't be printed since a number '2' already existed inside that set
set([1,1,2,3])

mylist = [1,1,1,1,1,2,2,2,2,3,3]
set(mylist) #Even if my list contains repeated numbers, when converting it into a set, that will change


#-------------------------------------------------------------BOOLEANS--------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#Booleans are operators that will allow you to convert TRUE or FALSE statements. 
#These are very important when we deal with control flow and logic.
type(True)
type(False)

1 > 2
2 == 2

#Operator	Description	                                                            Example
# ==    If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.
# !=	If values of two operands are not equal, then condition becomes true.	    (a != b) is true.
# >	    If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
# <	    If the value of left operand is less than the value of right operand, then condition becomes true.	    (a < b) is true.
# >=	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	(a >= b) is not true.
# <=	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	    (a <= b) is true.

#Other logical operator: and, or & not
#'and' both conditions need to be true 
#'or' at least one condition need to be true
#'not' will return the opposite boolean

1 < 2 > 3 # -> False

1 < 2 and 2 > 3 
'h' == 'h' and 2 == 2
1 < 2 or 2 > 3 
not 1 == 1 #This would be true, nevertheless we're using 'not' so the display will be 'False'


#-----------------------------------------------------------I/O with Files----------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------

#Search for the document 'InputOutput with basic files' in Anaconda

#---------------------------------------------------IF, ELIF AND ELSE STATEMENTS----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#Here, we'll learn about control flow
#We often, only want certain code to run when a particular condition has been met
#i.e. *if* my dog is hungry, then I will feed the dog
#To control this flow of logic, will use the following key words: if, elif, else

#Syntax of and if statement:
#   if *some condition*:
        #execute some code

#Syntax of and if/else statement:
#   if _some condition_:
#       _execute some code_
#   else:
#       _do something else_

#Syntax of and if/elif/else statement:
#   if _some condition_:
#       _execute some code_
#   elif _some other condition_:
#       _do something different
#   else:
#       _do something else_

if 3>2:
    print('True')


hungry = True
if hungry:
    print('Feed me!')


hungry = False
if hungry:
    print('Feed me!')
else:
    print('Im not hungry, thanks!')


loc = 'NY'
if loc == 'Auto Shop':
    print('Cars are cool!')
elif loc == 'Bank':
    print('Money is cool uwu')
elif loc == 'NY':
    print('Welcome to the jungle!!!')
else:
    print('I dont know much...')


x = 42
if x > 1:
    print(f'{x} is bigger than one')
    if x < 100:
        print('Still bigger than one but lower than 100')
print('Query done')


for i in range(5):
    print(i)
    if i > 2:
        print('Bigger than 2')
    print('Done with', i)
print('All done')

x = 2
if x < 4:
    print('x is smaller than 4')
else:
    print('x is greater or equal than 4')
print('All done')

x = 5
if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
else:
    print('Large')
print('All done')

#Condicional anidado

name = 'Techiman'
age = 17
if name == 'Alexis':
    if age >= 18:
        print('Tu apellido es Vargas y eres mayor de edad')
    else:
        print('Tu apellido es Vargas pero eres menor de edad')
else:
    print('No eres Alexis, intento con el usuario correcto...')
print('Consulta terminada')


#Try and except
rawstr = input('Enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number, please try again')


#-----------------------------------------------------------FOR LOOP----------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#Many objects in python are iterable, meaning we can iterate over every element in the object.
#Such as every element in a list, every character in a string or every key in a dictionary
#Syntax of a for loop:
#   my_iterable = [1,2,3]
#   *for* item_name *in* my_iterable:
#       print(item_name)

my_list = [1,2,3,4,5] #for loop with lists
for i in my_list:
    print('Techiman')


my_list = list(range(11))
for i in my_list:
    print(i)


my_list = list(range(1,11))
for i in my_list:
    #Check if even
    if i % 2 == 0:
        print(i)
    else:
        print('Odd number: {}'.format(i)) # -> print(f''Odd number: {i}')



list_sum = 0
my_list = list(range(1,11))
for i in my_list:
    list_sum = list_sum + i
    print(list_sum)


list_sum = 0
my_list = list(range(1,6))
for i in my_list:
    list_sum = list_sum + i
    print(list_sum)
print(f'The sum of all the values is: {list_sum}')


mylist = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append((x*y))
mylist        


for letter in 'Hello World': #for loop with strings
    print(letter)


tup = (1,2,3) #for loop with tuples
for item in tup:
    print(item)


my_list = [(1,2),(3,4),(5,6),(7,8),(9,10)]
len(my_list)
for i in my_list:
    print(i)


my_list = [(1,2),(3,4),(5,6),(7,8),(9,10)] #Unpacking tuples
for a,b in my_list:
    print(a)


my_list = [(1,2),(3,4),(5,6),(7,8),(9,10)] #Unpacking tuples
for a,b in my_list:
    print(b)


my_list = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in my_list:
    print(a+c)


d = {'k1':1, 'k2':2, 'k3':3} #Looping into dictionaries
for i in d:
    print(i)


d = {'k1':1, 'k2':2, 'k3':3} #Looping into dictionaries
for i in d.items(): #If you want to loop into the actual values of the keys, use 'items' method
    print(i)


d = {'k1':1, 'k2':2, 'k3':3} #Looping into dictionaries
for key,value in d.items(): #If you want to loop into the actual values of the keys, use 'items' method
    print(key)
    print(value)


new_list = []
d = {'k1':1, 'k2':2, 'k3':3} #Looping into dictionaries
for key,value in d.items(): #If you want to loop into the actual values of the keys, use 'items' method
    new_list.append(value)
print(new_list)
new_list.sort() #Since dictionaries aren't sorted, we use this method
list_sorted = new_list
print(list_sorted)


#----------------------------------------------------------WHILE LOOPS--------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#While loops will continue to execute a block of code while some condition remains true
#i.e. while my pool isn't full, keep filling it with water
#Syntax
#   while -some_boolean_condition-:
#       #do something
#   else:
#       #do something else

x = 0
while x < 6:
    print(f'The current number is: {x}')
    x = x + 1 # x += 1 is another way to write it
else:
    print('The value of x is higher or already reached number 5!')


x = 500
while x < 6:
    print(f'The current number is: {x}')
    x = x + 1 # x += 1 is another way to write it
else:
    print('The value of x is higher or already reached number 5!')


#BREAK, CONTINUE AND PASS KEYWORDS
#break -> breaks out of the current closest enclosing loop
#continue -> goes to the top of the closest enclosing loop
#pass -> does nothing at all

x = [1,2,3]
#for i in x:
#Since we have nothing here and the for loop is expecting something to happen, this will throw and error.
#print('End of my script')

#We can fix it by using 'pass'

#Using pass
x = [1,2,3]
for i in x:
    pass
print('End of my script') #Now we'll be able to see this print


#Using continue
my_string = 'alejandra'
for i in my_string:
    if i == 'a':
        continue
    print(i)


#Using break
my_string = 'alejandra'
for i in my_string:
    if i == 'j':
        break
    print(i)

x = 0
while x < 5:
    if x == 4:
        break
    print(f'The current value of x is: {x}')
    x += 1


#-------------------------------------------------MORE ABOUT LOOPS AND ITERATORS----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
n = 5
while n > 0:
    n = n - 1
    print(n)

n = 5
while n > 0:
    print(n)
    n = n - 1

#Breaking out of a loop
while True:
    line = input('> ')
    if line == 'done':
        break #The break statement ends the current loop and jumps to the statement inmediatly following the loop
    print(line)
print('Done!')

#Finishing an iteration with continue
while True:
    line = input('> ')
    if line[0] == '#':
        continue #The continue statement ends the current iteration and jumps to the top of the loop and starts the next iteration
    if line == 'done':
        break
    print(line)
print('Done!')

#Definite loop with for
#This loops are called this way because they execute an exact number of times
#We say 'definite loops iterate through the members of a set'
#Definite loops have explicit iteration variables that change each time through a loop. These iteration variables move through
# the sequence or set
#We can loops through lists of numbers, strings, etc

for i in [5,4,3,2,1]:
    print(i)

for i in range(1,6):
    print(i)

people = ['Alexis', 'Andrea', 'Alondra', 'Sujey', 'Vianey']
for i in people:
    print('Good day! ' + i)
print('Done with names!')

numbers = [5,4,3,2,1]
max(numbers)


largest = -1
print('Before ', largest)
for num in [9,41,12,3,74,15]:
    if num > largest:
        largest = num
    print(largest, num)
print('After ', largest)


#-----------------------------------------------------------------------------------------------------------------------------------
#Counting in a loop
counter = 0 #This is our counter that starts on 0
print('Before', counter)
for i in [9,41,12,3,74,15]: #Here it will start iterating
    counter = counter + 1 #To add up a value in our count, we introduce a sum variable that starts on 0 
    print(counter, i)
print('After:', counter)


#With the counter, we'll be summing up the values
counter = 0 #This is our counter that starts on 0
sum_list = 0
print('Before', sum_list)
for i in [9,41,12,3,74,15]: #Here it will start iterating
    counter = counter + 1 #To add up a value in our count, we introduce a sum variable that starts on 0 
    sum_list = sum_list + i
    print(counter, sum_list)
print('After:', sum_list)


#-----------------------------------------------------------------------------------------------------------------------------------
#Filtering a loop:
for i in [9,41,12,3,74,15]: #Here it will start iterating
    if i >= 15:
        print(i)
print('This are the numbers !')


#-----------------------------------------------------------------------------------------------------------------------------------
#Boolean filter
found = False
for i in [9,41,12,3,74,15]:
    if i == 12:
        found = True #As soon as the condition becomes true, we know we already found the number 12, so afterwards, everything will be true
        break
    print(found, i)
print('Done with it...')


#-----------------------------------------------------------------------------------------------------------------------------------
#Finding the smallest value
#We have a set with different values but we don't really know which of them would be smaller than an arbitrary number that we could
#choose to evaluate with a condition, so we need to use 'none'
#None stands for an empty value, its a constant. Non existance
#'is' operator can be used in logical expressions. There's also 'is not'. Is stronger than '=='
#'is' as an advice, its better to use it only on booleans and non types, so use == for integers, floats and strings

smallest = None
for i in [9,41,12,3,74,15]:
    if smallest is None: 
        smallest = i
    elif i < smallest:
        smallest = i
    print(smallest, i)
print('The smallest number is:', smallest)


#----------------------------------------------------USEFUL OPERATORS IN PYTHON-----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------

#range (start,stop,step)
for i in range(5,11):
    print(i)

for i in range(0,11,2):
    print(i)

range(0,11,2) #This will only get a range operator since it's a generator, if you want to convert it into a list:
list(range(0,11,2))


#enumerate: it returns back some sort of index counter and then the element at the particular iteration
index_count = 0
for i in 'abcde':
    print('At index {}, the letter is {}'.format(index_count,i))
    index_count += 1

index_count = 0
word = 'abcde'
for i in 'word':
    print(word[index_count])
    index_count += 1

word = 'abcde'
for i in enumerate(word):
    print(i) #It will return the values like tuples. If we want to unpack the tuples, let's do the following

word = 'abcde'
for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')


#zip: zips together 2 lists
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]

for i in zip(mylist1,mylist2,mylist3):
    print(i)

#We can also convert the zip into a list
mylist1 = [1,2,3]
mylist2 = ['a','b','c']

list(zip(mylist1,mylist2))


#What happens if one list to zip has more elements than the other ones? It will ignore everything else that's extra
mylist1 = [1,2,3,4,5,6,7,8,9,10]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]

for i in zip(mylist1,mylist2,mylist3):
    print(i)


#in: it helps us in checking if an object is in a list and will return a boolean
'x' in [1,2,3]
'x' in ['x','y','z']
'o' in 'world'
'Techiman' in {'Techiman': 'May 20'}

d = {'Techiman': 'May 20'}
'May 20' in d.values() #'values' is to ask for the existance of values inside a dictionary

d = {'Techiman': 'May 20'}
'May 20' in d.keys()  #'keys' is to ask for the existance of keys inside a dictionary


#min & max
my_list = [1,2,30,500,6000]
min(my_list)
max(my_list)


#random library
from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
mylist

from random import randint
randint(0,100)
myrandom = randint(0,500)
myrandom


#input: this will be used when we ask the user for an input
#NOTE: everything that pass into 'input', turns into strings
result = input('Whats your age? ')
result 
type(result) #When printing, we notice that the outcome is in string format, even if user entered an integer/number
print(int(result)) #Now we turned it into an integer


#-----------------------------------------------------LIST COMPREHENSIONS-----------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
mystring = 'hello'
mylist = []
for i in mystring:
    mylist.append(i)
print(mylist)


mystring = 'hello'
mylist = [i for i in mystring] #This is a list comprehension
mylist

mylist = [i for i in 'word']
mylist

numbers = []
for i in range(1,6):
    numbers.append(i)
print(numbers)

numberstwo = [i for i in range(1,6)]
print(numberstwo)

mylist = [i**2 for i in range(1,6)]
print(mylist)

mylist = [i for i in range(1,11) if i%2 == 0]
print(mylist)

mylist = [i**2 for i in range(1,11) if i%2 == 0]
print(mylist)


celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*i + 32) for i in celcius]
fahrenheit

celcius = [0,10,20,34.5]
fahrenheit = []
for i in celcius:
    fahrenheit.append(((9/5)*i + 32))

print(fahrenheit)


#---------------------------------------------------------FUNCTIONS-----------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#Creating clean repeatable code is a part of becoming an effective programmer. 
#Functions allow us to create code that can be easily executed many times without needing to rewrite the same entire block of code
#'return' keyword is used to send back the result of a function without printing it out.
#'return' allow us to assign the output of the function to a new variable

def thing():
    ''' Docstring goes inside triple quotes, this is used for explanation'''
    print('Hey Techis')
thing() #In order to print the function, you need to invocate it


#Same fuctions written differently and using a parameter
def thing2(name):
    print(f'Hey {name}')
thing2('Techis')

def add_function(num1, num2):
    return num1 + num2 #return doesn't use parethesis
result = add_function(10,20) #Using return, we were able to assing the sum of the function's arguments into the result variable
print(result) #Whenever we want to use the result value (which is 30), we'll just need to call the variable


def even_check (number):
    return number % 2 == 0

even_check(22)


#Given a list of numbers, define a function that squares the numbers and returns them into a list
numeros = [1,2,3,4,5]
def square():
    cuadrado = []
    for i in numeros:
        cuadrado.append(i ** 2)
    return cuadrado
square()


#Given a list of numbers, iterate through them and square them
numeros = [1,2,3,4,5]
for i in numeros:
    print(i**2)


#LOOP THROUGH A LIST AND PRINT 'TRUE' IF ANY EVEN VALUE WAS FOUND, ELSE PRINT 'FALSE'
def even_check_list (number_list):

    for i in number_list:
        if i % 2 == 0:
            return True
        else:
            pass
    return False #We want to FIRST loop all over the list to see if theres a even number, if not found, then print False

even_check_list([1,11,15])




#LOOP THROUGH A LIST AND  GET ALL EVEN NUMBERS INSIDE A LIST CALLED 'EVEN_NUMBERS'.
def even_check_list (number_list):

    even_numbers = [] #placeholder variable

    for i in number_list:
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            pass
    return even_numbers

even_check_list([1,4,6,8,10,11,15])


#Crea una funcion que obtenga el cuadrado de los numeros pares del uno al 20 y agregalo en una lista
#En este ejemplo, la lista con el rango se creara dentro de la funcion, por lo que esta ultima no tendrá parametros
square_numbers = []
def square():
    for i in range(0,6):
        if i % 2 == 0:
            square_numbers.append(i ** 2)
        else:
            pass
    return square_numbers
square()


#Crea una funcion que obtenga el cuadrado de los numeros PARES del 1 al 5 y agregalo en una lista.
#En este ejemplo, ya se tiene una lista dada 'numbers' que contiene del 1 al 5
numbers = list(range(0,6)) #numbers sera nuestra entrada de datos a evaluar con la funcion
squared_numbers = []

def square(lista): #El nombre del parametro es completamente independiente a los valores que se ingresaran a la funcion
    for i in lista: #Dentro de nuestro ciclo for, SI SE TIENE QUE ESCRIBIR EL MISMO NOMBRE DEL PARAMETRO DE LA FUNCION
        if i % 2 == 0:
            squared_numbers.append(i ** 2)
        else:
            pass
    return squared_numbers

square(numbers) #Agregamos nuestros datos a evaluar en la funcion


#Crea una lista con un ciclo for que tenga los cuadrados de los numeros pares y diga 'odd' cuando el numero sea impar
listnums = []
for i in range(0,6):
    if i % 2 == 0:
        listnums.append(i**2)
    else:
        listnums.append('odd')
listnums



#TUPLE UNPACKING WITH FUNCTIONS
#This function will return the employee who has the most worked hours

work_hours = [('Alexis',40),('Alondra',35),('Vianey',60),('Efra',70)] #List with tuples

def employee_check(work_hours): #Here, as the argument, we have our work hour list

    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours: #Here we'll loop through all the list of work_hours to find out who has the more worked hours
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month, current_max) #This will return the tuple with the employee with most working hours

result = employee_check(work_hours) #You can save the result in a variable and then call it
result # -> ('Efra',70)

name, hours = employee_check(work_hours) #Or you can also do tuple unpacking and the print the result sepparately
name # -> 'Efra'
hours # -> 70




#INTERACTIONS BETWEEN FUNCITONS
#Let's create a few functions to mimic the guessing game 'Three cup monte' where you'll have to find out where the ball is within 3 cups
from random import shuffle

mylist = [' ','o',' '] #'o' represents the ball

def shuffle_list(mylist):
    shuffle(mylist)
    
    return mylist

shuffle_list(mylist) #By using the function 'shuffle_list', the ball will take the 3 possible places randomly


#Now let's create a player function where he'll have to guess between 3 possible indexes
def player_guess():
    guess = ''

    while guess not in ['0','1','2']:
        guess = input('Pick a number: 0, 1 or 2 -> ') 
          
    return int(guess) #We have to use 'int' because 'input' always return strings. That's why in the while loop we also use strings

player_guess()


#Finally, we'll create the check function in order to see whether our guess was right or not
def check_guess (mylist, guess):
    if mylist[guess] == 'o':
        print('CORRECT!')
    else:
        print('Wrong guess :(')
        print(f'The correct answer was: {mylist}')


#INITIAL LIST
mylist = [' ','o',' ']

#SHUFFLE LIST
mixed_list = shuffle_list(mylist)

#USER GUESS
guess = player_guess()

#CHECK GUESS
check_guess(mixed_list, guess)




#------------------------------------------------------MORE ABOUT FUNCTIONS-----------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------

#Parameters for fucntions:
#A paramater is a function which we use in the function definition. It is a 'handle' that allows the code in the function 
#to access arguments for a particular function invocation

def greet(lang):
    if lang == 'esp':
        return('hola')
    if lang == 'eng':
        return('hello')
    if lang == 'fr':
        return('bonjour')
greet('esp')

#Usando return
#print() muestra lo que le pidas mostrar (z en el caso de la primera función). La segunda función no tiene print() por tanto no 
# muestra nada, pero tiene un return que devuelve el resultado a la función que la llamó, por lo que esa otra función puede tener 
# el print() necesario. Puede hacer por ejemplo print(suma(3,4))

#Return es más genérico pues la función que llamó puede elegir si quiere mostrar el resultado, o guardarlo para otra cosa como con 
# s = suma(3,4), cosa que la primera función no permite porque no retorna nada.

def suma(x, y):
    z = x + y
    print(z)
suma(3,4)


def suma2(x, y):
    return x + y
print(suma2(3,4))


def suma2(x, y):
    adition = x + y
    return adition
resultado = suma2(3,4)
print(resultado)


def suma2(x, y):
    return x + y
s_7 = suma2(3,4)
print(s_7)


def greet(lang, nambre):
    if lang == 'esp':
        return('hola', nambre)
    if lang == 'eng':
        return('hello', nambre)
    if lang == 'fr':
        return('bonjour', nambre)
greet('fr', 'Techis')


def greet2(lang):
    if lang == 'esp':
        return('hola')
    if lang == 'eng':
        return('hello')
    if lang == 'fr':
        return('bonjour')
Techis_Esp = greet2('esp'), 'Techiman'
print(Techis_Esp)


#Crea una funcion que imprima los numeros pares del 1 al 10
n = 0
def pair_nums ():

    """Creates a function that will display pair numbers in range of 1 to 11""" #This is called docstring
    for n in range(1, 11): #Se utiliza in range para determinar el rango que se evaluara en la funcion
        if (n % 2 == 0):
            print(n)
        print()

pair_nums() #Since this function doesnt need any parameter, you just call it by typing the name with empty parenthesis
    

#-----------------------------------------------------------------------------------------------------------------------------------
#Crea una funcion que acepte un parametro
def greet_username(username): #username es el PARAMETRO de la funcion
    print(f'Hello, {username.title()}!')

greet_username('Techisman') #Techisman es el ARGUMENTO de la funcion


#-----------------------------------------------------------------------------------------------------------------------------------
#Crea una funcion con argumentos posicionales
def describe_pet(animal_type, pet_name):

       """Display information about a pet."""
       print(f"\nI have a {animal_type}.")
       print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('dog', 'Niurka')


#-----------------------------------------------------------------------------------------------------------------------------------
#Keyword Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry') #Al especificar el valor del parametro, no importa el orden
describe_pet(pet_name='harry', animal_type='hamster')


#-----------------------------------------------------------------------------------------------------------------------------------
#Default Values
def describe_pet(pet_name, animal_type='dog'): #Asignamos 'dog' como valor predeterminado
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie') #Al saber que dog es predeterminado, no es necesario especificar el 'animal_type'

#To describe an animal other than a dog, you could use a function call like this:
describe_pet(pet_name='harry', animal_type='hamster') #Al especificar el parametro 'animal_type', python ignorara el valor predeterminado


#Write a function array_oper which accepts two numbers num1, num2 and perform array operations given below:
#Create a 2D array of shape (2,3) having numbers from num1 to num2
#Square each element of y
#Add 5 to each element of resulted array
#Print the new array

#Sample input (1,6)
#Sample output
#   [[6 9 14]
#    [21 30 41]]

import numpy as np

array2d = []
def array_oper(num1,num2):
    for i in range(num1,num1+6):
        array2d.append(i)
    shape = np.reshape(array2d,(2,3))
    skuere = np.square(shape)
    add = skuere + 5
    print(add)
array_oper(1,6)


#---------------------------------------------------------*ARGS, **KWARGS-----------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#When using functions, you can define argument inside them, but when arguments exceed the ones delimited inside the function,
#you'll get an error. That's when we use *args, so you can insert as much arguments as you want.
def suma(a,b):
    return (a+b) * 0.05
suma(100,50)


def suma(a,b):
    return (a+b) * 0.05
suma(100,50,30) # -> TypeError: suma() takes 2 positional arguments but 3 were given


mylist = []
def suma(*args):
    for i in args:
        mylist.append(i)
    print(mylist)
    return sum(args) * 0.05

suma(100,50,30) #Now I can pass in as many arguments as I want



#**kwargs: key word arguments returns a dictionary
def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is: {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc(fruit = 'Mango', veggie = 'Carrot')


#Using args and kwargs together
def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[3], kwargs['actions']))

myfunc(10, 20, 100, 500, animal = 'cats', actions = 'kisses', money = 'dolars')


#Exercise:
#Define a function that takes in a string and returns a matching string where every even letter is uppercase and
#every odd letter is lowercase
def myfunc(x):
    out = []
    for i in range(len(x)):
        if i % 2 == 0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)

myfunc('Alondra')


def animal_crackers(text):
    text.split()
    text_split = text
    return text_split

animal_crackers('Levelheaded Llama')

animal_crackers = 'Levelheaded Llama'
text_split = animal_crackers.split()
first = text_split[0][0]
second = text_split[1][0]
first == second


#---------------------------------------------LAMBDA EXPRESSIONS, MAP AND FILTER FUNCTIONS------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------


mynums = [1,2,3,4,5]
for i in mynums:
    print(i**2)


#Looping through a list using map
def square (nums):
    return nums ** 2

mynums = [1,2,3,4,5]
for i in map(square, mynums):
    print(i)


#Converting into a list using map
def square (nums):
    return nums ** 2

mynums = [1,2,3,4,40]
list(map(square,mynums))


#Using map for strings
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return 'ODD'

names = ['Andy', 'Frank', 'IronMan','Alex']
list(map(splicer, names))


#Creating a list with using a function and filter
def check_even(num):
    if num % 2 == 0:
        return num

numbers = [1,2,3,4,40]
list(filter(check_even, numbers))


#Looping through a list with filter
numbers = [1,2,3,4,40]
def check_even(num):
    if num % 2 == 0:
        return num

for i in filter(check_even,numbers):
    print (i)

#LAMBDA FUNCTION
#Is also known as an anonymus function becase its a functionality that you intend only to use one time
#Because of that, we don't actually give it a name nor we use def keyword. Instead we use 'lambda'
#syntax lambda [any name]: [any name], [variable]

numbers = [1,2,3,4,40]
list(map(lambda x: x ** 2, numbers))
list(filter(lambda y: y % 2 == 0, numbers))

names = ['Andy', 'Frank', 'IronMan','Alex']
list(map(lambda letter: letter[0], names))


#-----------------------------------------------------NESTED STATEMENTS AND SCOPE---------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#LEGB Rule:
#Local - names assigned within a function (def or lambda) that are not declared globally
#Enclosing function locals - Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer
#Global (module) - names assigned at the top level of a module file or declared global in a def within the file
#Built in (python) - names pre assigned in the built in names module

x = 25

def variable():
    x = 100
    return x

print(x)
variable()



#Example of how it works according to the scope
#GLOBAL
name = 'This is a GLOBAL string'

def greet():

    #ENCLOSING
    name = 'This is an ENCLOSING string'

    def greet_two():

       #LOCAL
       name =  'This is a LOCAL string'
       print('After commenting out: ', name)

    greet_two()

greet()



#Example of re assignment of variables
x = 50

def func(x):
    print(f'The value of x is: {x}')

    #LOCAL RE ASSIGMENT!
    x = 150
    print(f'I just locally changed x to {x}')

func(x) #This print will bring both results
print(x) #This print will only bring the global scope result



#How to changed a global value inside a function using 'global' keyword
x = 50

def func():
    global x
    print(f'The value of x is: {x}')

    #LOCAL RE ASSIGMENT!
    x = 200
    print(f'I just changed global x to {x}')

print(x)
func() #This print will bring both results
print(x) #When printing, new global value will be shown



#This is another way to change a global variable without using 'global' keyword
#This is a saffer way to change global values. It's easier to debbug when needed
x = 50

def func(x):
    
    print(f'The value of x is: {x}')

    #LOCAL RE ASSIGMENT!
    x = 200
    print(f'I just changed global x to {x}')
    return x

print(x)
func(x) #This print will bring both results
print(x) #When printing, new global value will be shown


#-----------------------------------------------------------READING FILES-----------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------
#Using open()
#Example: file = open('filename', 'mode')
#Mode is optional but it can be 'r' for read and 'w' for write
#Both parameters need to be written as strings

file = open('stuff.txt') #This won't work since I have any file with that name

#The newline character
#Newline character is represented by '\n'. It indicates to go to a new line.
#'\n' also represents a character, so if you ask for the lenght, it will sum up 1
stuff = 'X\nY'
print(stuff)
print(len(stuff))

#File handle as sequence:
#A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence
xfile = open('mbox.txt') #This file doesn't exist, it's just to have an example
for line in xfile: #We can use for statement to iterate through a sequence
    print(line)

#Counting lines in a file:
xfile = open('mbox.txt') 
count = 0
for line in xfile:
    count = count + 1
print('Line count: ', count)

#Reading the whole file:
#We can read the whole file into a single string
xfile = open('mbox.txt') 
inp = xfile.read()
print(len(inp)) #This will print the lenght
print(inp[:20]) #This will print the first 20 rows

#Searching in a file:
xfile = open('mbox.txt') 
for line in xfile:
    line = line.rstrip() #This will take off the spaces generated by the loop
    if line.startswith('From: '):
        print(line)


#------------------------------------------------------DISPLAYING INFORMATION-------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

display(row1,row2,row3)

row2[1] = 'x'


#-------------------------------------------------------ACCEPTING USER INPUT--------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------

input('Please enter a value: ')

result = input('Please enter a value: ')
type(result)
result_int = int(result)
result_int


position_index = int(input('Choose an index position: '))
row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
row2[position_index]


#VALIDATING INPUT
#If we want the user to insert an integer as an input, but user writes a string, we could see this error
position_index = int(input('Choose an index position: ')) # -> ValueError: invalid literal for int() with base 10: 'two'

#We could have different types of issues when expecting user input. For this example we'll keep in mind the next 2:
#User writes a string instead a a integer
#User writes a value that is outside of range
#To avoid this, we can do the following

def user_choice():

    #INITIAL
    choice = 'Wrong'
    acceptable_range = range(0,10)
    within_range = False

    #TWO CONDITIONS TO CHECK: DIGIT OR WITHIN RANGE
    while choice.isdigit() == False or within_range == False:

        choice = input('Please enter a number (0-10): ')

        #DIGIT CHECK
        if choice.isdigit() == False:
            print('Sorry, thats not a digit!')

        #RANGE CHECK
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Sorry, youre out of acceptable range (0-10)')
                within_range = False
    
    return int(choice)

user_choice()


#USER INTERACTION THROUGH A GAME
#1. Create a function that can display the game
#2. Create a function where the user chooses the position
#3. Create a replacement choice function
#4. Create a function to ask if user wants to keep platying

game_list = [0,1,2]

def display_game(game_list):

    print('Here is the current list: ')
    print(game_list)



def position_choice():
    
    choice = 'wrong'

    while choice not in ['0','1','2']:

        choice = input('Pick a position (0,1,2): ')

        if choice not in ['0','1','2']:
            print('Sorry, invalid choice!')

    return int(choice)



def replacement_choice(game_list, position):

    user_placement = input('Type a string to place at a position: ')

    game_list[position] = user_placement

    return game_list



def gameon_choice():
    
    choice = 'wrong'

    while choice not in ['Y', 'N']:

        choice = input('Do you want to keep playing?: (Y or N)')

        if choice not in ['Y', 'N']:
            print('Please choose Y or N')


    if choice == 'Y':
        return True
    else:
        return False



game_on = True
game_list = [0,1,2]


while game_on:

    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list,position)

    display_game(game_list)

    game_on = gameon_choice()


#OBJECT ORIENTED PROGRAMMING

#Allows programmers to create their own objects that have methods and attributes
#The methods act as functions that use information about the object as well as the object instead to return results or change the current object.
#OOP allows users to create their own methods and attributes
#Uses 'self' keyword

#For much larger scripts of python code, functions by themselves aren't enough for organization and repeatability
#Common repeated tasks and objects can be defined with OOP to create code that is more usable

#Syntax

class NameOfClass(): #To define an object using 'class' keyword. Names uses 'camel casing'

    #Looks like a function but is a method (called this way when inside a class)
    #_init_ is to create an instance of the class. Is the constructor for the class
    def __init__(self, param1, param2): 
        self.param1 = param1 #Here we are assigning the first attribute to the class
        self.param2 = param2

    #Methods are essentially functions defined inside the body of the class and they are used to perform operations that sometimes
    # utilize the actual attributes of the object we created
    #You can think of methods as functions, acting on an object that take the object itself into account throught the use of
    # the self argument or self keyword
    def some_method(self):
        #Perform some action
        print(self.param1)

#Example:

class Dog():

    #CLASS OBJECTS ATTRIBUTES
    #Same for any instance of the class
    species = 'Mammal'

    def __init__(self, breed, name):

        #Attributes
        #We take in the argument
        #Assign it using self.attribute_name
        self.breed = breed
        self.name = name
    
    #OPERATIONS/ACTIONS ---> METHODS
    def bark(self, age):
        print('WOOF ! My name is {} and Im {} years old'.format(self.name, age)) #Age doesnt need 'self' since it has been provided in the method


my_dog = Dog(breed = 'Pitbull', name = 'Niurka')
type(my_dog)

#Let's call the Dog attributes, for this, you don't need parenthesis
my_dog.species
my_dog.breed
my_dog.name

#Let's call the Dog available method, now, you'll have to use parenthesis 
my_dog.bark(8)


#Example 2:

class Circle():

    #Class object attribute
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius

        #Something to point out here, if you have an attribute (in this case 'area'), it doesnt necessarily have to be defined from a 
        # parameter call
        self.area = radius ** 2 * self.pi #Since 'pi' is a class object attribute, you can also call it 'Circle.pi'
        #self.area = radius ** 2 * Circle.pi

    #METHOD
    def get_circumference(self):
        return self.radius * Circle.pi * 2

my_circle = Circle(30)
my_circle.pi
my_circle.radius
my_circle.get_circumference()
my_circle.area


#INHERITANCE AND POLYMORPHISM
#The main idea behind inheritance is to be able to reuse methods that should be common between classes by just inheriting, so there's
# no need to re write all the methods for a new class

#In python, polymorphism refers to the way in which different object classes can share the same method name and then those methods can
# be called from the same place even though a variety of different objects might be passed in

#First, let's create our base class
class Animal():

    def __init__(self):
        print('ANIMAL CREATED')
    
    def who_am_i(self):
        print('Im an animal')
    
    def eat(self):
        print('Im eating')

#Now lets inheritate the base class into a new class
#This will be a 'derived' class
#Since its a derived class, it will inherit the method from the base class
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self) #Here we create an instance of the 'Animal' class
        print('Dog Created')

    #What if you want to overwrite a previous method? You can do it
    def who_am_i(self):
        print('I am a Doggy Dog')

    #We can also add new methods
    def bark(self):
        print('WOOF !')


mydog = Dog()
mydog.who_am_i() #Even if we didn't define any method inside the 'Dog' class, 'Animal' class methods are available due to inheritance
mydog.eat()
mydog.bark()


#POLYMORPHISM

class Dog():

    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + ' says WOOF!'


class Cat():

    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + ' says MEOW!'

niurka = Dog('Niurka')
macario = Cat('Macario')

print(niurka.speak())
print(macario.speak())


#Function 'pet_speak' doesn't actually know whether you're going to pass in a dog or a cat, but since Dog and Cat classes share the 
# same 'speak' method, it means that I can leverage that capability to iterate through a list or pass it into a function where
# later on it calls for the method 'speak'. In both cases we are able to pass in different objects and we obtain object specific
# results from the same mechanism, that same method call.
for pet in [niurka, macario]:
    print(type(pet))
    print(pet.speak())


def pet_speak(pet):
    print(pet.speak())

pet_speak(niurka)


#A common pratice is to use abstract classes and inheritance.
#An abstract class never expects to be instantiated, never expects to create an instance of this class; instead, it's just designed
# to basically only serve as a base class

class Animal():

    def __init__(self, name):
        self.name = name

    #We won't be expecting to call for the method speak on the Animal class, so we'll raise an error
    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')

myanimal = Animal('Niurka')
myanimal.speak() # ---> NotImplementedError: Subclass must implement this abstract method
#This error will be happening because in the base class itself, it doesn't actually do anything. It's expecting you to inherit the
# 'Animal' class and then overwrite the 'speak' method

class Animal():

    def __init__(self, name):
        self.name = name

    #We won't be expecting to call for the method speak on the Animal class, so we'll raise an error
    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')


class Dog(Animal):

    def speak(self):
        return self.name + ' says woof!'

class Cat(Animal):

    def speak(self):
        return self.name + ' says meow!'

niurka = Dog('Niurka')
macario = Cat('Macario')

print(niurka.speak())
print(macario.speak())


#SPECIAL METHODS (MAGIC/DUNDER METHODS)
#They allow you to use built in functions with classes

class Book():

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self): # '__str__' is a special method which will allow us to print stuff in the future
        return f'{self.title} by {self.author}'
    
    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object had been deleted') 

b = Book('Python Rocks', 'Techiken Vargas', 200)
print(b)
len(b)

del b #This will delete the object created with the class from the computer memory
b

#OOP CHALLENGUE
#For this challenge, create a bank account class that has two attributes: owner & balance
#And two methods: deposit & withdraw

#As an added requirement, withdrawals may not exceed the available balance.
#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class BankAccount():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, dep_amount):
        self.balance = self.balance + dep_amount
        print(f'You just added {dep_amount}, your current balance is: {self.balance}')
    
    def withdraw(self, wt_amount):

        if wt_amount < self.balance:
            self.balance = self.balance - wt_amount
            print(f'Withdraw for {wt_amount} accepted, current balance: {self.balance}')
        else:
            print(f'Not enough funds, you stupid fuck!')
    
    def __str__(self):
        return f'Account owner: {self.owner} \nBalance owner: {self.balance}'

myaccount = BankAccount('Anuar', 1000)

print(myaccount)
myaccount.owner
myaccount.balance
myaccount.deposit(250)
myaccount.withdraw(1500)
myaccount.withdraw(750)

#PyPI with pip install
#PyPI is a repository for open source third party python packages
#So far, we´ve only used libraries that comes internally with Python (known as standard or built in libraries)
#pip is a simple way to download packages at the command line directly from the pypi repository



#MODULES & PACKAGES
#Modules are just .py scripts that you call in another .py script
#Packages are collection of modules
#This 2 terms help when you have a really large script, so instead of putting everything together and having
# huge script file, you can split it into modules and packages

#For modules, all you need to do is import the name of the file and the function you want to use
# i.e. from mymodule import my_func
#Files must be in the same folder

#For packages, first you need to create the folders and for every one of them, create a __init__.py
# from the text editor so Python understands that those aren´t just normal folders, instead, they are 
# actual packages

#This is how you can import from a module
from mymodule import my_func
my_func()

#This is how you can import directly from a package
from MyMainPackage import some_main_script
some_main_script.report_main()

#This is how you can import from a SubPackage
from MyMainPackage.SubPackage import mysubscript
mysubscript.sub_report()


#__name__ & __main__
#We see a lot of times the line of code below
# if __name__ == '__main__':

#When python runs a .py directly, it sets this name variable as '__main__'
print(f"First module's name is: {__name__}.")

#But we can also import modules (just like the previous section)
#So this help us know if we´re running a file directly or if it has been imported



#ERRORS AND EXCEPTIONS HANDLING
#Errors can happen along your code, especially when someone else ends up using it in an unexpected way.
#We can use error handling to attempt to plan for possible errors

#We will use three keywords for this entire process of exception handling:
#Try: This is the block of code to be attempted (may lead to an error)
#except: Block of code will execute in case there is an error in try block
#finally: A final block of code to be executed, regardless of an error

#Example:

def suma(num1, num2):
    print(num1 + num2)

number1 = 10
number2 = input('Please write a number: ')
suma(number1 + number2)

#We get this error
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

#what we could do is use the try keyword
try:
    result = 10 + 10
except:
    print('Youre fucking this up!')
result #Output is 20


try:
    result = 10 + '10'
except:
    print('Youre fucking this up!')
#Since we have an error in the result variable, output is 'Youre fucking this up!'
#Despite the error, the rest of the code was able to run, so when this kind of things happen, the program won't shut down entirely


try: #Try will be the code we want to try
    result = 10 + 10
except: #If there's an error inside 'try', except will handle it
    print('Youre fucking this up!')
else: #If there's no error, code will jump straight to the else statement
    print('The addition went well!')
    print(result)


#Now we can use the 'finally' keyword which will allow us to always execute code regardless if there's an error
try:
    f = open('testfile','w') #'w' allows to write
    f.write('Write a test line')
except TypeError:
    print('There was a type error!')
except OSError:
    print('You have an OS Error')
finally:
    print('I always run')


try:
    f = open('testfile','r') #'r' stands for 'read only'
    f.write('Write a test line') #Since we gave 'r' as an argument, we should get an error
except TypeError:
    print('There was a type error!')
except OSError:
    print('You have an OS Error')
finally:
    print('I always run')

#Output:
# You have an OS Error
# I always run


#Use of 3 keywords in a function
#We'll use a while loop so instead of just ending after you provide the wrong input, it keeps going until you have a block of code with no exception
def ask_for_int():

    while True:
        try:
            result = int(input('Please provide a number: '))
        except:
            print('Thats not a number, type an integer!')
            continue #as long as there's a mistake, program will keep asking for the right input
        else: #If this executes, means there was not any error
            print('Correct input, thanks')
            break #ends the loop only if we get the right input
        #finally:
            #print('Im going to ask you again until input is correct, bitch')

ask_for_int() #We can get rid of the finally statement so it doesn't show up its message when user enters the correct input



#UNIT TESTING
#As you begin to expand to larger multi-file projects, it becomes important to have test in place
#This way, as you (or your teammates) make changes or updates to your code, you can run your test files to make sure previous code still runs as expected
#There are several testing tools but we will focus in two:
#pylint: This is a library that looks at your code and reports back possible issues
#unittest: This built-in library will allow to test your own programs and check if you're getting the desired outputs


#For using pylint, you have to run this line in the termine (once your file is saved): pylint [DocName].py -r y
#At the end, your code will be rated (10 as max)

#Unittest part 2
#Go to the cap_test.py and cap.py files
#When running the test, go to the terminal path alexisvargas@MacBook-Pro-de-Alexis Bootcamps files % 
#Then write ---> python cap_test.py



#DECORATORS
#Decorators allow you to 'decorate' a function.
#Let's imagine that we just created a simple function

# def simple_func():
        #Do simple stuff
        #return something

#Now we want to add some more functionality to it...
#What we could do is take the original simple function and add more code to it but this idea of adding new functionality basically represents a problem
# because you have 2 options:
# add that extra code to the old function -- but then you'll have a problem of not being able to call your original function since you've edited with the new functionality
# or create a new function that contains the old and new code -- the problem is that now you have to recreate the entire function again.

#What if you actually then wanted to remove that extra functionality later? We would have to manually delete or make sure not to call it.

#Wouldn't it be cool if we could turn on or off those functions? This is where decorator comes in
#Decorators allow you to tack on extra functionality to an already existing function
#They use the @ operator and are then placed on top of the original function and then if you no longer want that functionality, you just delete one line from the decorator

# @some_decorator
# def simple_func():
        #Do simple stuff
        #return something

def hello(name = 'Techis'):
    print('The hello() function has beene executed!')

    def greet():
        return '\t This is the greet() func inside hello!'

    def welcome():
        return '\t This is the welcome() func inside hello!'
    
    print(greet())
    print(welcome())
    print('This is the end of the hello() function!')

hello()

#Since greet and welcome functions were defined inside the hello function, we can't run them separately
greet() # --> NameError: name 'greet' is not defined
#with this quick example, we can see that the scope for those functions are limited to the hello function

#What if we wanted to access these functions outside of hello? We could make the function return the functions inside of it

def hello(name = 'Techis'):
    print('The hello() function has beene executed!')

    def greet():
        return '\t This is the greet() func inside hello!'

    def welcome():
        return '\t This is the welcome() func inside hello!'
    
    print("I'm going to return a function!")

    if name == 'Techis':
        return greet
    else:
        return welcome

my_new_func = hello() #Since Techis is the default name inside hello, my_new_func will comply with the if statement and will become the greet function
print(my_new_func()) #When printing it, we'll get 'This is the greet() func inside hello!'

#This is an example of a function inside another funciton and then assigning it to a variable
def cool():
    
    def super_cool():
        return 'Im very cool'
    
    return super_cool

some_func = cool()
print(some_func())

#Now we'll pass a function inside another function
def hello():
    return 'Hi Techiman'

def other (some_def_func):
    print('Other code runs here!')
    print(some_def_func())

other(hello) #Here just pass in the function instead of executing it because it will execute inside the 'other' function


#Now let's crate a new decorator
def new_decorator(original_func):

    def wrap_func():
        print('Some extra code before the orinal function')
        original_func()
        print('Some extra code, after the original function')   
    return wrap_func

def func_needs_decorator():
    print('I want to be decorated')

func_needs_decorator()

decorated_func = new_decorator(func_needs_decorator)
decorated_func()


#Instead of doing all the previous steps we can use the decorators syntax:
@new_decorator #This is the decorator
def func_needs_decorator():
    print('I want to be decorated')

func_needs_decorator()

#What if we don't want the 'new_decorator' output in the second function? We just delete/comment out the decorator
# @new_decorator #This is the decorator
def func_needs_decorator():
    print('I want to be decorated')

func_needs_decorator()



#GENERATORS
#Generators allow us to generate a sequence of values over time instead of having to create an entire sequence and hold it in memory
#The main difference in syntax will be the use of a YIELD keyword/statement

#When a generator function is compiled, they become an object that supports an iteration protocol, that means that when they are called in your code, they
# don't actially return a value and then exit, instead, generators will automatically suspend and resume their execution state around the last point of value generation

#The advantage is that instead of having to compute an entire series of values up front and hold it in memory, the generator computes one value
# and waits until the next value is called for

#since they don't store anything in memory, generator are more efficent that creatin a list

#Let's create some generators

#In this first example, a list has to be created before the for loop so we can append the results somewhere... This list will be stored in memory
def created_cubes(n):
    result = []
    for x in range (n):
        result.append(x**3)
    return result

created_cubes(10)

#What if we don't need/want the results to be store but just have the output of certain process?
def created_cubes(n):
    for x in range (n):
        yield x**3

for x in created_cubes(10):
    print(x) #Same output but way too much better at memory efficiency

#If we just execute the created_cubes functions
created_cubes(10) # --> <generator object created_cubes at 0x7f98bd882580>

#If we still want to have the result as a list...
list(created_cubes(10))


#Let's create the fibonacci sequence
def gen_fibon(n):

    a = 1
    b = 1
    for i in range (n):
        yield a
        a,b = b, a+b

for number in gen_fibon(10):
    print(number)


#Another generator example:
def simple_gen():
    for x in range(3):
        yield x

for i in simple_gen():
    print(i)

g = simple_gen()
g
print(next(g)) # --> 0
print(next(g)) # --> 1
print(next(g)) # --> 2
print(next(g)) # --> Iteration error: StopIteration. It means that the values have been yielded

#When you call the 'yield' keyword, the generator is remembering what the previous item was and will return the next value GIVEN WHATEVER FORMULA IS FOLLOWING
# and the best part, it's not holding everything  in memory


#Iter function
#Allows you to automatically iterate through a normal object that you may not expect

s = 'hello'
for i in s:
    print(i)

#What if we want to iterate over s?
next(s) # --> 'str' object is not an iterator
#This means that the string object does support iteration because we went through a for loop on it, but we cannot directly iterate over it just like we did
# in the previous example using the 'next' function. If we want to iterate over an object that's not an iterator, call the 'iter' function:

s = 'hello'
s_iter = iter(s)
next(s_iter)



# ADVANCED COLLECTIONS MODULE
#Counter class 
#Let's say we want to count the number of times a number appears on a list. We would have to do the following

def count():
    mylist = [1,1,1,1,2,2,2,2,2,2,3,3,3,3,3]
    counter = {}
    for i in mylist:
        if i in counter:
            counter[i] = counter[i] + 1
        else:
            counter[i] = 1 
    return counter

count()

#Counter can actually do this for us automatically
from collections import Counter

mylist = [1,1,1,1,2,2,2,2,2,2,3,3,3,3,3]
Counter(mylist) # --> Counter({2: 6, 3: 5, 1: 4}) . Notice this looks similar to a dictionary but counters are tecnically a dictionary subclass
Counter('aaaaabbbbbbkdjdndkmd') #Counter work with strings as well

#What if I want to count the words in a sentence?
sentence = 'How many times does each word show up in this sentence with a word'
Counter(sentence.lower().split())

#We can also use special methods for this counter
letters = 'aaaaaaaaabbbbbbbbbbcccccccchhhhhhheeeeee'
c = Counter(letters)
c # --> Counter({'b': 10, 'a': 9, 'c': 8, 'h': 7, 'e': 6})
c.most_common() # --> [('b', 10), ('a', 9), ('c', 8), ('h', 7), ('e', 6)] . This method will return back a list of tuples  

#What if we just one the 3 most common?
c.most_common(3) # --> [('b', 10), ('a', 9), ('c', 8)]

#Common patterns when using the Counter() object

#sum(c.values())                 # total of all counts
#c.clear()                       # reset all counts
#list(c)                         # list unique elements
#set(c)                          # convert to a set
#dict(c)                         # convert to a regular dictionary
#c.items()                       # convert to a list of (elem, cnt) pairs
#Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
#c.most_common()[:-n-1:-1]       # n least common elements
#c += Counter()                  # remove zero and negative counts

c # --> Counter({'b': 10, 'a': 9, 'c': 8, 'h': 7, 'e': 6})
list(c)
sum(c.values())


#default dictionary
#Imagine we are in a situation where you want you script to keep running (despite an error with the keys of a dictionary) and you want to assign some 
# default value like zero.
from collections import defaultdict

d = {'a':10}
d
d['a']

#what happens if I run in a wrong way a normal python dictionary? I'll get an error
d['wrong'] #this doesn't exists yet inside the 'd' dictionary

#This is what we're gonna do
d = defaultdict(lambda : 0) #We're assigning 0 as a default value through a lambda function

d['correct'] = 100
d['correct']

d['wrong key!'] #Now, instead of getting an error, we'll get the default value --> 0

d # --> defaultdict(<function <lambda> at 0x7f98bdc3c9d0>, {'correct': 100, 'wrong key!': 0})
#So in conclusion, use cases for default dictionaries comes when you're trying to assing values to a dictionary but you don't know if every value is present or not



#Named tuple
#Tries to expand on a normal tuple object by actually having named indices inteas of just calling the values by its index

#Normal tuple and way to call the value '10'
mytuple = (10,20,30)
mytuple[0]

#What if I have a vary large tuple and want to look for a very specific value? or maybe you don't remember which value is at which index
#A named tuple is going to have not just a numeric connection to the values, but it will also have essentially a named index for that value

#This is how you construct a named tuple (kinda looks similar to a class in OOP)
from collections import namedtuple
Dog = namedtuple('Dog',['age','breed','name'] ) # function(typename:string, field_names:string)
Dog # --> <class '__main__.Dog'>

#now let's crate an instance
sammy = Dog(age = 5, breed = 'Husky', name = 'Sam')
type(sammy) # <class '__main__.Dog'>
sammy # --> Dog(age=5, breed='Husky', name='Sam')

sammy.age
sammy[0]

sammy.breed
sammy[1]

sammy.name
sammy[2]



#OPENING AND READING FILES AND FOLDERS
import os
os.getcwd()
os.listdir() #list files in the current directory

import shutil #To move files through different folders


#DATETIME MODULE
import datetime

#For time
mytime = datetime.time(23,20,1,20) #parameters 24hr format-> hour, minute, second, microsecond, timezone info
mytime.minute
mytime.hour
print(mytime) # --> 23:20:00
type(mytime)

#For dates
today = datetime.date(2022,10,18) # --> as integer: year, month, day
print(today)

today = datetime.date.today()
print(today)

today.day
today.month
today.year

#For datetime
from datetime import datetime
mydatetime = datetime(2021, 10, 3, 14, 20, 1)
print(mydatetime) # --> 2021-10-03 14:20:01

#In case you made a mistake or just want to change a value, do this
mydatetime = mydatetime.replace(year=2020)
print(mydatetime)

#Arithmetics with date time
#let's suppose you wanna know how much time a person spends on your website or how long did it take for a customer to comeback to your website after a previous visit

from datetime import date

date1 = date(2021,11,3)
date2 = date(2020,11,3)
result = date1 - date2
result.days

datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)
datetime_result = datetime1 - datetime2
datetime_result.seconds


#MATH MODULE
import math
#help(math) --> for documentation

value = 4.5
math.floor(value)
math.ceil(value)
round(4.35)
round(4.5)
round(5.5)
#When rounding, will round up when odd number and down when even number

math.pi
math.e
math.inf
math.nan
math.log(math.e)


#RANDOM MODULE
import random
random.randint(0,100)

random.seed(101) #In order to make the seed work properly, run it in the same cell as the randit
random.randint(0,100)

mylist = list(range(0,20))
mylist
random.choice(mylist) #this is to grab a random value from a list

#What if we want to grab more than 1 value from a list (repeted values are permitted) -> sample with replacement
random.choices(population = mylist, k = 10) #population = source, k = number of values you want to grab

#What if we want to grab more than 1 value from a list (repeted values are not permitted) -> sample without replacement
random.sample(population = mylist, k = 10)

#To shuffle a list
random.shuffle(mylist) #Since this happens inplace, there's no need to assign it to a variable (will affect permanetly)
mylist

sorted(mylist) #To reverse the shuffle


#Distributions
random.uniform(a=0, b=100)
random.gauss(mu=0, sigma=1)

#PYTHON DEBUGGER
#Python comes with a built-in debugger toold that allows you to interactibely explore variables within mid-operation of your python code
x = [1,2,3]
y = 2
z = 3

result = y + z
result2 = x + y #This will throw an error

import pdb
pdb.set_trace()
#This will allow you to see the variables that are interacting between eachother when getting an error
#To quit debugger, run 'pdb.set_trace()' and type 'q' 


#REGULAR EXPRESSIONS
#We already know we can search for substrings within a larger string with the 'in' operator
'dog' in 'my dog is great'
#'in' has severe limitations if we need to know the exact string and need to perform additional operations to account for capitalization and punctuation
#Whar if we only want to search for a pattern structure like an email or phone number?
#Regular expressions (REGEX) allos us to search for general patterns in text data


#i.e.
#Phone number (555)-555-5555
#REGEX pattern r"(\d\d\d)=\d\d\d-\d\d\d\d" --> 'r' is used to treat the pattern not as a string but as identifiers, 'd' means digit 
#REGEX pattern with quantifiers r"(\d{3})-\d{3}-\d{4}"

text = "The agent's phone number is 408-555-1234. Call soon!"
'phone' in text
#Now let's use regular expressions
import re
pattern = 'phone'
re.search(pattern, text) #This means: search for 'pattern' inside 'text': <re.Match object; span=(12, 17), match='phone'>

pattern = 'NOT IN TEXT'
re.search(pattern, text) #Since there's no match, nothing is returned

pattern = 'phone'
match = re.search(pattern, text)
match.span() #This method will bring the index location of the pattern
match.start()
match.end()


#If we look for the same, REGEX will only bring the first one
text = 'my phone once, my phone twice'
match = re.search('phone', text) 
match #--> <re.Match object; span=(3, 8), match='phone'>  | only turned back the first 'phone'

matches = re.findall('phone', text) #'FINDALL' will look for all the coincidences
matches #Will return a list
len(matches) #To know how many matches we have

#To get match multiple objects that coincide, use 'finditer' (this is kinda the combination of .search and .findall)
for match in re.finditer('phone', text):
    print(match.span())

#If you want to get the actual text, use the group method
for match in re.finditer('phone', text):
    print(match.group())


#REGULAR EXPRESSION PT. 2
#Character	Description	        Example Pattern Code	Exammple Match
#\d	        A digit	            file_\d\d	            file_25
#\w	        Alphanumeric	    \w-\w\w\w	            A-b_1
#\s	        White space	        a\sb\sc	                a b c
#\D	        A non digit	        \D\D\D	                ABC
#\W	        Non-alphanumeric	\W\W\W\W\W	            *-+=)
#\S	        Non-whitespace	    \S\S\S\S	            Yoyo

#Quantifiers
#Character	    Description	                Example Pattern Code	Exammple Match
#       +	    Occurs one or more times	Version \w-\w+	        Version A-b1_1
#       {3}	    Occurs exactly 3 times	    \D{3}	                abc
#       {2,4}	Occurs 2 to 4 times	        \d{2,4}	                123
#       {3,}	Occurs 3 or more	        \w{3,}	                anycharacters
#       *	    Occurs zero or more times	A\*B\*C*	            AAACC
#       ?	    Once or none	            plurals?	            plural

text = 'My phone number is 408-555-7777'
phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
phone # --> <re.Match object; span=(19, 31), match='408-555-7777'>
phone.group() # --> '408-555-7777'

#what if we want to only get the area code for the phone number?
# 'compile' compiles together different regular expressionn pattern codes
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
results
results.group()
results.group(1) #This will get us the code area


#ADDITIONAL REGEX SYNTAX
re.search(r'cat', 'The cat is here').group()
re.search(r'cat|dog', 'The dog is here')
re.search(r'cat|dog', 'The cat is here')

re.findall(r'.at', 'The cat in the hat sat there') #'.' (period) act as wildcard
re.findall(r'...at', 'The cat in the hat went splat') #Remember wildcard brings spaces as well

re.findall(r'^\d', '1 is a number') #'^' starts with - looks for the first value of the string
re.findall(r'\d$', 'The number is 2') #'$' ends with - looks for the last value of the string

#For exclusion - This is a great way to get rid of information from sentences
phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]' #This will avoid digit numbers
re.findall(pattern, phrase)

pattern = r'[^\d]+' #To group strings after deleting unwanted digits
re.findall(pattern, phrase)

test_phrase = 'This is a string!  But it had punctuation. How can we remove it?'
re.findall(r'[^!.?]+', test_phrase) #We are removing !.? from the sentence
re.findall(r'[^!.? ]+', test_phrase) #By adding a space, we'll get back the list of strings from the sentences without the digits we wanted to delete
clean = re.findall(r'[^!.? ]+', test_phrase)
' '.join(clean) #This way we join our strings/words from the previously cleaned sentence

#Test exercise
text = 'Only find the hypen-words in this sentence. But you do not know how long-ish words actually are'
pattern = r'[\w]+-[\w]+'
re.findall(pattern, text)



#TIMING YOUR CODE
#As you learn more python, you will discover multiple solutions for a single task and you may find yourself trying to figure out the most efficient approach.
#An easy way to do this is to time you code's performance
#We will focus on 3 ways of doing this:
    #Simply tracking time elapsed
    #Using the timeit module
    #Special %%timeit 'magic' for Jupyter Notebooks

#Return a list of n numbers converted to strings
#Which way is more efficient?

def func_one(n):
    return [str(num) for num in range(n)]
func_one(10)

def func_two(n):
    return list(map(str, range(n)))
func_two(10)

import time
#CURRENT TIME BEFORE
start_time = time.time()
#RUN CODE
result = func_one(1000000)
#CURRENT TIME AFTER RUNNING CODE
end_time = time.time()
#ELAPSED TIME
elapsed_time = end_time - start_time
print(elapsed_time) # --> 0.2866828441619873


#CURRENT TIME BEFORE
start_time = time.time()
#RUN CODE
result = func_two(1000000)
#CURRENT TIME AFTER RUNNING CODE
end_time = time.time()
#ELAPSED TIME
elapsed_time = end_time - start_time
print(elapsed_time) # --> 0.23856186866760254

#For code that it's simple, this method won't work because if the code runs very fast, this precission method wont be enough
#To fix this issue, we'll use 'timeit'
import timeit

#stmt = This statement will be run over and over again
#setup: Essentially means: What code needs to be run before you call statement over and over again

stmt = '''
func_one(100)
'''
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
timeit.timeit(stmt, setup, number = 100000) #In 'number' you specify how many time you want test to run (This way you get time for super fast code)
# --> 2.005156477000128


stmt2 = '''
func_two(100)
'''
setup2 = '''
def func_two(n):
    return list(map(str, range(n)))
'''
timeit.timeit(stmt2, setup2, number = 100000) # --> 1.9585707080000248


#WEB SCRAPING 
#Web scraping is a general term for techniques involving automating the gathering of data from a website
#In this section we'll download images or information off a website

#Rules of Web Scraping
    #Always try to get permission before scraping
    #If you make too many craping attempts or requests your IP Address could get blocked
    #Some sites automatically block scraping software

#Limitations of Web Scraping
    #In general every website is unique, which means every web scraping script is unique
    #A slight change or update to a website may completely break your web scraping script

#We can use HTML and CSS tags to locate specific information on a page
#To web crape woth Python we can use the BeautifulSoup and requests libraries

import requests
result = requests.get('https://example.com/') #This will be the website where we're gonna get the information/items
type(result)
result.text # --> raw string

import bs4
soup = bs4.BeautifulSoup(result.text, 'lxml') #This is the soup object where we pass in our website source and the format we want to use
soup # --> same format as HTML

#You can return anything you want, just specify it inside the select method
soup.select('title') #To get the script of the title
soup.select('title')[0].getText() #To get the actual title

site_paragraphs = soup.select('p') #To get the script of the paragraphs
site_paragraphs[0].getText() #To get the actual paragraph


#Grabbing ALL elements of a Class
res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, 'lxml')
first_item = soup.select('.toctext')[0] #This is how we get the first item from the table of content inside the wikipedia page
first_item.text

#What if we want the whole sections from the table of content? We can loop through it
for item in soup.select('.toctext'):
    print(item.text)

#
#
#

#WORKING WITH PDF'S AND SPREADSHEET CSV FILES
#Remember sometimes you can face encoding issues due to special characters based on the language your using
#In order to fix/avoid this, use the encoding argument when opening the data --> data = open('data_path', encoding = 'utf-8')
#You can search for different types of encoding
import csv
data = open('/Users/alexisvargas/Documentos/Data Science/Bootcamps files/example.csv') #Opens the file
csv_data = csv.reader(data) #Reads the csv file
data_lines = list(csv_data)
data_lines
data_lines[0] # --> These are the columns headings
len(data_lines) #It means there's 1000 rows = 1 row for headings

for line in data_lines:
    print(line)

#What if we want to grab the email of the 9th row? (excluding the first row of the headings)
data_lines[10][3] # --> 'hgasquoine9@google.ru'

#What if we only want the first 10 emails?
all_emails = []
for i in data_lines[1:11]:
    all_emails.append(i[3])
all_emails

#What if we want the full name of the 10th row?
data_lines[10]
full_name = []
for i in data_lines[1:]:
    full_name.append(i[1] + ' ' + i[2])
full_name


#HOW TO WRITE TO A CSV FILE
file_to_output = open('/Users/alexisvargas/Documentos/Data Science/Bootcamps files/to_save_file.csv', mode = 'w', newline = '')
csv_writer = csv.writer(file_to_output, delimiter = ',')
csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'], ['4','5','6']])
file_to_output.close() #You need to close the document after writing to it

#What if you want to write to an existing file? You can do it by just appending the new data
f = open('/Users/alexisvargas/Documentos/Data Science/Bootcamps files/to_save_file.csv', mode = 'a', newline = '')
csv_writer = csv.writer(f)
csv_writer.writerow(['7','8','9'])
f.close()


#EMAILS WITH PYTHON
#In this section we will explore how to send emails with Python
#We will go over this process with a Gmail account
import smtplib
smtp_object = smtplib.SMTP('smtp.gmail.com',587) #Object for the server. 1.Domain server and 2.Port number
smtp_object.ehlo() #This is to connect
smtp_object.starttls()

input('Password: ')
import getpass
password = getpass.getpass('Password: ') #This is a secure way to pass in sensitive information such as a password
#This is better than saving password in a variable i.e. password = 'password123'

email = getpass.getpass('Email: ')
password = getpass.getpass('Password: ')
smtp_object.login(email, password)
#After these 3 steps, you'll be connected to your email

from_address = email
to_address = email
subject = input('Enter the subject line: ')
message = input('Enter the body message: ')
msg = 'Subject: ' + subject + '\n' + message

smtp_object.sendmail(from_address, to_address, msg)
#These steps are to create the actual email we want to send

smtp_object.quit() #After sending the email, this is the way to close the session


#ADVANCED PYTHON OBJECTS AND DATA STRUCTURES

#ADVANCED NUMBERS
hex(12) #hex for hexadecimal representation of numbers
bin(1234) #binary representation of numbers

2**4
pow(2,4) #Function for powers

abs(-3) #Absolute value
round(3.9) #Rounds values
round(3.1416, 2)

#ADVANCED STRINGS
s = 'hello world'
s.capitalize() #Capitalizes the first word of a string
s.upper()
s.lower()
s.count('o') #To count how many items of the string fill the condition
s.find('o') #This will return the index of the first instance to when the object appears

s = 'hello'
s.isalnum() #Checks if characters are alphanumerics
s.isalpha() #To check if characters are alphabetic
s.islower() #To check if all string is lower case
s.isupper() #To check if all string is upper case
s.isspace() #To check if string is a white space
s.istitle() #To check if string is a title case
s.endswith('o')
s.startswith('h')

#Built in methods for strings
s = 'Techiman Vargas'
s.split()

s = 'hello'
s.split('e') #To split a unique word starting from one character of its own

s = 'hiihihihiiihhhiihihi'
s.split('i') #It will also split every instance of it

s.partition('i') #Partition will only separate at the first instance -> before character, actual character, after character


#ADVANCED SETS
s = set()
s.add(1)
s.add(2)
s
s.add(2)
s
s.clear()
s

s = {1,2,3}
sc = s.copy()
sc
s.add(4)
s
sc
s.difference(sc) #Returns the difference between 2 sets

s1 = {1,2,3}
s2 = {1,4,5}
s1.difference_update(s2) #Removes elements found in both sets
s1

s
s.discard(2) #Gets rid of the elements you ask for IF EXISTS
s

s1 = {1,2,3}
s2 = {1,2,4}
s1.intersection(s2) #Returns the common elements between 2 sets

s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
s1.isdisjoint(s2) #This returns true if sets HAVE A NULL INTERSECTION
s1.isdisjoint(s3)

s1
s2
s1.issubset(s2) #To check if one set is contained in another set
s2.issuperset(s1) #The inverse of issubset

s1
s2
s1.symmetric_difference(s2) #Will return the different items between the 2 sets

s1.union(s2)
s1.update(s2)
s1


#ADVANCED DICTIONARIES
d = {'k1':1, 'k2':2}

for k in d.items():
    print (k)


#ADVANCED LISTS
l = [1,2,3]
l.append(4)
l

l.count(10)
l.count(4)

x = [1,2,3]
x.append([4,5]) #Append appends all the elements from the iterable
x

x = [1,2,3]
x.extend([4,5]) #Extends appends elements individually
x

l = [1,2,3,4]
l
l.index(2)

l = [1,2,3,4]
l
l.insert(2, 'inserted') #Inserts whatever item you want in the specified index
l

l = [1,2,3,4]
l
l.pop(2) #You can pass an index to get rid of that element, if any index is specified, the last item will be removed. Happens in place
l

l = [1,2,3,4]
l.append(1)
l
l.remove(1) #'remove' removes the first occurence of the specified item. Happens in place
l

l = [1,2,3,4]
l.reverse() #Happens in place
l

l = [1,2,3,4]
l.sort() #Happens in place
l


