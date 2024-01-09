class User:		
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42
    def __str__ (self):
        return f'{self.first_name} {self.last_name} {self.age}'
# Now that you have a class set up with a constructor 
# You can assign new variables to new users in the outer scope!

user_ada = User()
print(user_ada.first_name, user_ada.last_name) # prints Ada
user_ada.last_name='Ojwang'
print(user_ada.first_name, user_ada.last_name) # prints Ada
print(user_ada)

user_2 = User()
print(user_2.last_name)
print(user_ada) #prints the memory location of the class? <__main__.User object at 0x1058fa030>
