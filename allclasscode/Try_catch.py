import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

driver = webdriver.Chrome()  # Opens Chrome browser
driver.maximize_window()
driver.get("https://demoblaze.com/")

try:
    nav_login = driver.find_element(By.ID, "login2")
    nav_login.click()
    driver.implicitly_wait(2)
    txt_username = driver.find_element(By.ID, "loginusername")
    txt_username.send_keys("testmorning")
    txt_password = driver.find_element(By.ID, "loginpassword")
    txt_password.send_keys("test123")
    btn_login = driver.find_element(
        By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]"
    )
    btn_login.click()

except ElementNotInteractableException as e:
    print(f"Element not interactable: {e}")

except Exception as e:
    print(f"An error occurred: {e}")

time.sleep(5)
driver.quit()