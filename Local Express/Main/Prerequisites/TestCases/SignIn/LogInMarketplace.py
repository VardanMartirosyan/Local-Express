import HtmlTestRunner
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Main.Prerequisites.LocalExpressClasses.Class_Global.Class_GlobalLocalExpress import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_StoresSection.Page_MarketplaceStores import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_StoresSection.PopUp_SignInMarketPlace import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_NavigationBar.UserMenuMobile import *
import time

class TCStart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = GlobalLocalExpress.openGCAndCustomizeiBrowserSettings()

    @classmethod
    def tearDownClass(cls):
        GlobalLocalExpress.tearDown(cls.driver)
        print("Message")


class TestCases(TCStart):

    def test_LogInMarketplace(self):
        Page_MarketplaceStores.openLocalExpressStoresSection(self.driver)

        UserMenuMobile.openUserMenuMobileDropdown(self.driver)
        UserMenuMobile.clickSignInDropdownMenuButton(self.driver)

        PopUp_SignInMarketplace.SignInPopUpValidation(self.driver)
        PopUp_SignInMarketplace.fillDataAndPressSignIn(self.driver, Env.WebTestingLogIn, Env.WebTestingPassword)

#if __name__ == '__main__':
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())


