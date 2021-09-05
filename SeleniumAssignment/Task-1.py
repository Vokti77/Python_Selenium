from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://evaly.com.bd/")

print(driver.title)


driver.find_element_by_css_selector('button.absolute').click()
driver.find_element_by_css_selector('button.flex span span.p-2').click()

username = driver.find_element(By.NAME, 'phone')
username.send_keys("01931611577")

password = driver.find_element(By.NAME, "password")
password.send_keys("Bangladesh@1")

login_btn = driver.find_element(By.CLASS_NAME, 'btn')
login_btn.click()

# driver.find_element(By.LINK_TEXT, 'Speaker').click()
speaker = driver.get("https://evaly.com.bd/categories/speaker-2f615cf9a")
brandName = driver.find_elements(By.CLASS_NAME, 'BrandCard___StyledP-sc-1kq2v0k-1')
# print(brandName.text)
for ele in brandName:
    print(ele.text)

time.sleep(5)