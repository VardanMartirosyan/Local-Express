import string
import time

from selenium.webdriver.common.by import By

class AddProduct():
    def __init__(self, driver):
        self.driverParam = driver

    def addAnyProduct(self, locator):
        cardProductsCount = self.getCartValue()
        self.driverParam.find_element(By.XPATH, locator).click()
        time.sleep(2)
        cardProductsCountAfterAdd = self.getCartValue()
        if int(cardProductsCount) + 1 != int(cardProductsCountAfterAdd):
            print("Can not add product to cart.")
            exit(2)

    def getCartValue(self) -> int:
        return self.driverParam.find_element(By.XPATH, "(//span[@class='product-cart-qty'])[1]").text

