import HtmlTestRunner
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Main.Prerequisites.LocalExpressClasses.Class_Global.SetUpConfiguration import *
from Main.Prerequisites.LocalExpressClasses.Class_Global.Class_GlobalLocalExpress import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_StoresSection.Page_MarketplaceStores import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_StoresSection.PopUp_SignInMarketPlace import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_NavigationBar.UserMenuMobile import *

class TCStart(unittest.TestCase):
    globalLocalExpress = None

    @classmethod
    def setUpClass(cls):
        cls.driver = SetUpConfiguration.openGCAndCustomizeiBrowserSettings()
        cls.globalLocalExpress = GlobalLocalExpress(cls.driver)
        cls.page_MarketplaceStores = Page_MarketplaceStores(cls.driver)
        cls.userMenuMobile = UserMenuMobile(cls.driver)
        cls.popUp_SignInMarketplace = PopUp_SignInMarketplace(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.globalLocalExpress.tearDown(cls.driver)
        print("Message")


class TestCases(TCStart):

    def test_LogInMarketplace(self):
        self.page_MarketplaceStores.openLocalExpressStoresSection()

        self.userMenuMobile.openUserMenuMobileDropdown()
        self.userMenuMobile.clickSignInDropdownMenuButton()

        self.popUp_SignInMarketplace.SignInPopUpValidation()
        self.popUp_SignInMarketplace.fillDataAndPressSignIn(Env.WebTestingLogIn, Env.WebTestingPassword)



