import time

import time
import unittest
import selenium
from selenium import webdriver





class TestParallel(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Remote(command_executor = "http://localhost:4444/wd/hub",
                                       desired_capabilities =  {
                                           "browserName": "chrome", })
        self.driver.implicitly_wait(30)


    def test_four(self):

        driver = self.driver
        driver.get("https://www.google.org")
        time.sleep(3)


    def test_five(self):

        driver = self.driver
        driver.get("https://www.facebook.com")
        time.sleep(3)




    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":

    unittest.main()
