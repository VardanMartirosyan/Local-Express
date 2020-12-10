from Automation.FunctionalityLib import *
from selenium.webdriver.common.by import By


class UserMenuMobile:
    @staticmethod
    def openUserMenuMobileDropDown(driverParam):
        UserMenuMobile.userMenuMobileDropdownShouldBeClosedValidation(driverParam)
        UserMenuMobile.openUserMenuMobileDropdown(driverParam)
        UserMenuMobile.userMenuMobileDropdownContentValidation(driverParam)

    @staticmethod
    def clickSignInDropdownMenuButton(driverParam):
        driverParam.find_element(By.XPATH, "//a[contains(text(),'Sign In')]").click()
        #driverParam.find_element(By.XPATH, "//*[@id='header-user-menu']/div")

    @staticmethod
    def userMenuMobileDropdownShouldBeClosedValidation(driverParam):
        ElementShouldNotBeVisible(driverParam, "//*[@class='open']")

    @staticmethod
    def openUserMenuMobileDropdown(driverParam):
        driverParam.find_element(By.XPATH, "//*[@id='user-menu-mobile']/i").click()

    @staticmethod
    def userMenuMobileDropdownContentValidation(driverParam):
        ElementShouldBeVisible(driverParam, "//*[@class='open']")
        ElementShouldBeVisible(driverParam, "//*[@class='open']/ul/li[1]")
        ElementShouldBeVisible(driverParam, "//*[@class='open']/ul/li[2]")
        ElementShouldBeVisible(driverParam, "//*[@class='open']/ul/li[3]")
        ElementShouldBeVisible(driverParam, "//*[@class='open']")
