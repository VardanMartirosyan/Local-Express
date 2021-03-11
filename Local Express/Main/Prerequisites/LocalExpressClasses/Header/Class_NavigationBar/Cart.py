from selenium.webdriver.common.by import By
import time

from Automation.FunctionalityLib import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_NavigationBar.CartValidation import *


class Cart():
    @staticmethod
    def openCart(driverParam):
        if isElementPresent(driverParam, "(//a[@class='cart-btn active'])[1]"):
            return
        CartValidation.cartButtonShouldBeExist(driverParam)
        driverParam.find_element(By.XPATH, "(//a[@class='cart-btn'])[1]").click()
        CartValidation.cartShouldBeOpened(driverParam)

    @staticmethod
    def closeCart(driverParam):
        if isElementPresent(driverParam, "(//a[@class='cart-btn'])[1]"):
            return
        CartValidation.cartShouldBeOpened(driverParam)
        driverParam.find_element(By.XPATH, "//*[@title='products-cart']//a[@role='cart-close']").click()
        CartValidation.cartShouldBeClosed(driverParam)

    @staticmethod
    def removeCartAllContent(driverparam):
        cardProductsCount = Cart.getCartValue(driverparam)
        if cardProductsCount == 0:
            return
        Cart.openCart(driverparam)
        for x in range(cardProductsCount):
            Cart.removeFirstItemFromCart(driverparam)
        Cart.cartShouldBeEmpty(driverparam)

    @staticmethod
    def removeFirstItemFromCart(driverParam):
        CartValidation.cartShouldBeOpened(driverParam)
        cardProductsCount = Cart.getCartValue(driverParam)
        driverParam.find_element(By.XPATH, "//*[@role='cart-remove-all-product']").click()
        time.sleep(2)
        cardProductsCountAfterAdd = Cart.getCartValue(driverParam)
        if int(cardProductsCount) - 1 != int(cardProductsCountAfterAdd):
            print("Can not Delete product from Cart.")
            exit(3)


    @staticmethod
    def getCartValue(driverParam) -> int:
        return int(driverParam.find_element(By.XPATH, "(//span[@class='product-cart-qty'])[1]").text)


