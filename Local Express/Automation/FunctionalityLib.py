def ElementShouldNotBeVisible(driver, xpath):
    try:
        validation = driver.find_element_by_xpath(xpath)
    except:
        validationResult = "ElementNotFound"
    else:
        raise Exception("Element Is Visible")

def ElementShouldBeVisible(driver, xpath):
    try:
        validation = driver.find_element_by_xpath(xpath)
    except:
        raise Exception("Element Is Not Visible")
