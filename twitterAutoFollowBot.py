from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("user-data-dir=/home/adi/.config/google-chrome/Default")
	        # Replace below path with the absolute path of the 
	        #chromedriver in your computer
driver = webdriver.Chrome(r'/home/adi/Downloads/chromedriver',chrome_options=options)
driver.get("https://twitter.com/search?q=%23DotNet&src=typed_query&f=user")
wait = WebDriverWait(driver, 600)
# x_arg = '//span[contains(@class,' + 'css-1dbjc4n r-18u37iz r-1wbh5a2 r-1f6r7vd' + ')]'
new_usernames_followed=[]
#x_arg='//span[contains(@class,' + 'css-901oao css-bfa6kz r-hkyrab r-1qd0xha r-a023e6 r-vw2c0b r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0'+')]'
#group_title=wait.until(EC.element_to_be_clickable((By.XPATH, x_arg)))


driver.set_window_size(480, 680)
for i in range(0,100):
	driver.implicitly_wait(20)
	group_title_buttons=driver.find_elements_by_xpath("//div[@class='css-18t94o4 css-1dbjc4n r-1niwhzg r-p1n3y5 r-sdzlij r-1phboty r-rs99b7 r-1w2pmg r-1vsu8ta r-aj3cln r-1ny4l3l r-1fneopy r-o7ynqc r-6416eg r-lrvibr' or @class='css-18t94o4 css-1dbjc4n r-urgr8i r-42olwf r-sdzlij r-1phboty r-rs99b7 r-1w2pmg r-1vsu8ta r-aj3cln r-1ny4l3l r-1fneopy r-o7ynqc r-6416eg r-lrvibr']")#find_element_by_class_name("css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")
	group_title_usernames=driver.find_elements_by_xpath("//div[@class='css-1dbjc4n r-18u37iz r-1wbh5a2']")
	print(len(group_title_buttons))
	print(len(group_title_usernames))
	for i in range(0,len(group_title_buttons)):
		print("-"*40)
		if group_title_buttons[i].text=="Following":
			print("Already following: " + str(group_title_usernames[i].text))
		else:
			print("Now following: "+ str(group_title_usernames[i].text))
			driver.execute_script("arguments[0].click();", group_title_buttons[i])
			print("Followed: " + str(group_title_usernames[i].text))
			new_usernames_followed.append(group_title_usernames[i].text)
			
			#group_title_buttons[i].click()
	driver.execute_script("window.scrollBy(0,1000)")
	time.sleep(5)

print("Followed " + str(len(new_usernames_followed)) + " new users")

with open('followed.txt', 'w') as f:
    for item in new_usernames_followed:
        f.write("%s\n" % item)

print("Usernames saved in followed.txt")
#group_title[0].click()
