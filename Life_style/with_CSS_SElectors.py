from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
import unittest
import sys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# import xmlrunner
#
# desiredCapabilities = {
#     'browserName':'chrome',
#     'node': 'node',
#     'platform': 'plateform'
# }
#
# driver = webdriver.Remote(desired_capabilities = desiredCapabilities)
# driver.get("https://www.google.co.in/")
# print(driver.title)
# driver.quit()

# class ExampleTestCase(unittest.TestCase):
#
#     capabilities = None
#
#     def setUp(self):
#         self.driver = webdriver.Remote(desired_capabilities={
#         'browserName': broswer,
#         'platform': platform,
#         'node':node })
#
#     def test_example(self):
#         self.driver.get('www.360logica.com')
#         self.assertEqual(self.driver.title, '360logica')
#
#     def tearDown(self):
#         self.driver.quit()
#
# if __name__ == '__main__':
#     args = sys.argv
#     port = args[1]
#     platform = args[2]
#     broswer = args[3]
#     suite = unittest.TestSuite()
#     suite.addTest(ExampleTestCase('test_example'))
#     runner = XMLTestRunner(file('results_ExampleTestCase_%s.xml' % (broswer), 'w'))
#     runner.run(suite)

# class ExampleTestCase(unittest.TestCase):
#     capabilities = None  # поле
#
#     def setUp(self):
#
#         #self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',desired_capabilities = webdriver.DesiredCapabilities.FIREFOX)
#
#         self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={
#             "browserName": "firefox",
#         })
#
#         self.driver.maximize_window()
#
#
#     def test_example(self):  # здесь будет сам тест
#         self.driver.get("http://www.google.com")
#         time.sleep(4)
#         self.assertEqual(self.driver.title, "Google")
#
#     def tearDown(self):
#         time.sleep(4)
#         self.driver.quit()
#
#
# if __name__ == "__main__":
#     #
#     # ExampleTestCase.capabilities = {
#     #
#     #     "browserName": sys.argv[1],
#     #     #"port": sys.argv[2],
#     #     #"platform": sys.argv[2],
#     # }
#
#     unittest.main()

class ExampleTestCase(unittest.TestCase):

    def setUp(self):
#
         self.driver = webdriver.Chrome()
         self.driver.maximize_window()

    def test_method_with_selector(self):

        self.driver.get("https://devadmin.bonration.ru/external/login")

        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR,"#mat-input-0"))).send_keys("wyvzmp5iy5oh@mail.ru")

        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "#mat-input-1"))).send_keys("qwerty")

        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "body > app-root > portal-login > div > mat-card > mat-card-content:nth-child(2) > div > div > div > app-spinner-button > button"))).click()

        time.sleep(4)

    def tearDown(self):
#         time.sleep(4)
         self.driver.quit()


if __name__ == "__main__":
    unittest.main()