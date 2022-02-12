# coding=utf-8

import xlrd

def login_value():
    list1=[]
    file=r"C:\python\api_auto2\config\login.xls"
    book=xlrd.open_workbook(file)
    sheet=book.sheet_by_index(0)
    rows=sheet.nrows
    for i in range(rows):
        if i>0:
            value=sheet.row_values(i,0)
            list1.append(value)
    return list1


def queryuser_value():
    list1=[]
    file=r"C:\python\api_auto2\config\queryuser.xls"
    book=xlrd.open_workbook(file)
    sheet=book.sheet_by_index(0)
    rows=sheet.nrows
    for i in range(rows):
        if i>0:
            value=sheet.row_values(i,0)
            list1.append(value)
    return list1
if __name__ == '__main__':
    # print(login_value())
    print(queryuser_value())

