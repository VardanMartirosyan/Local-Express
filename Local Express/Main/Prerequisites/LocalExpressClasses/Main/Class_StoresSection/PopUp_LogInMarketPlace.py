from Automation.FunctionalityLib import *
from selenium.webdriver.common.by import By
from Main.Common import Env


class PopUp_LogInMarketplace:
    @staticmethod
    def SignInPopUpValidation(driverParam):
        #Todo
        print(" ")

    @staticmethod
    def fillDataAndPressSignIn(driverParam):
        PopUp_LogInMarketplace.fillEmail(driverParam, Env.WebTestingLogIn)
        PopUp_LogInMarketplace.fillPassword(driverParam, Env.WebTestingPassword)
        PopUp_LogInMarketplace.clickSignInButton(driverParam)

    @staticmethod
    def fillEmail(driverParam, email):
        driverParam.find_element(By.XPATH, "//input[@name='credentials[email]']").send_keys(email)

    @staticmethod
    def fillPassword(driverParam, password):
        driverParam.find_element(By.XPATH, "//input[@name='credentials[password]']").send_keys(password)

    @staticmethod
    def clickSignInButton(driverParam):
        driverParam.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()

