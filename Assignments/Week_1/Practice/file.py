#variable declaration
num1 = 42 #Datatype Primitive Number
num2 = 2.3 #Datatype Primitive Number
boolean = True #Datatype Primitive Boolean
string = 'Hello World' #Datatype Primitive String 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #List + initialization
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Dictionary + initialization
fruit = ('blueberry', 'strawberry', 'banana') #Tuple + initialization

print(type(fruit)) #funtion call, returning variable type on Tuple 'fruit'
print(pizza_toppings[1]) #Accessing value in index 1 (second value) in list) to pring
pizza_toppings.append('Mushrooms')#List - Adding Value to the end of the list
print(person['name'])#Accessing value in dictionary based on the key 'name'
person['name'] = 'George'#Changing the value in a dictionary
person['eye_color'] = 'blue' #changing the value in dictionaty
print(fruit[2])#accessing - to print the 3rd item in the list

#if-else block conditional statement
if num1 > 45: #conditional if statement evaluation
    print("It's greater") # function to output - i.e. print a Literal String
else: #conditional elseif evaluated if 1st condition is not met
    print("It's lower") 

#if conditional statement
if len(string) < 5:#funtion to check length of string returning an integer
    print("It's a short word!") #function to output a string 
elif len(string) > 15:#funtion to check length of string returning an integer
    print("It's a long word!")
else:#action if all conditions above evaluate to false
    print("Just right!")#function print a literal String

#for loop - with function to print output of incremented interger value 'x'
for x in range(5): 
    print(x)#prints 0 to 4
for x in range(2,5):
    print(x)#prints 2 - 4 exlcuding 5 :)
for x in range(2,10,3):
    print(x)#prints 2, skips 3, prints 5, skips 3, prints 8 then terminates as the next value is 11

#variable definition and initiation - global
x = 0
while(x < 5):
    print(x)#function to print the value of x
    x += 1#increment the value of x before checkin the while condition again

pizza_toppings.pop()#pop the last element in the list leaving 5 elements
pizza_toppings.pop(1)#popping (removing) index 1 in the new 5 member list and resulting in a 4 memeber list

print(person)#function to print dictionaty named 'person'
person.pop('eye_color')#removing the key-value pair eye_color
print(person)#printing the new dictionary less the key-value pair eye_color removed by the previous operation

for topping in pizza_toppings:#for loop, initialize variable toppiong and assign the first value in the list index 0
    if topping == 'Pepperoni':
        continue#continue if condition met to iterate through the list index so outcome will be 
    #print all list members 'After First if statement' 3 times
    print('After 1st if statement')#function printing a literal string
    if topping == 'Olives':
        break#break once at index 4

#creating a function to iterate 10 times action is to print the literal string 'Hello'
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

#custom function called to print Hello 10 times
print_hello_ten_times()

#defined function to print Hello "x" times taking an integer as an argument
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')#function printing a literal string "Hello"
#call function to print hell 4 times
print_hello_x_times(4)

#collapsed function defined witha default iteration of 10 unless an argument is passed
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello') #function printing a literal string "Hello"

print_hello_x_or_ten_times()#print hello default 10 times
print_hello_x_or_ten_times(4)#print hello an additinal 4 times


"""
Bonus section
"""

print(num3) #- NameError: name <variable name> is not defined, should have been defined and initialized first
num3 = 72 #definition of variable after use throws an error
fruit[0] = 'cranberry' #- TypeError: 'tuple' object does not support item assignment
print(person['favorite_team'])#- KeyError: 'favorite_team'
print(pizza_toppings[7])#- IndexError: list index out of range
print(boolean)#- NameError: name <variable name> is not defined

#- AttributeError: 'tuple' object has no attribute 'pop'
#- TypeError: 'tuple' object does not support item assignment
fruit.append('raspberry')#Tuples are immutable and can't be modified - fruit is a tuple
#- AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1)#Tuples are immutable and can't be modified - fruit is a tuple