#Accessing Values in Lists
#!/usr/bin/python

list2 = ['Sachintend', 'dajdjasdas', 'rr', 'cr'];
list1 = ['physics', 'chemistry'];
list2.sort()
print list2
mydict = {key:value for key, value in zip(list2,list1)}
print mydict