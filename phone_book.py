#!usr/bin/python
a = {}
b = 0
f = {}
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
        for i,j in a.items():
            if search is j:
                print search
            else:
                print "No contact"
    elif choice == 2:
        first = raw_input("Enter a First name:")
        last = raw_input("Enter a Last name:")
        number = raw_input("Enter a Number:")
        list1 = a.values()
        for i in range(len(list1)):
            if number not in list1[i]:
                a["First"] = first
                a["Last"] = last
                a["Phone"] = number
        print a
    elif choice == 3:
        remove = input("Enter your number: ")
        for i,j in a.items():
            if remove is j:
                del a["phone"]
            else:
                print "No contact"
    elif choice == 4:
        menu()
print s