import os
import time
IS_CI = os.getenv("CI") == "true"
if not IS_CI:
    import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class FileUploadPage:
    def __init__(self, browser):
        self.browser = browser
        self.upload_button = "//input[@id='file-upload']"

    def upload_file(self):
            filepath = os.path.join(os.getcwd(),"screenshots"," -- @1.3 .png")
            uploadbtn = self.browser.find_element(By.XPATH,self.upload_button)

            action = ActionChains(self.browser)
            action.move_to_element(uploadbtn).click().perform()

            pyautogui.write(filepath)
            pyautogui.press("enter") # This may cause problem while running on CICD
            time.sleep(5)

