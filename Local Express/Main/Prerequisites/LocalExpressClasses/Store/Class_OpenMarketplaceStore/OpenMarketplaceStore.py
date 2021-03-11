import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Automation import FunctionalityLib


class OpenMarketplaceStore():
    @staticmethod
    def openStoreFromSearch(driverParam, storeName):
        OpenMarketplaceStore.clearSearchField(driverParam)
        OpenMarketplaceStore.fillInSearchField(driverParam, storeName)
        OpenMarketplaceStore.selectFirstStoreFromResult(driverParam)

    @staticmethod
    def clearSearchField(driverParam):
        driverParam.find_element(By.NAME, "search-store").clear()

    @staticmethod
    def fillInSearchField(driverParam, storeName):
        driverParam.find_element(By.XPATH, "//*[@name='search-store']")
        driverParam.find_element(By.NAME, "search-store").click()
        driverParam.find_element(By.NAME, "search-store").send_keys(storeName)
        time.sleep(2)

    @staticmethod
    def selectFirstStoreFromResult(driverParam):
        driverParam.find_element(By.NAME, "search-store").send_keys(Keys.DOWN, Keys.ENTER)

#        WebDriverWait(driver, 5).until_not(EC.visibility_of_element_located((By.CLASS_NAME, "first-title")))
    #        #searchField.send_keys(Keys.TAB, Keys.ENTER)
    #        driver.find_element(By.XPATH, "//div[@class='box-content']/div[1]").click()





