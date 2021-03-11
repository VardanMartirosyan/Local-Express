from selenium.webdriver.common.by import By
from Automation.FunctionalityLib import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_NavigationBar.Cart import *


class CartValidation():

    @staticmethod
    def cartButtonShouldBeExist(driverParam):
        driverParam.find_element(By.XPATH, "(//a[@class='cart-btn'])[1]")
        ElementShouldNotBeVisible(driverParam,"(//a[@class='cart-btn active'])[1]")

    @staticmethod
    def cartShouldBeOpened(driverParam):
        driverParam.find_element(By.XPATH, "(//a[@class='cart-btn active'])[1]")
        driverParam.find_element(By.XPATH, "//span[text()='Your Cart']")

    @staticmethod
    def cartShouldBeClosed(driverParam):
        driverParam.find_element(By.XPATH, "(//a[@class='cart-btn'])[1])")

    @staticmethod
    def cartShouldNotBeEmpty(driverParam):
        if int(Cart.getCartValue(driverParam)) >= 1:
            pass
        else:
            print("Cart is empty")
            exit(4)

    @staticmethod
    def cartShouldBeEmpty(driverParam):
        driverParam.find_element(By.XPATH, "//*[text()='Your cart is empty']")
        if int(Cart.getCartValue(driverParam)) == 0:
            pass
        else:
            print("Cart is not empty")
            exit(5)
