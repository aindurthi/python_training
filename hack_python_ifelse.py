#!usr/bin/python
'''
#############WRITE A FUNCTION####################
def is_leap(year):
    leap = False
    if year%400 == 0:
        return not leap
    if year%100 == 0:
        return leap
    if year%4 == 0:
        return not leap
    return leap
#year = input("Enter the year: ")
#print is_leap(year)
n = input("Enter a number: ")
def loop(n):
     print "".join(map(str,range(1,n+1)))
loop(n)
################################################
n = input("Enter a number: ")                 ##
for ____ in range(10):                        ##
    print ____                                ##
################################################
#########LISTS#############
l = []
t = input("Enter the number: ")
for i in range(0,t):
  cmd = raw_input("operation: ").split()
  if cmd[0] == "insert":
    l.insert(int(cmd[1]),int(cmd[2]))
  if cmd[0] == "print":
    print l
  if cmd[0] == "remove":
    l.remove(int(cmd[1]))
  if cmd[0] == "append":
    l.append(int(cmd[1]))
  if cmd[0] == "sort":
    l.sort()
  if cmd[0] == "pop":
    l.pop()
  if cmd[0] == "reverse":
    l.reverse()
############TUPLES##################
n = input()
integer_list = map(int,raw_input().split())
print hash(tuple(integer_list))
#print hash(tuple(list))
###########LIST COMPREHENSION###################
x = int ( raw_input())
y = int ( raw_input())
z = int ( raw_input())
n = int ( raw_input())
ar = []
p = 0
for i in range ( x + 1 ) :
    for j in range( y + 1):
        for k in range( z + 1):
                if i+j+k != n:
                        ar.append([])
                        ar[p] = [ i , j , k ]
                        p+=1
print ar
##########FIND SECOND LARGEST NUMBER##############
n = input()
arr = map(int, raw_input().split())
print max(n for n in arr if n!=max(arr))
#################NESTED LISTS####################
test = input()
scores = []
every = []
total = []
for i in range(test):
 name = raw_input()
 score = float(raw_input())
 scores.append(score)
 every.append([name,score])
for j in range(len(scores)):
  if scores[j] == min(n for n in scores if n!=min(scores)):
   total.append(every[j][0])
   total.sort()
for k in total:
 print k
################Finding the percentage####################
n = int(raw_input())
student_marks = {}
for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
query_name = raw_input()
for i,j in student_marks.items():
    if query_name == i:
     avg = [(j[0]+j[1]+j[2])/3 for k in range(len(j))]
     print float(avg[0])
#############SWAP CASE#######################
def swap_case(s):
    return ("".join(i.upper() if i.islower() else (i.lower() if i.isupper() else i.upper()) for i in s))
s = raw_input()
result = swap_case(s)
print result
##########SPLIT AND JOIN####################
def saj(line):
    return "-".join(line.split(" "))
line = raw_input()
print saj(line)
##############What's Your Name?##################
def pfn(a,b):
    v = "Hello first_name last_name"
    t = v.split(" ")
    print " ".join(a if t[i] == "first_name" else (b if t[i] == "last_name" else t[i]) for i in range(len(t)))+"! You just delved into python."
first_name = raw_input()
last_name =raw_input()
pfn(first_name,last_name)
############################################################
####################################################
s=raw_input()
cmd=raw_input().split()
l=list(s)
p = int(cmd[0])
c = cmd[1]
if p:
    l[p]=c
    s=''.join(l)
    print s
#########################MUTATIONS####################
def ms(string,position,character):
    lists = list(string)
    if position:
        lists[position]=character
        string=''.join(lists)
        return string
s=raw_input()
i,c=raw_input().split()
test = ms(s,int(i),c)
print test
#####################FIND A STRING#########################
def my_count(string, sub_string):
    string_size = len(string)
    substring_size = len(sub_string)
    count = 0
    for i in xrange(0,string_size-substring_size+1):
        if string[i:i+substring_size] == sub_string:
            count+=1
    return count
string = raw_input().strip()
sub_string=raw_input().strip()
my_count(string,sub_string)
###########################################################
############################################################
s=raw_input()
a,b,c,d,e = [],[],[],[],[]
for i in range(len(s)):
    if s[i].isalnum():
        a.append(s[i])
    else:
        print False
    if s[i].isalpha():
        print True
    else:
        print False
    if s[i].isdigit():
        print True
    else:
        print False
    if s[i].isupper():
        print True
    else:
        print False
    if s[i].islower():
        print True
    else:
        print False
##############################################################
#####################SRING VALIDATOR###########################
s=raw_input()
a,b,c,d,e = [],[],[],[],[]
for i in range(len(s)):
    if s[i].isalnum():
        a.append(s[i])
    if s[i].isalpha():
        b.append(s[i])
    if s[i].isdigit():
        c.append(s[i])
    if s[i].islower():
        d.append(s[i])
    if s[i].isupper():
        e.append(s[i])
if len(a)>0:
    print True
else:
    print False
if len(b)>0:
    print True
else:
    print False
if len(c)>0:
    print True
else:
    print False
if len(d)>0:
    print True
else:
    print False
if len(e)>0:
    print True
else:
    print False
######################TEXT ALIGMENT##############################
thickness = input()
c = 'H'
for i in range(thickness):
    print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)
for i in range((thickness+1)/2):
    print (c*thickness*5).center(thickness*6)
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)
for i in range(thickness):
    print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)
#################TEXT WRAP#####################
import textwrap
def wrap(string,max_width):
    testing = textwrap.fill(string,max_width)
    return testing
string,max_width = raw_input(),input()
result= wrap(string,max_width)
print result
##############Designer Door Mat####################
N, M = map(int,raw_input().split())
for i in xrange(1,N,2):
    print ((M-(i*3))/2)*"-" + i*".|." + ((M-(i*3))/2)*"-"
print ((M/2)-3)*"-"+"WELCOME"+((M/2)-3)*"-"
for i in xrange(N-2,-1,-2):
    print ((M - (i * 3)) / 2) * "-" + i * ".|." + ((M - (i * 3)) / 2) * "-"
##############string Formatting#################
n = input()
width = len(format(n,"b"))
for i in range(1,n+1):
    octa =oct(i)
    octal = octa.lstrip('0')
    hexad = format(i,"x")
    hexa_up=hexad.upper()
    binary = format(i,"b")
    print str(i).rjust(width)+"\t"+octal.rjust(width)+"\t"+hexa_up.rjust(width)+"\t"+binary.rjust(width)
################Aplhabetic rangoli################
import string
alpha = string.ascii_lowercase
n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(L[:0:-1]+L)'''





















