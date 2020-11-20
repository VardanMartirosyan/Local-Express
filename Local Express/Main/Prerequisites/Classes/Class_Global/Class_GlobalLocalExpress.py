from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

class GlobalLocalExpress:
    def openGCAndCustomizeiBrowserSettings(self, driverParam):
        driverParam = webdriver.Chrome(ChromeDriverManager().install())
        driverParam.maximize_window()
        driverParam.implicitly_wait(5)

    def openLocalExpressAndValidate(self, driverParam):
        driverParam.get("https://local.express/stores")
        self.LocalExpressValidation(driverParam)

    def LocalExpressValidation(self, driverParam):
        assert "Find a store" in driverParam.title
        driverParam.find_element(By.NAME, "search-store")

    def tearDown(self, driverParam):
        driverParam.close()




