import time
import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # ожидания различных событий
from selenium.webdriver.support.ui import Select  # работа со списками
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains # для скролдинга к нужному элементу импортируем класс ActionChains

# import pytest


class Admin_filters_orders(unittest.TestCase):

# фильтрация   раздела Заказы на Новые, Текущие, Выполняюттся  Выполненные, Все


    def authorization(self, driver): # авторизация

        driver.get("https://devadmin.bonration.ru/external/login")


        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-0']" )))#
            email_field.send_keys("8fzxx1cby0gy@mail.ru")
        except:
            print("email_field is not founded")

        try:
            password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-1']" )))
            password_field.send_keys("password3")
        except :
            print("password_field is not founded")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                       "/html/body/app-root/portal-login/div/mat-card/mat-card-content[2]/div/div/div/app-spinner-button/button")))
        if button_voity.is_displayed():  # если кнпока видна , то
            button_voity.click()
        time.sleep(3)





    def setUp(self):

        self.driver = webdriver.Firefox() #Chrome()
        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна

        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_filter_orders(self):  # главный метод, надо чтобы он начинался  с test_
        try:
            driver = self.driver
            self.authorization(driver)  # вызов метода,котрый выше
            #time.sleep(4)  # чтобы сразу окно не закрывалось

            # раздел Заказы:
            WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,""
                                                                                     "//a[@href='/main/orders']"))).click()



            # в поле Поиск вводим номер заказк:
            time.sleep(5)
            search = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Поиск']")))
            time.sleep(2)
            search.send_keys("1138")
            search.clear() # чищвем поле

            time.sleep(2)
            search.send_keys("makar")
            time.sleep(2)
            search.clear()  # чищвем поле

            time.sleep(2)
            search.send_keys("Hfabjy")
            search.clear() #  очищае поле

            time.sleep(2)

            for i in range(1, 5):
              try:
                current = WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='mat-tab-label mat-ripple ng-star-inserted']")))[i]
                time.sleep(2)
                current.click()
                time.sleep(2)
              except:
                  print("somthing is wrong^ element is not cluckable or element not founded")

        except:
            print("error")


    def tear_down(self):
        time.sleep(5)# чтобы окно сразу не закрывалось
        self.driver.close()



if __name__ == "__main__":
    unittest.main()



