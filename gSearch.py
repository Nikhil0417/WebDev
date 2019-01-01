from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#driver = webdriver.Firefox()
driver = webdriver.Chrome()

#FACEBOOK
# driver.get("http://www.facebook.com")
# #driver.get("Iron Man")
# email = driver.find_element_by_xpath('//*[@id="email"]') #q is for google search bar
# password = driver.find_element_by_xpath('//*[@id="pass"]')
# #inputElement.send_keys("Sai Nikhil Reddy Mettupally")
# submit = driver.find_element_by_xpath('//*[@id="u_0_2"]')
# email.send_keys("+919490431864")
# password.send_keys("HelloWorld")
# submit.submit()

# WebDriverWait(driver,200)
# #WebDriverWait(driver, 10).until(EC.title_contains("Grant"))
# print(driver.title)

#AMAZON
driver.get("https://www.amazon.com")

search = driver.find_element_by_id("twotabsearchtextbox")

s = "ipad"
search.send_keys(s)
search.submit()

WebDriverWait(driver, 10).until(EC.title_contains(s))
print(driver.title)
#filter = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[3]/div[3]/div[2]/ul[10]/div/li[1]/span/a/i/span")
#filter = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div[3]/div[2]/ul[5]/div/li[1]/span/a')
#filter = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div[3]/div[2]/ul[13]/div/li[1]/span/a')
driver.find_element_by_partial_link_text("Tablet Cases").click()
#filter.submit()

#4.5 out of 5 stars