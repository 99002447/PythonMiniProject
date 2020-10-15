from selenium import webdriver
from time import sleep
import xlrd
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
def status():
    return "Finished"
#usr=input('Enter Email Id:')
#pwd=input('Enter Password:')
loc = r"details.xlsx"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
newtabblocker=0

for i in range(sheet.nrows):
    try:
        usr = sheet.cell_value(i + 1, 0)
        pwd = sheet.cell_value(i + 1, 1)
        if newtabblocker == 0:
           #driver = webdriver.Chrome(ChromeDriverManager().install())
           chrome_options = webdriver.Options()

           chrome_options.add_argument('--headless')
           driver = webdriver.Chrome(r'./linux',
                                    chrome_options=chrome_options,
                                    service_args=['--verbose'])
           driver.get('https://www.facebook.com')
           newtabblocker = 1


           print ("Opened Facebook")
           sleep(1)

           username_box = driver.find_element_by_id('id_userLoginId')
           username_box.send_keys(usr)
           print ("Email Id entered")
           sleep(1)

        password_box = driver.find_element_by_id('id_password')
        password_box.send_keys(pwd)
        print ("Password entered for {}".format(usr))
       # driver.find_element_by_id('id_password').send_keys(Keys.ENTER)

        login_box = driver.find_element_by_id('submit')
        login_box.click()


        print ("Done")
        sleep(5)
    except:
            driver.get('https://www.facebook.com/login')
            print(status())


