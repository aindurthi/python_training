from datetime import datetime
import xlrd
wb=xlrd.open_workbook("C:\\Users\\admin\\Google Drive\\acharya\\python\\Copy_Input.xls")
sheet = wb.sheet_by_name("Volume")
file_name=open("C:\\Users\\admin\\Google Drive\\acharya\\python\\test.csv",'wb')
lists=[0,10,19,29]
print "assigned","DATE","Ticket"
'''for col in range(sheet.ncols):
    for row in range(sheet.nrows):
        if row in lists:
            if row == 0:
                array1=datetime.datetime(*xlrd.xldate_as_tuple(sheet.row_values(rowx=row),wb.datemode)
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
    print array4[0], array4[i],ar4[i]'''
file_name.close()