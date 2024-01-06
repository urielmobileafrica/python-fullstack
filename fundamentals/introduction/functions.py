def add(a,b):	# function name: 'add', parameters: a and b
    x = a + b	# process
    return x	# return value: x

new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
print(new_val)    # the result of the add function gets sent back to and saved into new_val, so we will see 8

# Challenge 1:
#   Fill in the missing code for the full_name function.
#   Be sure to add the 2 parameters (and name them appropriately)
#   Return the full name to get the desired output!

def full_name(fname,lname):
    return f'{fname} {lname}'

name1 = full_name("Eddie", "Aikau")
print(name1) # should print Eddie Aikau
print(full_name("Sam", "Keiru"))
# Challenge 2: 
#   Call the function again using your own name and print the results!