from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By

class GlobalLocalExpress:
    @staticmethod
    def openGCAndCustomizeiBrowserSettings(driverParam):
        driverParam = webdriver.Chrome(ChromeDriverManager().install())
        driverParam.maximize_window()
        driverParam.implicitly_wait(5)
        return driverParam

    #Copy
    @staticmethod
    def openLocalExpressAndValidate(driverParam):
        driverParam.get("https://local.express/stores")
        GlobalLocalExpress.LocalExpressValidation(driverParam)

    #Copy
    @staticmethod
    def LocalExpressValidation(driverParam):
        assert "Find a store" in driverParam.title
        driverParam.find_element(By.NAME, "search-store")

    @staticmethod
    def tearDown(driverParam):
        driverParam.close()




