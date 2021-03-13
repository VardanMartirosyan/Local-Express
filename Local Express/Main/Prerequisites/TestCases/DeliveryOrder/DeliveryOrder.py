import HtmlTestRunner
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Main.Prerequisites.LocalExpressClasses.Class_Global.SetUpConfiguration import *
from Main.Prerequisites.LocalExpressClasses.Class_Global.AddProduct import *
from Main.Prerequisites.LocalExpressClasses.Class_Global.Class_GlobalLocalExpress import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_NavigationBar.Cart import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_StoresSection.Page_MarketplaceStores import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_StoresSection.PopUp_SignInMarketPlace import *
from Main.Prerequisites.LocalExpressClasses.Header.Class_NavigationBar.UserMenuMobile import *
import time
from Main.Prerequisites.LocalExpressClasses.Store.Class_OpenMarketplaceStore.OpenMarketplaceStore import *


class TCStart(unittest.TestCase):
    globalLocalExpress = None
    
    @classmethod
    def setUpClass(cls):
        cls.driver = SetUpConfiguration.openGCAndCustomizeiBrowserSettings()
        cls.addProduct = AddProduct(cls.driver)
        cls.page_MarketplaceStores = Page_MarketplaceStores(cls.driver)
        cls.globalLocalExpress = GlobalLocalExpress(cls.driver)
        cls.openMarketplaceStore = OpenMarketplaceStore(cls.driver)
        cls.cart = Cart(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.globalLocalExpress.tearDown(cls.driver)
        print("Message")

class TestCases(TCStart):

    def test_DeliveryOrder(self):
        self.page_MarketplaceStores.openLocalExpressStoresSection()
        self.globalLocalExpress.setLALocation()
        self.globalLocalExpress.fastSignIn(Env.WebTestingLogIn, Env.WebTestingPassword)
        self.openMarketplaceStore.openStoreFromSearch("Local Express WebTesting")
        self.cart.openCart()
        self.cart.removeCartAllContent()
        self.addProduct.addAnyProduct("//div[@class='product-card-cart-wrapper']//span[@role='button-text']")
        self.cart.closeCart()
        print("Any Message")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())


