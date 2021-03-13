from selenium.webdriver.common.by import By
from Automation.FunctionalityLib import *

class HeaderMenu:
    def __init__(self, driver):
        self.driverParam = driver

    def isSignInValidation(self):
        self.driverParam.find_element(By.XPATH, "//*[@id='header-user-menu']/div")

    def clientIsNotSignedIn(self):
        self.driverParam.find_element(By.XPATH, "//*[@id='user-menu-mobile']")
        ElementShouldNotBeVisible(self.driverParam, "//*[@id='header-user-menu']/div")

    def clientWasSignedIn(self):
        self.driverParam.find_element(By.XPATH, "//*[@id='header-user-menu']/div")
        ElementShouldNotBeVisible(self.driverParam, "//*[@id='user-menu-mobile']")

