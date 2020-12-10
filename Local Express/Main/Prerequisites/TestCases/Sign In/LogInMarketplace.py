import HtmlTestRunner
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Main.Prerequisites.LocalExpressClasses.Main.Class_Global.Class_GlobalLocalExpress import *
from Main.Prerequisites.LocalExpressClasses.Main.Class_StoresSection.Page_MarketplaceStores import *
from Main.Prerequisites.LocalExpressClasses.Main.Class_StoresSection.PopUp_LogInMarketPlace import *
from Main.Prerequisites.LocalExpressClasses.Main.Class_UserMenuMobile.UserMenuMobile import *
import time

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = None


class TCStart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global driver
        driver = GlobalLocalExpress.openGCAndCustomizeiBrowserSettings(driver)

    @classmethod
    def tearDownClass(cls):
        GlobalLocalExpress.tearDown(driver)


class TestCases(TCStart):

    def test_LogInMarketplace(self):
        Page_MarketplaceStores.openLocalExpressStores(driver)

        UserMenuMobile.openUserMenuMobileDropdown(driver)
        UserMenuMobile.clickSignInDropdownMenuButton(driver)

        PopUp_LogInMarketplace.SignInPopUpValidation(driver)
        PopUp_LogInMarketplace.fillDataAndPressSignIn(driver)

        WebDriverWait(driver, 5).until_not(EC.visibility_of_element_located((By.CLASS_NAME, "first-title")))
        searchField = driver.find_element_by_name("search-store")
        searchField.clear()
        searchField.click()
        searchField.send_keys("Vardan's Store")
        time.sleep(2)
        #searchField.send_keys(Keys.TAB, Keys.ENTER)
        driver.find_element(By.XPATH, "//div[@class='box-content']/div[1]").click()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())


