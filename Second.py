#!usr/bin/python
password = raw_input("Enter the password:")
a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
symbol ="~`!@#$%^&*()_-+{}[]?<>"
b = []
c = []
d = []
e = []
f = []
g = []
for k in symbol:
  f.append(k)
for i in range(len(password)):
   if password[i].isupper():
     b.append(password[i])
   if password[i].islower():
     c.append(password[i])
   if password[i].isspace():
     d.append(password[i])
   if password[i].isdigit():
     e.append(password[i])
for l in password:
  if l in f:
   g.append(l)
if len(b) > 0 and len(c) > 0 and len(e) > 0 and len(g) > 0 and len(password) is 8:
    print "Created password succesfully"
else:
    print "please check the password pattern"