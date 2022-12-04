#Name: A.MANOJ
#Date: 04/12/2022
#Project: Develop automation for user.management.Tool by.adding a.user

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

admin_user = "Admin"
admin_password = "admin123"
first_name = "manoj38"
last_name = "anba38"
full_name = first_name + " "+last_name 
user_name = "manoj038"
password = "Manojarm1208#"




driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
driver.maximize_window()
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys(admin_user)
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys(admin_password)
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(5)

driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
time.sleep(5)
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a').click()
time.sleep(3)
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input').send_keys(first_name)

driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').send_keys(last_name)

driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
time.sleep(1)

driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i').click()
userrolelistbox = driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[@role="listbox"]')
actions = ActionChains(driver)
actions.move_to_element(userrolelistbox)
Adminelement = driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[@role="listbox"]/div[3]')
actions.move_to_element(Adminelement).click().perform()

driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i').click()
statuslistbox = driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[@role="listbox"]')
actions = ActionChains(driver)
actions.move_to_element(statuslistbox)
Enabledelement = driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[@role="listbox"]/div[2]')
actions.move_to_element(Enabledelement).click().perform()

#username
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').click()
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').send_keys(user_name)

#password
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').click()
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys(password)

#confirmpassword
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').click()
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys(password)


#employee name
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys(full_name)
time.sleep(2)
WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]')))
time.sleep(1)
actions.move_to_element(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]'))
time.sleep(1)
Emp_Name=driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]/div')
time.sleep(1)
for i in Emp_Name:
    if i.text == full_name:
        actions.move_to_element(i).click().perform()


driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click()

time.sleep(7)


#Logout from the Admin user
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p').click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()
time.sleep(5)

#Login with Added User Employee
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys(user_name)
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys(password)
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(5)



