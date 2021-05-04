from Main.Prerequisites.LocalExpressClasses.Class_Global.FastFunctions import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_NavigationBar.UserMenuMobile import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_StoresSection.HeaderMenu import *
from Utilities.DataDrivenTesting import DataDrivenTesting
import Automation.MyLogger as myLogger
from selenium.webdriver.common.by import By
from TestData.ENVs import Env


class PopUp_SignInMarketplace():
    def __init__(self, driver):
        self.driverParam = driver
        self.headerMenu = HeaderMenu(self.driverParam)
        self.fastFunctions = FastFunctions(self.driverParam)
        self.userMenuMobile = UserMenuMobile(self.driverParam)

    def signInPopUpValidation(self):
        #Todo
        print(" ")

    def fillDataAndPressSignIn(self, logIn, password):
        self.fillEmail(logIn)
        self.fillPassword(password)
        self.clickSignInButton()

    def fillEmail(self, email):
        emailField = self.driverParam.find_element(By.XPATH, "//input[@name='credentials[email]']")
        emailField.clear()
        emailField.send_keys(email)

    def fillPassword(self, password):
        passwordField = self.driverParam.find_element(By.XPATH, "//input[@name='credentials[password]']")
        passwordField.clear()
        passwordField.send_keys(password)

    def clickSignInButton(self):
        self.driverParam.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()

    def closePopUp(self):
        self.driverParam.find_element(By.XPATH, "//*[@id='sign-in-popup']/div/div/div[1]/a").click()

    def signInDDT(self):
        testData = DataDrivenTesting.getLogInAndPasswordsFromFile()
        #ToDo Make sure dor SignIn popup opened, if not open it
        for i in testData:
            self.fillDataAndPressSignIn(str(i['userName']), str(i['password']))
            if i['result'] == "Valid" and self.headerMenu.isSignedIn():
                self.fastFunctions.fastSignUp()
                self.userMenuMobile.openUserMenuMobileDropdown()
                self.userMenuMobile.clickSignInDropdownMenuButton()
                continue
            elif self.headerMenu.isNotSignedIn() and i['result'] == "InValid":
                continue
            else:
                myLogger.logger("ERROR", "Bad result during LogIn DDT", Env.logFilePath)
                self.driverParam.save_screenshot(Env.screenshotFilePath + "6.png")
                exit(6)
        self.closePopUp()





