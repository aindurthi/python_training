#!usr/bin/python
import re
import sys
def total():
 def menu():
    print "Please enter any one option"
    print "1.search"
    print "2.add"
    print "3.remove"
    print "4.exit"
 menu()
 book = {"First": [],"Last": [],"Phone":[],"Email": []}
 book2 = {}
 i = 1
 while i:
  i = raw_input("Enter choice: ")
  if i == '1':
    a = raw_input("enter any one option: ")
    cache1 =  [book["Phone"][i] for i in range(len(book["Phone"]))]
    cache2 =  [book["First"][i] for i in range(len(book["First"]))]
    cache3 =  [book["Last"][i] for i in range(len(book["Last"]))]
    cache4 =  [book["Email"][i] for i in range(len(book["Email"]))]
    for y in range(len(cache2)):
       if  a == cache2[y]:
         print cache1[y]
         print cache3[y]
         print cache4[y]
    for y in range(len(cache3)):
       if a == cache3[y]:
         print cache1[y]
         print cache2[y]
         print cache4[y]
    for y in range(len(cache1)):
       if a == cache1[y]:
         print cache2[y]
         print cache3[y]
         print cache4[y]
    total()
  elif i == '2':
    first_name = raw_input("Enter the First name: ")
    last_name = raw_input("Enter the Last Name: ")
    number = raw_input("Enter the phone Number: ")
    email = raw_input("Enter the email account: ")
    if first_name in book["First"] and last_name in book["Last"] and number in book["Phone"] and email in book["Email"] and len(number) is 10:
        print "already exist"
    else:
     if first_name.isalpha() and last_name.isalpha() and last_name not in book["Last"] and email not in book["Email"] and re.match(r'\w+@\w+\.com',email) and number not in book["Phone"] and len(number) is 10 and number.isdigit():
        book["First"].append(first_name)
        book["Last"].append(last_name)
        book["Email"].append(email)
        book["Phone"].append(number)
     else:
        print ("Please check ")
        if last_name in book["Last"] or email in book["Email"] or number in book["Phone"]:
           print "email or number or last name already exist"
    book2["First"] = list(set(book["First"]))
    book2["Last"] = list(set(book["Last"]))
    book2["Phone"] = list(set(book["Phone"]))
    book2["Email"] = list(set(book["Email"]))
    print book2
    menu()
  elif i == '3':
    remove = raw_input("Enter contact to remove: ")
    cache1 =  [book["Phone"][i] for i in range(len(book["Phone"]))]
    cache2 =  [book["First"][i] for i in range(len(book["First"]))]
    cache3 =  [book["Last"][i] for i in range(len(book["Last"]))]
    cache4 =  [book["Email"][i] for i in range(len(book["Email"]))]
    for y in range(len(cache1)):
        if remove == cache1[y]:
           del book["Phone"][y]
           del book["First"][y]
           del book["Last"][y]
           del book["Email"][y]
           print book
           print "Removed Successfully"
    total()
  elif i == '4':
    sys.exit()
  elif i != '4':
    total()
total()