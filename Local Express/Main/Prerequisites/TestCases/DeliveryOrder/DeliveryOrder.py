import HtmlTestRunner
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Main.Prerequisites.LocalExpressClasses.Class_Global.AddProduct import *
from Main.Prerequisites.LocalExpressClasses.Class_Global.Class_GlobalLocalExpress import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_NavigationBar.Cart import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_StoresSection.Page_MarketplaceStores import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_StoresSection.PopUp_SignInMarketPlace import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_NavigationBar.UserMenuMobile import *
import time
from Main.Prerequisites.LocalExpressClasses.Store.Class_OpenMarketplaceStore.OpenMarketplaceStore import *


class TCStart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = GlobalLocalExpress.openGCAndCustomizeiBrowserSettings()

    @classmethod
    def tearDownClass(cls):
        GlobalLocalExpress.tearDown(cls.driver)
        print("Message")

class TestCases(TCStart):

    def test_DeliveryOrder(self):
        Page_MarketplaceStores.openLocalExpressStoresSection(self.driver)
        GlobalLocalExpress.setLALocation(self.driver)
        GlobalLocalExpress.fastSignIn(self.driver, Env.WebTestingLogIn, Env.WebTestingPassword)
        OpenMarketplaceStore.openStoreFromSearch(self.driver, "Local Express WebTesting")
        Cart.openCart(self.driver)
        Cart.removeCartAllContent(self.driver)
        AddProduct.addProduct(self.driver, "//div[@class='product-card-cart-wrapper']//span[@role='button-text']")
        AddProduct.addProduct(self.driver, "//div[@class='product-card-cart-wrapper']//span[@role='button-text']")
        Cart.closeCart(self.driver)
        print("Any Message")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())


