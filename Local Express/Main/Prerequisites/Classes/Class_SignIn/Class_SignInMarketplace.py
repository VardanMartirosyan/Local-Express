from Automation.FunctionalityLib import *
from selenium.webdriver.common.by import By

class ClassSignInMarketplace:
    def fillDataAndPressSignIn(self, driverParam):
        self.fillSignInData(driverParam, "vardanm@local.express", "Q11111111")
        driverParam.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()

    def openUserMenuMobileDropDownAndPressSignInButton(self):
        self.openUserMenuMobileDropdownAndValidation()
        self.clickIntoSignInButtonAndValidate()


    def openUserMenuMobileDropdownAndValidation(self, driverParam):
        ElementShouldNotBeVisible(driverParam, "//*[@class='open']")
        userMenuIcon = driverParam.find_element(By.XPATH, "//*[@id='user-menu-mobile']/i")
        userMenuIcon.click()
        ElementShouldBeVisible(driverParam, "//*[@class='open']")

    def clickIntoSignInButtonAndValidate(self, driverParam):
        driverParam.find_element(By.XPATH, "//a[contains(text(),'Sign In')]").click()
        driverParam.find_element(By.XPATH, "//*[@id='header-user-menu']/div")

    def fillSignInData(self, driverParam, mail, password):
        ElementShouldBeVisible(driverParam, "//input[@name='credentials[email]']")
        driverParam.find_element(By.XPATH, "//input[@name='credentials[email]']").send_keys(mail)
        driverParam.find_element(By.XPATH, "//input[@name='credentials[password]']").send_keys(password)

