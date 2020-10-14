from typing import List, Any

import xlrd


def xlsxreader():
    loc = (r"C:\Users\Training\PycharmProjects\Automation\details.xlsx")

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    for i in range(sheet.nrows):
        usr = sheet.cell_value(i + 1, 0)
        pwd = sheet.cell_value(i + 1, 1)
        print("{} {}".format(usr, pwd))
        return usr+" "+pwd

    # print("{} {}" .format((sheet.cell_value(i+1, 0)),(sheet.cell_value(i + 1, 1))))
