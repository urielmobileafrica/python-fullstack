
#Basics - Printing 1 to 150
for i in range(1,151):
    print(i)

#Multiples of Five
for i in range(5,1001,5):
    print(i)

#Counting the Dojo Way
for i in range(1,101):
    if (i%10) == 0:
        print('Coding Dojo')
    elif(i%5) == 0:
        print('Coding')
    else:
        print(i)

#Whoa. That Sucker's Huge
oddsum=0
for i in range(1,500001,2):
    oddsum=oddsum+i
print(oddsum)

#Count Down by Fours
for i in range(2018,0,-4):
    print(i)

#Flexible Counter
lowNum=2
highNum=9
mult=3
for i in range(lowNum+1,(highNum+1),mult):
    print(i)

