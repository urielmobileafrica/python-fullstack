'''
for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

# Challenge: Write a for loop to print all integers from 1 to 20, including 20.
print("starting the challenge")
for i in range(1,21):
    print(i)

'''
for x in 'Hello':
    print(x)
# output: 'H', 'e', 'l', 'l', 'o'


my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz


countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]

# Challenge 1: Fix the range!
for integer in range(0,len(countries)):
    print(integer, countries[integer])
    # Challenge 2: print the index here
    #print(countries[integer])
    # Challenge 3: print the country here
 
# Looping over values only...
for country in countries:
    print("Country: ", country)
    # Challenge 4: print the country here

    count = 0
while count <= 5:
    print("looping - ", count)
    count += 1


y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")


for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r







