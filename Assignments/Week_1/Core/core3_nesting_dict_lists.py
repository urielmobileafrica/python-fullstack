#01 - Update Values in Dictionaries & Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#01-1 - Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)
print() 

#01-2 - Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name']='Brayant'
print(students)
print()

#01-3 - In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]='Andres'
print(sports_directory)
print()

#01-4 - Change the value 20 in z to 30
z[0]['y']=30
print(z)
print()


#02 - Update Values in Dictionaries & Lists
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range(len(students)):
        h1=''
        h2=''
        itr=0
        for first_name, last_name in students[i].items():
            if itr == 0:
                h1=f'{first_name} - {last_name}'
                itr +=1
            elif itr != 0:
                itr=0
                h2=f'{first_name} - {last_name}'
                print(h1,', ',h2)

iterateDictionary(students)
print()

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
'''
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
'''

#03 - Get Values From a List of Dictionaries
def iterateDictionary2(keyname,students):
    print(keyname)
    for i in range(len(students)):
        print(students[i].get(keyname))

iterateDictionary2('first_name',students)
print()
iterateDictionary2('last_name',students)
print()

# Wasn't able to solve this will look at the solution post submission!!
#04 - Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo_arg={}):
    keys=[]
    keys=dojo_arg.keys()
    print(keys)

    

printInfo(dojo)

