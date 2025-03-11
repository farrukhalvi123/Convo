import os
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FileUploadPage:
    def __init__(self, browser):
        self.browser = browser
        self.upload_button = "//input[@id='file-upload']"

    def upload_file(self):
        # try:
            filepath = os.path.join(os.getcwd(),"screenshots","Testing upload functionality with pyautogui.png")
            uploadbtn = self.browser.find_element(By.XPATH,self.upload_button)
            self.browser.execute_script("arguments[0].style.display = 'block'; arguments[0].setAttribute('value', arguments[1]);", filepath,uploadbtn)
            time.sleep(3)

