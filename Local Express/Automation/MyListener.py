import unittest
from selenium.webdriver.support.events import AbstractEventListener


class MyListener(AbstractEventListener):
#    def before_navigate_to(self, url, driver):
#        print("Before navigating to ", url)

    def after_navigate_to(self, url, driver):
        print("<span style='display:block;'>", "After navigating to <a href='", url, "'>", url, "</a>", "</span>")

 #   def before_navigate_back(self, driver):
 #       print("before navigating back ", driver.current_url)

    def after_navigate_back(self, driver):
        print("<span style='display:block;'>", "After navigating back ","<span style='color:blue;'>",  driver.current_url, "</span>", "</span>")

 #   def before_navigate_forward(self, driver):
 #       print("before navigating forward ", driver.current_url)

    def after_navigate_forward(self, driver):
        print("<span style='display:block;'>", "After navigating forward ", "<span style='color:blue;'>", driver.current_url, "</span>", "</span>")

 #   def before_find(self, by, value, driver):
 #       print("before find", by, value)

    def after_find(self, by, value, driver):
        print("<span style='display:block;'>", "after_find", "<span style='color:Navy;'>", by, "</span> <span style='color:blue;'>", value, "</span> </span>")

 #   def before_click(self, element, driver):
 #       print("before_click")

    def after_click(self, element, driver):
        print("<span style='display:block;'>", "after_click", "<span style='color:blue;'>", element, "</span>", "</span>")

 #   def before_change_value_of(self, element, driver):
 #       print("before_change_value_of")

    def after_change_value_of(self, element, driver):
        print("<span style='display:block;'>", "after_change_value_of", "<span style='color:blue;'>", element, "</span>", "</span>")

 #   def before_execute_script(self, script, driver):
 #       print("before_execute_script")

    def after_execute_script(self, script, driver):
        print("<span style='display:block;'>", "after_execute_script", "<span style='color:blue;'>", script, "</span>", "</span>")

 #   def before_close(self, driver):
 #       print("before_close")

    def after_close(self, driver):
        print("<span style='display:block;'>", "after_close", "</span>")

 #   def before_quit(self, driver):
 #       print("before_quit")

    def after_quit(self, driver):
        print("<span style='display:block;'>", "after_quit", "</span>")

    def on_exception(self, exception, driver):
        print("<span style='display:block;'>", "on_exception", "</span>")


