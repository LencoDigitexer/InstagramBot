from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options #для сохранения куки в первый раз
import os 
import time
from data import login, password

#---подключение драйвера chrome в текущей директории и настройка куки
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
path= str(os.getcwd()) + r"\chromedriver.exe" 
driver = webdriver.Chrome(executable_path=path, options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data") 

#---заходим в инстаграм с...
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
time.sleep(3)
#elem_login = driver.find_element_by_name("username") #---... логином ...
elem_login = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
elem_login.send_keys(login)
elem_passwd = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
elem_passwd.send_keys(password)
elem_passwd.send_keys(Keys.RETURN)
time.sleep(50)
driver.close()
