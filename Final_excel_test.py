import datetime
import xlrd
import sys
wb=xlrd.open_workbook("C:\\Users\\admin\\Google Drive\\acharya\\python\\Copy_Input.xls")
sheet = wb.sheet_by_name("Volume")
fh=open("C:\\Users\\admin\\Google Drive\\acharya\\python\\Short_test.csv","wb")
sys.stdout=fh
print "Assigned,Month,Tickets opened"
for row in  range(sheet.nrows):
    for column in range(sheet.ncols):
        if sheet.row_values(row)[column]=="LQ DSL" or sheet.row_values(row)[column]=="LQ ETH" or sheet.row_values(row)[column]=="LC DSL" or sheet.row_values(row)[column]=="LC ETH":
            for i in range(1,len(sheet.row_values(row+1))):
                a1 = datetime.datetime(*xlrd.xldate_as_tuple(sheet.row_values(row)[i],wb.datemode))
                print "%s,%s,%s"%(sheet.col_values(column)[row],a1.strftime("%y-%b"),sheet.row_values(row + 1)[i])
fh.close()