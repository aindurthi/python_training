#!usr/bin/pyhton
def funct():
 perform = input("Enter required action: ")
 book = {}
 def search_funct():
    a = raw_input("enter any one option: ")
    if a in book:
        print book
    if a in book:
        print book
    if a in book:
        print book

 def add_funct():
    first_name = raw_input("Enter the First name: ")
    last_name = raw_input("Enter the Last Name: ")
    number = raw_input("Enter the phone Number: ")
    if first_name not in book:
        book["First"] = first_name
    else:
        print ("already exist")
    if last_name not in book:
        book["Last"]= last_name
    else:
        print ("already exist")
    if number not in book:
        book["Phone"] = number
    else:
        print ("already exist")
    return book
 def remove_funct():
    remove = input("Enter contact to remove: ")
    if remove in book.values():
        del book["Phone"]
        print book
 def total():
    if perform == 1:
        search_funct()
    elif perform == 2:
        add_funct()
    elif perform == 3:
        remove_funct()
    elif perform !=4:
        total()
 total()
funct()





'''first_name = raw_input("Enter the First name: ")
last_name = raw_input("Enter the Last Name: ")
number = raw_input("Enter the phone Number: ")
book = {"First_Name": [], "Last_Name": [], "Phone": []}
def search_funct():
    if first_name in book["First_Name"]:
        print book
    if last_name in book["Last_Name"]:
        print book
    if number in book["Phone"]:
        print book
search_funct()
def add_funct():
    if first_name not in book["First_Name"]:
        book["First_Name"].append(first_name)
    if last_name not in book["Last_Name"]:
        book["Last_Name"].append(last_name)
    if number not in book["Phone"]:
        book["Phone"].append(number)
    print book
add_funct()
print book
def remove_funct():
    if first_name in book["First_Name"]:
        book.remove("First_Name")
    if last_name in book["Last_Name"]:
        book.remove("Last_Name")
    if number in book["Phone"]:
        book.remove("Phone")
    print book



if first_name not in book["First_Name"]:
    book["First_Name"].append(first_name)
if last_name not in book["Last_Name"]:
    book["Last_Name"].append(last_name)
if number not in book["Phone"]:
    book["Phone"].append(number)
print book'''