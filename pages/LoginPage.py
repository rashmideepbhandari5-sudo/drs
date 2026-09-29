import time

from selenium.webdriver.common.by import By
from locator.Locater import Locate

class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.lc=Locate()

    def get_login_nav(self):
        return self.driver.find_element("id",self.lc.login_nav_id)

    def click_login_nav(self):
        self.get_login_nav().click()

    def get_username(self):
         self.driver.implicitly_wait(10)
         return self.driver.find_element(By.ID, self.lc.username_id)

    def enter_username(self,username):
        self.get_username().send_keys(username)

    def get_password(self):
        return self.driver.find_element(By.ID, self.lc.password_id)

    def enter_password(self, password):
        self.get_password().send_keys(password)

    def get_login_button(self):
        return  self.driver.find_element(By.XPATH,self.lc.button_xpath)

    def click_login(self):
        self.get_login_button().click()

    def login_function(self,username,password):
       self.click_login_nav()
       self.driver.implicitly_wait(10)
       self.enter_username(username)
       self.enter_password(password)
       self.click_login()
       time.sleep(5)

