#!usr/bin/python
#dicts = {"name": "Nobody" , "location": "Nowhere", "age": "infinity"}
dict1 = {"name": "Nobody" , "location": "Nowhere", "age": "infinity", "friend" : "somebody"}
dict2 = {"sex": "none"}
list1 = dict1.values()
print list1
#for i in range(len(list1)):
#    if "tester" not in list1[i]:
#       print "No"
for i in range(len(dict1)):
    print dict1["name"][i]
#d1 = {"arya": [], "vis": []}
#d2 = {"arya": ["test","rest"], "vis": ["test","best"]}
'''list2 = {"first": [] ,"last": [],"num": []}
list1 = ["arya","teja",123,"arya","test",154]
d = dict(zip(list2["first"],[list1[i] for i in range(len(list1)) if list1[i] is "arya"]))
print d'''
'''d = {}
for d in (d1,d2):
    for key,value in d.iteritems():
        d[key].append(value)
print d'''


'''for i,j in dict1.items():
    if j is "Nowhere":
        print i'''