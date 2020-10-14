from selenium import webdriver
from time import sleep
import xlrd
from Excel_read import xlsxreader

def status():
    return "Done"

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

#usr=input('Enter Email Id:')
#pwd=input('Enter Password:')
loc = (r"details.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
c=0
for i in range(sheet.nrows):
    usr = sheet.cell_value(i + 1, 0)
    pwd = sheet.cell_value(i + 1, 1)
    if c == 0:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://www.facebook.com/')
        c = 1


    print ("Opened facebook")
    sleep(1)

    username_box = driver.find_element_by_id('email')
    username_box.send_keys(usr)
    print ("Email Id entered")
    sleep(1)

    password_box = driver.find_element_by_id('pass')
    password_box.send_keys(pwd)
    print ("Password entered")

    login_box = driver.find_element_by_name('login')
    login_box.click()


    print(status())
    sleep(5)
    
    driver.get('https://www.facebook.com/')
    print("Finished")

