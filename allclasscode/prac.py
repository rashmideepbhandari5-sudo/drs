# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver= webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.automationtesting.in/Alerts.html")
#
# # alterwitok
# nav_with_ok=driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a')
# nav_with_ok.click()
# time.sleep(2)
# sim_button=driver.find_element(By.XPATH, '//*[@id="OKTab"]/button')
# sim_button.click()
# time.sleep(2)
# driver.switch_to.alert.accept()
#
# #alter with ok or cancel
# nav_with_cancel=driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a')
# nav_with_cancel.click()
# time.sleep(2)
# sim_button_cancel=driver.find_element(By.XPATH, '//*[@id="CancelTab"]/button')
# sim_button_cancel.click()
# time.sleep(2)
# driver.switch_to.alert.dismiss()
# time.sleep(5)
#
#
# # alert with text box
# nav_textbox=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a')
# nav_textbox.click()
# time.sleep(2)
# sim_textbox=driver.find_element(By.XPATH,'//*[@id="Textbox"]/button')
# sim_textbox.click()
# time.sleep(2)
# driver.switch_to.alert.send_keys("hello rashmi")
# driver.switch_to.alert.accept()
# time.sleep(5)



# facebook
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote import switch_to
#
# driver= webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.facebook.com/")
# username_or_email=driver.find_element(By.ID,"_R_c9l6neappb6amH1_")
# username_or_email.send_keys("9849304264")
# time.sleep(2)
# password=driver.find_element(By.ID,"_R_cdl6neappb6amH1_")
# password.send_keys("Rabindrabhandari123")
# time.sleep(2)
# login=driver.find_element(By.XPATH,"//*[@id='login_form']/div/div[1]/div/div[3]/div/div/div/div[1]")
# login.click()
# time.sleep(7)



# demoblaze
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome() # It will open the Edge browser
# driver.maximize_window() # Maximize the browser window
# driver.get("https://demoblaze.com/") # Open the Google website
#
# login=driver.find_element(By.ID, "login2")
# login.click()
# driver.implicitly_wait(5)
# # time.sleep(2)
# username_input=driver.find_element(By.ID, "loginusername")
# username_input.send_keys("testmorning")
# time.sleep(2)
# password_input=driver.find_element(By.ID, "loginpassword")
# password_input.send_keys("test123")
# time.sleep(2)
# login=driver.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]")
# login.click()
# time.sleep(5)