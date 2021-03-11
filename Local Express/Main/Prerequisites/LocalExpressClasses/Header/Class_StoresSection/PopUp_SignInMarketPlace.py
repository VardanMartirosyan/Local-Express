from Automation.FunctionalityLib import *
from selenium.webdriver.common.by import By
from Main.Environment import Env
from Main.Prerequisites.LocalExpressClasses.Header.Class_StoresSection.HeaderMenu import *


class PopUp_SignInMarketplace:
    @staticmethod
    def SignInPopUpValidation(driverParam):
        #Todo
        print(" ")

    @staticmethod
    def fillDataAndPressSignIn(driverParam, logIn, password):
        PopUp_SignInMarketplace.fillEmail(driverParam, logIn)
        PopUp_SignInMarketplace.fillPassword(driverParam, password)
        PopUp_SignInMarketplace.clickSignInButton(driverParam)
        HeaderMenu.isSignInValidation(driverParam)


    @staticmethod
    def fillEmail(driverParam, email):
        driverParam.find_element(By.XPATH, "//input[@name='credentials[email]']").send_keys(email)

    @staticmethod
    def fillPassword(driverParam, password):
        driverParam.find_element(By.XPATH, "//input[@name='credentials[password]']").send_keys(password)

    @staticmethod
    def clickSignInButton(driverParam):
        driverParam.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()

