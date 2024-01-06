
#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#This will print '5'

#This is commented out because it has an error
'''
#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#This will return an error as the first function is yet to be defined - CORRECT
'''

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#This will return the number '5' as the function will exit on the first return statement


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#This will print the number 5

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#This will print the number '5' - WRONG!
#This function actually returns None so as no explict return statement has been added and I failed to notice that

#This is commented out as it error out
'''
#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#This will print the number '8'
#The Add fundtion is incomplete and rather than returning a value it attempts to do None + None and so returns an exception rather than the number '8'
'''

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#This with print the string literal '25'


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#This will print '100' and return an interger value of 10 - PARTIALLY CORRECT
#My omission here is that the return value is also printed so it prints both 100, then 10.

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3

#This will return the interget 7 and print '7'
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
#This will return the integer 14 and print '14'
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#The two function calls will return 7 and 14 respectively and the value '21' will be printed on screen
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))




#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#This will print the number '8'


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#This will first print the number '500' twice on two separate lines, it will then print '300' once before printing '500' one final time


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#This will print '500' twice, then print '300' then finally print '500' all on separate lines


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#This will print '500' twice, Then print '300' and assign the global variable b a value of 300, then would print '300' one last time. All on separate lines



#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#This would print '1', then '3', then '2'


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#This would print '1', then print '3', then print '5', then print '10' all on diffferent lines
