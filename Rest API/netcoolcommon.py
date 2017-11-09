string=['tejaswi','tejaswini','tea','temperature','saketh','saikiran','sainath']
str=''
a=len(string)
for i in range(a):
     b=len(string[i])
     for j in range(b):
         if string[i][j] in string[i][j]:
             print string[i][j]