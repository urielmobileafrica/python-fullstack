# Practice Challenge: Correct the errors!
first_name = "Alana"
last_name = "Da Silva"
age = 36
profession = "Software Developer"
years_experience = 5

greeting = f"Hello my name is {first_name} {last_name}"
#print(f"Hello my name is {first_name} {last_name}" )
print(greeting) 
# Desired output: Hello my name is Alana Da Silva

print(f"I am {age} years old") 
# Desired output: I am 36 years old

print("I work as a {}.".format(profession))
# Desired output: I work as a Software Developer.

exp_string = f"I have worked in the field for {years_experience} years."
print(exp_string)
# Desired output: I have worked in the field for 5 years.

print("I started in the field when I was " + str(age - years_experience) + " years old.")
# Desired output: I started in the field when I was 31 years old.
