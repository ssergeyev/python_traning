# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    


    def add_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("middlename").send_keys(u"Николаевич")
        wd.find_element_by_name("lastname").send_keys(u"Любимов")
        wd.find_element_by_name("firstname").send_keys(u"Сергей")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("3")
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("October")
        wd.find_element_by_name("byear").send_keys("1969")
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text("family")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home page").click()
        wd.find_element_by_link_text("Logout").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def test_untitled_test_case(self):
        wd = self.wd
        wd.get("http://192.168.1.63/addressbook/index.php")
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd)


    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
