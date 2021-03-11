from selenium.webdriver.common.by import By
from Automation.FunctionalityLib import *

class HeaderMenu:
    @staticmethod
    def isSignInValidation(driverParam):
        driverParam.find_element(By.XPATH, "//*[@id='header-user-menu']/div")

    @staticmethod
    def clientIsNotSignedIn(driverParam):
        driverParam.find_element(By.XPATH, "//*[@id='user-menu-mobile']")
        ElementShouldNotBeVisible(driverParam, "//*[@id='header-user-menu']/div")

    @staticmethod
    def clientWasSignedIn(driverParam):
        driverParam.find_element(By.XPATH, "//*[@id='header-user-menu']/div")
        ElementShouldNotBeVisible(driverParam, "//*[@id='user-menu-mobile']")

