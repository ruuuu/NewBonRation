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


class Admin_filters_rations(unittest.TestCase):

# фильтрация   раздела Управление рациоанми по возрастанию и  убыванию и поиск


    def authorization(self, driver): # авторизация

        driver.get("https://devadmin.bonration.ru/external/login")


        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-0']" )))#
            email_field.send_keys("wyvzmp5iy5oh@mail.ru")
        except :
            print("email_field is not founded")

        try:
            password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-1']" )))
            password_field.send_keys("qwerty")
        except :
            print("password_field is not founded")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                       "/html/body/app-root/portal-login/div/mat-card/mat-card-content[2]/div/div/div/app-spinner-button/button")))
        if button_voity.is_displayed():  # если кнпока видна , то
            button_voity.click()
        time.sleep(3)

    def search_rations(self,driver):

         # Поиск по названию, калонрийности цене
         search_rations = WebDriverWait(driver, 10).until(
             ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Поиск']")))
         search_rations.send_keys("string")
         time.sleep(2)
         search_rations.clear()

         time.sleep(2)
         search_rations.send_keys("789")
         time.sleep(2)
         search_rations.clear()

         time.sleep(2)
         search_rations.send_keys("1200")
         time.sleep(2)
         search_rations.clear()


    def setUp(self):

        self.driver = webdriver.Firefox()  #.Chrome()
        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна

        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_filter_rations(self):  # главный метод, надо чтобы он начинался  с test_
        try:
            driver = self.driver
            self.authorization(driver)  # вызов метода,котрый выше
            #time.sleep(4)  # чтобы сразу окно не закрывалось

            # раздел Рацилоны:
            WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,
                                                                                     "//a[@href='/main/rations']"))).click()

            # # Новые
            # new = driver.find_elements_by_xpath("//div[@class='mat-tab-label mat-ripple ng-star-inserted']")[0]
            # time.sleep(10)
            # if new.is_displayed():
            #
            #     new.click()
            # else:
            #     time.sleep(7)
            #     new.click()
            # time.sleep(3)

            # Название по возрастанию
            time.sleep(5)
            name_taions = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Change sorting for name']")))
            time.sleep(1)
            name_taions.click()

            # Калорийность по возрастанию
            time.sleep(2)
            calor_rations = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Change sorting for calories']")))
            time.sleep(1)
            calor_rations.click()

            # Цена по возрастанию
            time.sleep(2)
            price_rations = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Change sorting for price']")))
            time.sleep(1)
            price_rations.click()

        except:
            print("error")
        time.sleep(4)

        self.search_rations(driver) # вызов метода поиска



    def tear_down(self):
        time.sleep(5)# чтобы окно сразу не закрывалось
        self.driver.close()



if __name__ == "__main__":
    unittest.main()



