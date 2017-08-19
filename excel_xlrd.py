from datetime import datetime
import xlrd
import csv
import pandas as pd
wb=xlrd.open_workbook("C:\\Users\\admin\\Google Drive\\acharya\\python\\Copy_Input.xls")
sheet = wb.sheet_by_name("Volume")
lists=[0,10,19,29]
array1,array2,array3,array4=[],[],[],[]
ar1,ar2,ar3,ar4=[],[],[],[]
for col in range(sheet.ncols):
    for row in range(sheet.nrows):
        if row in lists:
            if row == 0:
                array1=sheet.row_values(rowx=row)
                ar1.append(sheet.cell_value(rowx=row+1,colx=col))
            if row == 10:
                array2=sheet.row_values(rowx=row)
                ar2.append(sheet.cell_value(rowx=row+1, colx=col))
            if row == 19:
                array3=sheet.row_values(rowx=row)
                ar3.append(sheet.cell_value(rowx=row+1, colx=col))
            if row == 29:
                array4=sheet.row_values(rowx=row)
                ar4.append(sheet.cell_value(rowx=row+1, colx=col))


for i in range(1,len(dict(zip(array1,ar1)))):
    print array1[0], array1[i],ar1[i]
for i in range(1,len(dict(zip(array2,ar2)))):
    print array2[0], array2[i], ar2[i]
for i in range(1,len(dict(zip(array3,ar3)))):
    print array3[0], array3[i],ar3[i]
for i in range(1,len(dict(zip(array4,ar4)))):
    print array4[0], array4[i],ar4[i]

'''for i in range(1,len(array2)):
    print array2[0],array2[i],ar2[i]
for i in range(1,len(array3)):
    print array3[0],array3[i]
for i in range(1,len(array4)):
    print array4[0],array4[i]'''

#for col in range(sheet.ncols):
 #   for row in range(sheet.nrows):
  #      if row in lists:
   #         if row ==

