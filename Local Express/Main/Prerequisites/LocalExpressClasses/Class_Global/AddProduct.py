import string
import time

from selenium.webdriver.common.by import By

class AddProduct():
    #def __init__(self, driver):
    #    driverParam = driver

    @staticmethod
    def addProduct(driverParam, locator):
        cardProductsCount = AddProduct.getCartValue(driverParam)
        driverParam.find_element(By.XPATH, locator).click()
        time.sleep(2)
        cardProductsCountAfterAdd = AddProduct.getCartValue(driverParam)
        if int(cardProductsCount) + 1 != int(cardProductsCountAfterAdd):
            print("Can not add product to cart.")
            exit(2)

    @staticmethod
    def getCartValue(driverParam) -> int:
        return driverParam.find_element(By.XPATH, "(//span[@class='product-cart-qty'])[1]").text

