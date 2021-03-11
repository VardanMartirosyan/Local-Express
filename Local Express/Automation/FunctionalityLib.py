from selenium.webdriver.common.by import By

def ElementShouldNotBeVisible(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except:
        validationResult = "ElementNotFound"
    else:
        raise Exception("Element Is Visible")

def ElementShouldBeVisible(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except:
        raise Exception("Element Is Not Visible")


def isElementPresent(driverParam, locator) -> bool:
   try:
       driverParam.find_element(By.XPATH, locator)
       return True
   except:
       return False
