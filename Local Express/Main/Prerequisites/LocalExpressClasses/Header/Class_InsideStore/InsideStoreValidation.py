from selenium.webdriver.common.by import By

class InsideStoreValidation():

    @staticmethod
    def SliderShouldBeVisible(driverParam):
        driverParam.find_element(By.XPATH, "//*[@class='flex-wrapper product-cards-wrapper products-cards-slider slick-initialized slick-slider']")
