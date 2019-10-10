from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os,sys
import time, random
import datetime

#---подключение драйвера chrome в текущей директории и добавление куки
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
path= str(os.getcwd()) + r"\chromedriver.exe" 
driver = webdriver.Chrome(executable_path=path, options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data") 

f = open("log.txt",'a') 
#---заходим в инстаграм
driver.get('https://www.instagram.com/')

token = 10
while(True):
    try:
        today = datetime.datetime.today()
        try:
            like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Нравится"]')
            like_button().click()
            f.write( today.strftime("%d.%m.%Y \t %H:%M:%S \t\t"))
            f.write(str(token) + " Good\n")
        except:
            #f.write( today.strftime("%d.%m.%Y \t %H:%M:%S \t\t"))
            print("!")
            #f.write(str(token) + " Pass\n")
        driver.execute_script("window.scrollTo(0, " + str(token) + ");") # идем вверх
        token = token + 150
        print(token)
        random_id=100 + random.randint(1,27)
        random_id = random_id/50
        print(random_id)
        time.sleep(random_id)
    except KeyboardInterrupt:
        print("Ok ok, quitting")
        sys.exit(1)

