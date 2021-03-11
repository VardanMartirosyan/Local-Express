import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from Main.Prerequisites.LocalExpressClasses.Header.Class_StoresSection.HeaderMenu import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_StoresSection.PopUp_SignInMarketPlace import PopUp_SignInMarketplace


class GlobalLocalExpress:
    @staticmethod
    def openGCAndCustomizeiBrowserSettings():
        driverParam = webdriver.Chrome(ChromeDriverManager().install())
        driverParam.maximize_window()
        driverParam.delete_all_cookies()
        driverParam.implicitly_wait(10)
        return driverParam

    @staticmethod
    def fastSignIn(driverParam, email, password):
        driverParam.find_element(By.XPATH, "//*[@id='user-menu-mobile']/i").click()
        driverParam.find_element(By.XPATH, "//a[contains(text(),'Sign In')]").click()
        PopUp_SignInMarketplace.fillEmail(driverParam, email)
        PopUp_SignInMarketplace.fillPassword(driverParam, password)
        PopUp_SignInMarketplace.clickSignInButton(driverParam)
        HeaderMenu.isSignInValidation(driverParam)

    @staticmethod
    def fastSignUp(driverParam):
        print("FastSignUp")
        driverParam.find_element(By.XPATH, "//*[@id='header-user-menu']/div").click()
        driverParam.find_element(By.LINK_TEXT, "Sign Out").click()


    @staticmethod
    def tearDown(driverParam):
        if driverParam.find_element(By.XPATH, "//*[@id='header-user-menu']/div"):
            Cart.closeCart(driverParam)
            driverParam.find_element(By.XPATH, "//*[@id='header-user-menu']/div").click()
            driverParam.find_element(By.LINK_TEXT, "Sign Out").click()
            #TODO
            #fastSignUp(driverParam)
            driverParam.close()
        elif driverParam.find_element(By.XPATH, "//*[@id='user-menu-mobile']"):
            print("Any Message")
            driverParam.close()


    @staticmethod
    def setLALocation(driverParam):
        #driverParam.find_element(By.NAME, "filter[address]").clear().send_keys("455 n louise St, Glandle, CA" + Keys.ENTER)
        driverParam.implicitly_wait(20)
        locationField = driverParam.find_element(By.NAME, "filter[address]")
        locationField.clear()
        locationField.send_keys("455 N Louise St, Glendale, CA")
        time.sleep(7)
        driverParam.find_element(By.XPATH, "//span[contains(text(),'455 N Louise St, Glendale, CA 91206, USA')]").click()
        driverParam.implicitly_wait(10)





