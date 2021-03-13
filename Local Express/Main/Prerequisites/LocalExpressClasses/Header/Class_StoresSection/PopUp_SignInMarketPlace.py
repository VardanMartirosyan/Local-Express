from Automation.FunctionalityLib import *
from selenium.webdriver.common.by import By
from Main.Environment import Env
from Main.Prerequisites.LocalExpressClasses.Header.Class_StoresSection.HeaderMenu import *


class PopUp_SignInMarketplace:
    def __init__(self, driver):
        self.driverParam = driver
        self.headerMenu = HeaderMenu(self.driverParam)

    def SignInPopUpValidation(self):
        #Todo
        print(" ")

    def fillDataAndPressSignIn(self, logIn, password):
        self.fillEmail(logIn)
        self.fillPassword(password)
        self.clickSignInButton()
        self.headerMenu.isSignInValidation()

    def fillEmail(self, email):
        self.driverParam.find_element(By.XPATH, "//input[@name='credentials[email]']").send_keys(email)

    def fillPassword(self, password):
        self.driverParam.find_element(By.XPATH, "//input[@name='credentials[password]']").send_keys(password)

    def clickSignInButton(self):
        self.driverParam.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()

