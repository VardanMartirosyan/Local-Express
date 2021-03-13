from selenium.webdriver.common.by import By
from Automation.FunctionalityLib import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_NavigationBar.Cart import *


class CartValidation():
    def __init__(self, driver):
        self.driverParam = driver

    def cartButtonShouldBeExist(self):
        self.driverParam.find_element(By.XPATH, "(//a[@class='cart-btn'])[1]")
        ElementShouldNotBeVisible(self.driverParam, "(//a[@class='cart-btn active'])[1]")

    def cartShouldBeOpened(self):
        self.driverParam.find_element(By.XPATH, "(//a[@class='cart-btn active'])[1]")
        self.driverParam.find_element(By.XPATH, "//span[text()='Your Cart']")

    def cartShouldBeClosed(self):
        self.driverParam.find_element(By.XPATH, "(//a[@class='cart-btn'][1])")

    def cartShouldNotBeEmpty(self):
        if int(self.getCartValue()) >= 1:
            pass
        else:
            print("Cart is empty")
            exit(4)

    def cartShouldBeEmpty(self):
        self.driverParam.find_element(By.XPATH, "//*[text()='Your cart is empty']")
        if int(self.getCartValue()) == 0:
            pass
        else:
            print("Cart is not empty")
            exit(5)

    def getCartValue(self) -> int:
        return int(self.driverParam.find_element(By.XPATH, "(//span[@class='product-cart-qty'])[1]").text)
