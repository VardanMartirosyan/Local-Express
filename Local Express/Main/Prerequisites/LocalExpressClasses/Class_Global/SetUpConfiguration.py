from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

class SetUpConfiguration:

    @staticmethod
    def openGCAndCustomizeiBrowserSettings():
        driverParam = webdriver.Chrome(ChromeDriverManager().install())
        driverParam.maximize_window()
        driverParam.delete_all_cookies()
        driverParam.implicitly_wait(10)
        return driverParam
