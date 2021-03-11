from Automation.FunctionalityLib import *
from selenium.webdriver.common.by import By


class UserMenuMobile:
    @staticmethod
    def openUserMenuMobileDropdown(driverParam):
        UserMenuMobile.userMenuMobileDropdownShouldBeClosedValidation(driverParam)
        UserMenuMobile.clickInUserMenuMobileDropdown(driverParam)
        UserMenuMobile.userMenuMobileDropdownContentValidation(driverParam)

    @staticmethod
    def clickSignInDropdownMenuButton(driverParam):
        driverParam.find_element(By.XPATH, "//a[contains(text(),'Sign In')]").click()

    @staticmethod
    def userMenuMobileDropdownShouldBeClosedValidation(driverParam):
        ElementShouldNotBeVisible(driverParam, "//*[@class='open']")

    @staticmethod
    def clickInUserMenuMobileDropdown(driverParam):
        driverParam.find_element(By.XPATH, "//*[@id='user-menu-mobile']/i").click()

    @staticmethod
    def userMenuMobileDropdownContentValidation(driverParam):
        driverParam.find_element(By.XPATH, "//*[@class='open']")
        driverParam.find_element(By.XPATH, "//*[@class='open']/ul/li[1]")
        driverParam.find_element(By.XPATH, "//*[@class='open']/ul/li[2]")
        driverParam.find_element(By.XPATH, "//*[@class='open']/ul/li[3]")
