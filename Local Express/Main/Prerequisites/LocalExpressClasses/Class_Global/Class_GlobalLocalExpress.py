import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from Main.Prerequisites.LocalExpressClasses.Header.Class_StoresSection.HeaderMenu import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_StoresSection.PopUp_SignInMarketPlace import PopUp_SignInMarketplace


class GlobalLocalExpress:
    def __init__(self, driver):
        self.driverParam = driver
        self.popUp_SignInMarketplace = PopUp_SignInMarketplace(self.driverParam)
        self.headerMenu = HeaderMenu(self.driverParam)

    def fastSignIn(self, email, password):
        self.driverParam.find_element(By.XPATH, "//*[@id='user-menu-mobile']/i").click()
        self.driverParam.find_element(By.XPATH, "//a[contains(text(),'Sign In')]").click()
        self.popUp_SignInMarketplace.fillEmail(email)
        self.popUp_SignInMarketplace.fillPassword(password)
        self.popUp_SignInMarketplace.clickSignInButton()
        self.headerMenu.isSignInValidation()

    def fastSignUp(self):
        self.driverParam.find_element(By.XPATH, "//*[@id='header-user-menu']/div").click()
        self.driverParam.find_element(By.LINK_TEXT, "Sign Out").click()

    def tearDown(self):
        if self.driverParam.find_element(By.XPATH, "//*[@id='header-user-menu']/div"):
            #TODO
            #i can not call funtion here
            #Cart.closeCart(driverParam)
            self.driverParam.find_element(By.XPATH, "//*[@id='header-user-menu']/div").click()
            self.driverParam.find_element(By.LINK_TEXT, "Sign Out").click()
            #TODO
            #fastSignUp(driverParam)
            self.driverParam.close()
        elif driverParam.find_element(By.XPATH, "//*[@id='user-menu-mobile']"):
            print("Any Message")
            self.driverParam.close()

    def setLALocation(self):
        #driverParam.find_element(By.NAME, "filter[address]").clear().send_keys("455 n louise St, Glandle, CA" + Keys.ENTER)
        self.driverParam.implicitly_wait(20)
        locationField = self.driverParam.find_element(By.NAME, "filter[address]")
        locationField.clear()
        locationField.send_keys("455 N Louise St, Glendale, CA")
        time.sleep(7)
        self.driverParam.find_element(By.XPATH, "//span[contains(text(),'455 N Louise St, Glendale, CA 91206, USA')]").click()
        self.driverParam.implicitly_wait(10)





