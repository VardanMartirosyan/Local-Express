import unittest
import Automation.MyLogger as myLogger

from Automation.MyListener import MyListener
from Main.Prerequisites.LocalExpressClasses.Class_Global.SetUpConfiguration import *
from Main.Prerequisites.LocalExpressClasses.Class_Global.Class_GlobalLocalExpress import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_StoresSection.Page_MarketplaceStores import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_StoresSection.PopUp_SignInMarketPlace import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_NavigationBar.UserMenuMobile import *
from selenium.webdriver.support.events import EventFiringWebDriver
from TestData.ENVs import Env

class TCStart(unittest.TestCase):
    globalLocalExpress = None

    @classmethod
    def setUpClass(cls):
        cls.driver = SetUpConfiguration.openGCAndCustomizeiBrowserSettings()
        cls.edriver = EventFiringWebDriver(cls.driver, MyListener())
        cls.globalLocalExpress = GlobalLocalExpress(cls.edriver)
        cls.page_MarketplaceStores = Page_MarketplaceStores(cls.edriver)
        cls.userMenuMobile = UserMenuMobile(cls.edriver)
        cls.popUp_SignInMarketplace = PopUp_SignInMarketplace(cls.edriver)
        cls.headerMenu = HeaderMenu(cls.edriver)

    @classmethod
    def tearDownClass(cls):
        cls.globalLocalExpress.tearDown()


class LogInMarketplace(TCStart):

    def test_LogInMarketplace(self):
        self.page_MarketplaceStores.openLocalExpressStoresSection()

        self.userMenuMobile.openUserMenuMobileDropdown()
        self.userMenuMobile.clickSignInDropdownMenuButton()

        self.popUp_SignInMarketplace.signInPopUpValidation()
        self.popUp_SignInMarketplace.signInDDT()
        myLogger.logger("INFO", str(self.__class__.__name__) + Env.passTestCaseLoggerMessage, Env.logFilePath)



