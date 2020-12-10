from Automation.FunctionalityLib import *
from selenium.webdriver.common.by import By


class Page_MarketplaceStores:
    @staticmethod
    def openLocalExpressStores(driverParam):
        driverParam.get("https://local.express/stores")
        Page_MarketplaceStores.LocalExpressMarketplaceStoreValidation(driverParam)

    @staticmethod
    def LocalExpressMarketplaceStoreValidation(driverParam):
        Page_MarketplaceStores.validationByPageTitle(driverParam)
        driverParam.find_element(By.NAME, "search-store")

    @staticmethod
    def validationByPageTitle(driverParam):
        assert "Find a store" in driverParam.title
