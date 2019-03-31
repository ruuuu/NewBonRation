import time

import time
import unittest
import selenium
from selenium import webdriver





class TestThree(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Remote(command_executor = "http://localhost:4444/wd/hub",
                                       desired_capabilities =  {
                                           "browserName": "chrome", })
        self.driver.implicitly_wait(30)


    def  test_three(self):

        driver = self.driver
        driver.get("https://www.twitter.com")
        time.sleep(3)



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":

    unittest.main()
