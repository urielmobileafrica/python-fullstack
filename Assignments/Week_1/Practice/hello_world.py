# 1. TASK: print "Hello World"
print("Hello World")

# 2. print "Hello Noelle!" with the name in a variable
name = "Sam"
print("Hello",name)
print("Hello " + name)

# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello",name)	# with a comma

#print("Hello" + name)	# with a +	-- this one should give us an error!

print("Hello " + str(name))	# with a +	-- corrected with the str() method

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

food_one="chips"
food_two="Pork Ribs!"

print("I love to ear {} and {}".format(food_one,food_two))
print(f"I love to eat {food_one} and {food_two}")

print(food_one.capitalize())
print(food_two.strip('P'))
print(food_two.casefold())#change case to compare where your looking for literal rather than exact match :) 

#tabbing shows you methods available - by installing python plugin from MSFT

