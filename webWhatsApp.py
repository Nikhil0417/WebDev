from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

#driver = webdriver.Firefox()
driver = webdriver.Chrome()

#Whatsapp
l = ['tesla', 'vmware']
for i in l:
	s = i+' '+'careers'

	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
	driver.get("https://www.google.com")
	search = driver.find_element_by_name('q')
	
	search.send_keys(s)
	search.submit()

	WebDriverWait(driver, 10).until(EC.title_contains(s))
	print(driver.title)
#driver.find_element_by_partial_link_text("Tablet Cases").click()
#filter.submit()

#4.5 out of 5 stars