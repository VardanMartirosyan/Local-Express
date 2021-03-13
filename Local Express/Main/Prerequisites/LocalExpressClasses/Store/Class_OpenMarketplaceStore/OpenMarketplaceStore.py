import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Automation import FunctionalityLib


class OpenMarketplaceStore():
    def __init__(self, driver):
        self.driverParam = driver

    def openStoreFromSearch(self, storeName):
        self.clearSearchField()
        self.fillInSearchField(storeName)
        self.selectFirstStoreFromResult()

    def clearSearchField(self):
        self.driverParam.find_element(By.NAME, "search-store").clear()

    def fillInSearchField(self, storeName):
        self.driverParam.find_element(By.XPATH, "//*[@name='search-store']")
        self.driverParam.find_element(By.NAME, "search-store").click()
        self.driverParam.find_element(By.NAME, "search-store").send_keys(storeName)
        time.sleep(2)

    def selectFirstStoreFromResult(self):
        self.driverParam.find_element(By.NAME, "search-store").send_keys(Keys.DOWN, Keys.ENTER)

#        WebDriverWait(driver, 5).until_not(EC.visibility_of_element_located((By.CLASS_NAME, "first-title")))
    #        #searchField.send_keys(Keys.TAB, Keys.ENTER)
    #        driver.find_element(By.XPATH, "//div[@class='box-content']/div[1]").click()





