#!usr/bin/python
fh = open("test.txt","r+")
test = fh.readlines()
for i in range(len(test)):
    for j in range(len(test[1].split())):
        test[1].split()[5] = "rest"
print test

