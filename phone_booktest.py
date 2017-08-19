#!usr/bin/python
num={}
def menu():
    print "1.Search a contact"
    print "2.Add a contact"
    print "3.Remove a contact"
    print "4.exit"
menu()
c = [1,2,3,4]
for i in range(len(c)):
    choice = input("Enter any choice: ")
    if choice == 1:
        search=raw_input("Enter a contact name:")
        if search in num:
            print search
        else:
            print "No number"
    elif choice == 2:
        first = raw_input("Enter a First name:")
        last = raw_input("Enter a Last name:")
        number = raw_input("Enter a Number:")
