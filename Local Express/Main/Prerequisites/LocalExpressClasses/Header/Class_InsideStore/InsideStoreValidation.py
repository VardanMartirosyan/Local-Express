from selenium.webdriver.common.by import By

class InsideStoreValidation():
    def __init__(self, driver):
        self.driverParam = driver

    def sliderShouldBeVisible(self):
        self.driverParam.find_element(By.XPATH, "//*[@class='flex-wrapper product-cards-wrapper products-cards-slider slick-initialized slick-slider']")
