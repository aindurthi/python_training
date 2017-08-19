from datetime import datetime
import xlrd
import sys
wb=xlrd.open_workbook("C:\\Users\\admin\\Google Drive\\acharya\\python\\Copy_Input.xls")
sheet = wb.sheet_by_name("Volume")
test=sys.stdout
f=open("C:\\Users\\admin\\Google Drive\\acharya\\python\\test.csv","wb")
sys.stdout=f
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
#print ','.join(str(p) for p in array1)
print "Assigned,Month,Tickets opened"
for i in range(1,len(dict(zip(array1,ar1)))):
    a1_tuple = xlrd.xldate_as_tuple(array1[i], wb.datemode)
    a1_datetime = datetime(*a1_tuple)
    print "%s,%s,%s"%(array1[0],a1_datetime.strftime("%y-%b"),ar1[i])
for i in range(1,len(dict(zip(array2,ar2)))):
    a2_tuple = xlrd.xldate_as_tuple(array2[i], wb.datemode)
    a2_datetime = datetime(*a2_tuple)
    print "%s,%s,%s"%(array2[0],a2_datetime.strftime("%y-%b"),ar2[i])
for i in range(1,len(dict(zip(array3,ar3)))):
    a3_tuple = xlrd.xldate_as_tuple(array3[i], wb.datemode)
    a3_datetime = datetime(*a3_tuple)
    print "%s,%s,%s"%(array3[0],a3_datetime.strftime("%y-%b"),ar3[i])
for i in range(1,len(dict(zip(array4,ar4)))):
    a4_tuple = xlrd.xldate_as_tuple(array4[i], wb.datemode)
    a4_datetime = datetime(*a4_tuple)
    print "%s,%s,%s"%(array4[0],a4_datetime.strftime("%y-%b"),ar4[i])
sys.stdout=test
f.close()
