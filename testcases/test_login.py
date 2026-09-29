import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage

class MYTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com/")
        self.lp=LoginPage(self.driver)

    def test_login(self):
      self.lp.login_function("testmorning","test123")
      expected_result = "Welcome testmorning"
      actual_result = self.driver.find_element(By.ID, "nameofuser").text  # Get the text of the welcome message
      self.assertEqual(expected_result, actual_result, "User was not successful")

    def test_login_negative(self):
        self.lp.login_function("testmorning","test1234")
        actual_result = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        expected_result = "Wrong password."
        self.assertEqual(expected_result, actual_result, "User was successful")

def tearDown(self):
        self.driver.quit()
if __name__=="__main__":
    unittest.main()