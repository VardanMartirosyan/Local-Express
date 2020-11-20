from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Automation.FunctionalityLib import *
from Main.Prerequisites.Classes.Class_Global.Class_GlobalLocalExpress import *
from Main.Prerequisites.Classes.Class_SignIn.Class_SignInMarketplace import *
import time

class TCLogInMarketplace:
    def TestSetup(self):
        GlobalLocalExpress.openGCAndCustomizeiBrowserSettings()

    def TestTearDown(self):
        GlobalLocalExpress.tearDown()

if __name__ == '__main__':
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(9)
    driver.get("https://local.express/stores")
    assert "Find a store" in driver.title

    ElementShouldNotBeVisible(driver, "//*[@class='open']")

    userMenuIcon = driver.find_element(By.XPATH, "//*[@id='user-menu-mobile']/i")
    userMenuIcon.click()

    ElementShouldBeVisible(driver, "//*[@class='open']")

    SignIn = driver.find_element(By.XPATH, "//a[contains(text(),'Sign In')]")
    SignIn.click()

    ElementShouldBeVisible(driver, "//input[@name='credentials[email]']")
    driver.find_element(By.XPATH, "//input[@name='credentials[email]']").send_keys("vardanm@local.express")
    driver.find_element(By.XPATH, "//input[@name='credentials[password]']").send_keys("Q11111111")
    driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()

    WebDriverWait(driver, 5).until_not(EC.visibility_of_element_located((By.CLASS_NAME, "first-title")))
    searchField = driver.find_element_by_name("search-store")
    searchField.clear()
    searchField.click()
    searchField.send_keys("Vardan's Store")
    time.sleep(2)
    #searchField.send_keys(Keys.TAB, Keys.ENTER)
    driver.find_element(By.XPATH, "//div[@class='box-content']/div[1]").click()

    driver.close()
