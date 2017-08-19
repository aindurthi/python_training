#!usr/bin/python
import re
def menu():
   print "1.search"
   print "2.add"
   print "3.remove"
   print "4.exit"
menu()
book = {"First": [],"Last": [],"Phone":[],"Email": []}
i = 0
while i <= 4:
  i = input("Enter choice: ")
  if i == 1:
    a = raw_input("enter any one option: ")
    cache1 =  [book["Phone"][i] for i in range(len(book["Phone"]))]
    cache2 =  [book["First"][i] for i in range(len(book["First"]))]
    cache3 =  [book["Last"][i] for i in range(len(book["Last"]))]
    cache4 =  [book["Email"][i] for i in range(len(book["Email"]))]
    for y in range(len(cache2)):
       if  a == cache2[y]:
         print cache1[y]
         print cache4[y]
    for y in range(len(cache3)):
       if a == cache3[y]:
         print cache1[y]
         print cache4[y]
    for y in range(len(cache1)):
       if a == cache1[y]:
         print cache2[y]
         print cache3[y]
         print cache4[y]
  elif i == 2:
    first_name = raw_input("Enter the First name: ")
    last_name = raw_input("Enter the Last Name: ")
    number = raw_input("Enter the phone Number: ")
    email = raw_input("Enter the email account: ")
    if first_name in book["First"] and last_name in book["Last"] and number in book["Phone"] and email in book["Email"] and len(number) is 10:
        print "already exist"
    if first_name not in book["First"] or first_name in book["First"] and first_name.islower() or first_name.isupper() :
        book["First"].append(first_name)
    if last_name not in book["Last"] and last_name.islower() or last_name.isupper():
        book["Last"].append(last_name)
    if email not in book["Email"] and re.match(r'\w+@\w+\.[a-z]+',email):
        book["Email"].append(email)
    if number not in book["Phone"] and len(number) is 10 and number.isdigit():
        book["Phone"].append(number)
    else:
        print ("Phone number already exist")
    print book
  elif i  == 3:
    remove = raw_input("Enter contact to remove: ")
    cache1 =  [book["Phone"][i] for i in range(len(book["Phone"]))]
    cache2 =  [book["First"][i] for i in range(len(book["First"]))]
    cache3 =  [book["Last"][i] for i in range(len(book["Last"]))]
    cache4 =  [book["Email"][i] for i in range(len(book["Email"]))]
    for y in range(len(cache1)):
        if remove == cache1[y]:
           del book["Phone"][y]
           del book["First"][y]
           del book["Email"][y]
           print book
  elif i == 4:
    menu()
