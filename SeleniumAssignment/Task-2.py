from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://evaly.com.bd/brands/xiaomi-004a023b8?category=speaker-2f615cf9a")
print(driver.title)



