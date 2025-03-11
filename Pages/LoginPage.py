from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage():
    def __init__(self, browser):
        self.browser = browser
        self.uname = "username"
        self.pwd = "password"
        self.loginbtn = "//button[@type='submit']"
        self.logoutbtn = "//a[@href='/logout']"

    def user_login(self,usname,pwd):
        try:
            self.browser.find_element(By.ID,self.uname).send_keys(usname)
            self.browser.find_element(By.ID,self.pwd).send_keys(pwd)
            self.browser.find_element(By.XPATH,self.loginbtn).click()
        except Exception as e:
            print("Error Username or Password not found or incorrect ")




    def postlogin(self):
       try:
        logoutbtn = WebDriverWait(self.browser, 10).until(presence_of_element_located((By.XPATH,self.logoutbtn)))
        assert logoutbtn.is_displayed();
       except Exception as e:
           print("Error: Invalid User credentials")
           self.browser.save_screenshot("loginfailed.png")
