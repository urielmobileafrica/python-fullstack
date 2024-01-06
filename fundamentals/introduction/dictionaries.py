# Challenge yourself!

person = {
    "first_name": "Ada", 
    "last_name": 
    "Lovelace", 
    "age":42, 
    "is_organ_donor": True
}
print(person)


# Create a another person dictionary called person_2 and print it to the terminal

capitals = {}
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
print(capitals)
# Add 2 key-value pairs to this dictionary.

# print the capitals dictionary to see how it changed!
capitals["ke"] = "Nairobi"
capitals["ug"] = "Kampala"
#capitals["dnk"] = "Naivasha" #overwriting an existing key
if "dnk" not in capitals:
    capitals["dnk"] = 'Naivasha'
print(capitals)

print(capitals["ke"],capitals["deu"])
print(type(capitals))

my_dict = { "name": "Noelle", "language": "Python" }
for each_key in my_dict:
    print(each_key)
    print(my_dict[each_key])
# output: name, language
    
capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
     print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
     print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc



