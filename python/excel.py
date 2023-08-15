#how to use xlrd library and access data of excel files

import xlrd

loc=("C:\\Users\\DELL\\Desktop\\z.xls")    #avoid \u error by escape character
#latest xlrd function doesnt accept xlsx idk why

wb = xlrd.open_workbook(loc)

sheet= wb.sheet_by_index(0)

print ( sheet.cell_value(0,0))
print (sheet.ncols)
print(sheet.nrows)

for i in range(sheet.ncols):    #all columns
    print (sheet.cell_value(0,i))

print(sheet.row_values(1))