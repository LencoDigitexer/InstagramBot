from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options #для сохранения куки в первый раз
import os 
import time
import sys

#---подключение драйвера chrome в текущей директории и настройка куки
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
path= str(os.getcwd()) + r"\chromedriver.exe" 
driver = webdriver.Chrome(executable_path=path, options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data") 

#---логин с паролем
login = sys.argv[1]
passwd = sys.argv[2]

#---заходим в инстаграм с...
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
elem_login = driver.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input")#---... логином ...
elem_login.send_keys(login)
elem_passwd = driver.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input")#---... и паролем.
elem_passwd.send_keys(passwd)
elem_passwd.send_keys(Keys.RETURN)
time.sleep(50)
driver.close()
