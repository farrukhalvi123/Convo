from Pages.DynamicTablePage import DynamicTablePage
from Pages.FileUploadPage import FileUploadPage
from Pages.JSHandle import JSHandle
from Pages.LoginPage import LoginPage
class herokuapp:
    def __init__(self,browser):
        self.browser = browser
        self.loginpage = LoginPage(browser)
        self.dynamicTablePage = DynamicTablePage(browser)
        self.jshandling = JSHandle(browser)
        self.upload = FileUploadPage(browser)