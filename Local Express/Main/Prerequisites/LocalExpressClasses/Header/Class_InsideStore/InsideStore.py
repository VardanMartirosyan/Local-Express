from selenium.webdriver.common.by import By
from Main.Prerequisites.LocalExpressClasses.Header.Class_InsideStore import InsideStoreValidation


class InsideStore():
    def __init__(self, driver):
        self.driverParam = driver
        self.insideStoreValidation = InsideStoreValidation(self.driver)

    def openDepartment(self, storeName='default'):
        if storeName == 'default':
            self.driverParam.find_element(By.XPATH, "//*[@class='category-products-wrapper']")
        else:
            try:
                departmentNameXpath = "//*[@class='category-products-wrapper']//span[text()='" + storeName + "']"
                self.driverParam.find_element(By.XPATH, departmentNameXpath)
            except:
                print("Department not found")
                exit(1)

    def addProductFromSlider(self):
        self.insideStoreValidation.sliderShouldVisible()
        #Add product from Slider
        self.driverParam.find_element(By.XPATH, "//div[@class='roduct-card-add-line visible-lg-block '//div[@style='isplay: none;'")


