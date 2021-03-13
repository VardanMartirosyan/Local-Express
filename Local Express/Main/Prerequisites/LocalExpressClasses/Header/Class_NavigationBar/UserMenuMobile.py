from Automation.FunctionalityLib import *
from selenium.webdriver.common.by import By


class UserMenuMobile:
    def __init__(self, driver):
        self.driverParam = driver

    def openUserMenuMobileDropdown(self):
        self.userMenuMobileDropdownShouldBeClosedValidation()
        self.clickInUserMenuMobileDropdown()
        self.userMenuMobileDropdownContentValidation()

    def clickSignInDropdownMenuButton(self):
        self.driverParam.find_element(By.XPATH, "//a[contains(text(),'Sign In')]").click()

    def userMenuMobileDropdownShouldBeClosedValidation(self):
        ElementShouldNotBeVisible(self.driverParam, "//*[@class='open']")

    def clickInUserMenuMobileDropdown(self):
        self.driverParam.find_element(By.XPATH, "//*[@id='user-menu-mobile']/i").click()

    def userMenuMobileDropdownContentValidation(self):
        self.driverParam.find_element(By.XPATH, "//*[@class='open']")
        self.driverParam.find_element(By.XPATH, "//*[@class='open']/ul/li[1]")
        self.driverParam.find_element(By.XPATH, "//*[@class='open']/ul/li[2]")
        self.driverParam.find_element(By.XPATH, "//*[@class='open']/ul/li[3]")
