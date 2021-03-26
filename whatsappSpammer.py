from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("user-data-dir=/home/adi/.config/google-chrome/Default") #Replace with absolute chromedriver path in your computer

driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
driver.get("https://web.whatsapp.com/")
	        # time.sleep()
wait = WebDriverWait(driver, 600)
for i in range(0,100):
	target = '"Shreya Raghunandan"' #Name of target to be spammed
	string = "Sup girl" #Message to be sent
	x_arg = '//span[contains(@title,' + target + ')]'
	group_title = wait.until(EC.presence_of_element_located((
	By.XPATH, x_arg)))
	group_title.click()
	message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

	message.send_keys(string)
	sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
	sendbutton.click()
driver.close()
