import time

import time
import unittest
import selenium
from selenium import webdriver





class TestTwo(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Remote(command_executor = "http://localhost:4444/wd/hub",
                                       desired_capabilities =  {
                                           "browserName": "chrome", })
        self.driver.implicitly_wait(30)


    def  test_two(self):

        driver = self.driver
        driver.get("https://www.youtube.com")
        time.sleep(3)



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":

    unittest.main()
