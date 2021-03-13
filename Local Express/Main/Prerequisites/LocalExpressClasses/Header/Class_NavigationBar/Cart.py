from selenium.webdriver.common.by import By
import time

from Automation.FunctionalityLib import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_NavigationBar.CartValidation import *


class Cart():
    def __init__(self, driver):
        self.driverParam = driver
        self.cartValidation = CartValidation(self.driverParam)

    def openCart(self):
        if isElementPresent(self.driverParam, "(//a[@class='cart-btn active'])[1]"):
            return
        self.cartValidation.cartButtonShouldBeExist()
        self.driverParam.find_element(By.XPATH, "(//a[@class='cart-btn'])[1]").click()
        self.cartValidation.cartShouldBeOpened()

    def closeCart(self):
        if isElementPresent(self.driverParam, "(//a[@class='cart-btn'])[1]"):
            return
        self.cartValidation.cartShouldBeOpened()
        self.driverParam.find_element(By.XPATH, "//*[@title='products-cart']//a[@role='cart-close']").click()
        self.cartValidation.cartShouldBeClosed()

    def removeCartAllContent(self):
        cardProductsCount = self.cartValidation.getCartValue()
        if cardProductsCount == 0:
            return
        self.openCart()
        for x in range(cardProductsCount):
            self.removeFirstItemFromCart()
        self.cartValidation.cartShouldBeEmpty()

    def removeFirstItemFromCart(self):
        self.cartValidation.cartShouldBeOpened()
        cardProductsCount = self.cartValidation.getCartValue()
        self.driverParam.find_element(By.XPATH, "//*[@role='cart-remove-all-product']").click()
        time.sleep(2)
        cardProductsCountAfterAdd = self.cartValidation.getCartValue()
        if int(cardProductsCount) - 1 != int(cardProductsCountAfterAdd):
            print("Can not Delete product from Cart.")
            exit(3)



