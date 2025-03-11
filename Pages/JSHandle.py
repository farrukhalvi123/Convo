from selenium.webdriver.common.by import By

class JSHandle():
    def __init__(self,browser):
        self.browser = browser
    #Generic method that can handle any type of Browser Alerts
    def popup_appear(self,popuptype):
        try:
            self.JSalertbtn = "//button[normalize-space()='Click for JS Alert']"
            self.JSConfirm = "//button[normalize-space()='Click for JS Confirm']"
            self.JSprompt = "//button[normalize-space()='Click for JS Prompt']"

            popbtn = {
                "alert": self.JSalertbtn,
                "confirm": self.JSConfirm,
                "prompt": self.JSprompt
            }
            if popuptype in popbtn:
                self.browser.find_element(By.XPATH,popbtn[popuptype]).click()
        except Exception as e:
            print("Error: Unable to locate popup button")

    def handling_popup(self,action="accept", text=None):
        try:
            alert = self.browser.switch_to.alert
            print(f"text present in Pop up",{alert.text})
            if action == "input" and text is None:
                alert.send_keys("Hello")
                alert.accept()
            elif action == "accept":
                alert.accept()
            elif action == "dismiss":
                alert.dismiss()
            else:
                raise ValueError("Invalid Action for popup")
        except Exception as e:
            print("No Pop up found")









