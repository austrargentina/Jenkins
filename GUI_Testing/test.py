__author__ = 'arif'

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    
    '''
    Initialize the test environment
    '''
    #Create an instance of Firefox WebDriver
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    '''
    Check the IP-adress input with not allowed inputs like text
    '''
    def test_search_in_python_org(self):
        browser = self.browser
        #calls the following URL
        browser.get("http://127.0.0.1:5000/login")
        elem = browser.find_element_by_name("ip")
        assert "No results found." not in browser.page_source
        elem.send_keys(Keys.RETURN)
        #types the following IP address
        elem.send_keys("10.0.100.10")

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()