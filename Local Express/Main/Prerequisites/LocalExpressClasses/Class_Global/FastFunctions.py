from selenium import webdriver
from selenium.webdriver.common.by import By

class FastFunctions:
    def __init__(self, driver):
        self.driverParam = driver

    def fastSignUp(self):
        self.driverParam.find_element(By.XPATH, "//*[@id='header-user-menu']/div").click()
        self.driverParam.find_element(By.LINK_TEXT, "Sign Out").click()

