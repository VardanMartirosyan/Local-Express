from Automation.FunctionalityLib import *
from selenium.webdriver.common.by import By


class Page_MarketplaceStores:
    def __init__(self, driver):
        self.driverParam = driver

    def openLocalExpressStoresSection(self):
        self.driverParam.get("https://local.express/stores")
        self.LocalExpressMarketplaceStoreValidation()

    def LocalExpressMarketplaceStoreValidation(self):
        self.validationByPageTitle()
        self.driverParam.find_element(By.NAME, "search-store")

    def validationByPageTitle(self):
        assert "Find a store" in self.driverParam.title
