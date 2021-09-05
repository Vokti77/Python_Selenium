from Tools.scripts.win_add2path import PATH
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://evaly.com.bd/career")
print(driver.title)

driver.find_element(By.XPATH, '/html/body/reach-portal[1]/div/div/div/section/div/button').click()
driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/button').click()
career = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div')

for i in range(len(career)):
    career[i].click()

DomainName = driver.find_elements(By.XPATH, "//div[@class='p-6 mb-6']//p//a")
for e in DomainName:
    index =(str)(e.text).index("career@evaly.com.bd")
    if index == index:
        print("Domain Name is Available")
    else:
        print("Domain Name Not Found!")

driver.close()
time.sleep(10)