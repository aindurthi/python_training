#!usr/bin/python
def menu():
    print "1. Search a Phone Number"
    print "2. Add a Phone Number"
    print "3. Remove a Phone Number"
    print "4. Quit"
menu()
numbers = {}
i = 0
while i != 4:
    i = input("Enter the choice: ")
    if i == 1:
        name = raw_input("Name: ")
        for k,l in numbers.iteritems():
            if name is l:
                print name
    elif i == 2:
        First = raw_input("First_Name: ")
        Last = raw_input("Last_Name: ")
        Phone = input("Number: ")
       # numbers[First] = Phone
        #numbers[Last] = Phone
        for k,l in numbers.items():
            if Phone is not l:
                numbers[First] = Phone
                numbers[Last] = Phone
            else:
                print ("already exist")

