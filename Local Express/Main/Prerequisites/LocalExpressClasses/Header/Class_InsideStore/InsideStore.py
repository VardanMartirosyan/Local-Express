from selenium.webdriver.common.by import By
from Main.Prerequisites.LocalExpressClasses.Header.Class_InsideStore import InsideStoreValidation


class InsideStore():
    @staticmethod
    def openDepartment(driverParam, storeName='default'):
        if storeName == 'default':
            driverParam.find_element(By.XPATH, "//*[@class='category-products-wrapper']")
        else:
            try:
                departmentnamexpath = "//*[@class='category-products-wrapper']//span[text()='" + storeName + "']"
                driverParam.find_element(By.XPATH, departmentnamexpath)
            except:
                print("Department not found")
                exit(1)

    @staticmethod
    def AddProductFromSlider(driverParam):
        InsideStoreValidation.sliderShouldVisible(driverParam)
        #Add product from Slider
        driverParam.find_element(By.XPATH, "//div[@class='roduct-card-add-line visible-lg-block '//div[@style='isplay: none;'")
        #Add product from Slider
        driverParam.find_element(By.XPATH, "//div[@class='roduct-card-add-line visible-lg-block '//div[@style='isplay: none;'")
        #Add product from Slider
        driverParam.find_element(By.XPATH, "//div[@class='roduct-card-add-line visible-lg-block '//div[@style='isplay: none;'")


