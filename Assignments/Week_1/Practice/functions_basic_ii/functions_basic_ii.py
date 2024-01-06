#1 - Countdown
print()
print('1 - Countdown')
def countdown(number):
    newlist=[]
    for number in range(number,-1,-1):
        #print(number)
        newlist.append(number)
    return newlist
print(countdown(5))
print()

#2 - Print and Return
print('2 - Print and Return')
def print_and_return(alist=[]):
    print(alist[0])
    return int(alist[1])

print('This is the Value returned by the Function <> ' + str(print_and_return([1,2]))) #printing output to show correctness
print()

#3 - First Plus Length
print('3 - First Plus Length')
def first_plus_len(alist=[]):
    return len(alist)+int(alist[0])
    
print(first_plus_len([1,2,3,4,5])) #Checking Output
print()

#4 - Values Greater than Second
print('4 - Values Greater than Second')
def values_greater_than_second(alist=[]):
    pos2=alist[1] #store the second value
    print(str(alist) + ' <> The Original List ') #Original List
    alist.pop(pos2)
    #.sort(revers=True) would be largest to smallest
    alist.sort(reverse=True)
    print(str(alist) + ' <> List to be Sorted w/o Index 1 ') #Checking sorted alist and compating with printed blist
    print()
    blist=[]
    blist_count=0
    for i in range(len(alist)):
        if alist[i] > pos2:
            blist.append(alist[i])
            blist_count+=1
            continue
        if blist_count<2:
            print('There are no Qualifying Members')
            return False
        else:
            print(f'There are {blist_count} Members > {pos2}!')
            print(blist)
        return blist

values_greater_than_second([1,5,7,3,7,8,9,9,19])
print()
print('Example #2')
print(values_greater_than_second([1,2,2,0,2]))
print()

#5 This Length, That Value
print('#5 This Length, That Value')
def thisl_thatv(length=0,value=0):
    newlist=[]
    for length in range(length):
        newlist.append(value)
    print(newlist)
    return newlist

thisl_thatv(4,7)
thisl_thatv(6,2)








