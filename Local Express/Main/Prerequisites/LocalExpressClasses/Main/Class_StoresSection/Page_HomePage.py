from selenium.webdriver.common.by import By

class Page_HomePage:
    @staticmethod
    def isSignInValidation(driverParam):
        driverParam.find_element(By.XPATH, "//*[@id='header-user-menu']/div")
