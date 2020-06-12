# -*- coding: utf-8 -*-
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
from random import randint, random

# import pytest

# ильтрация оп названи, еалорийносии, весу и поиск

class Admin_filters_deliveres(unittest.TestCase):

# фильтрация   раздела  Досатвки


    def authorization(self, driver): # авторизация

        driver.get("https://devadmin.bonration.ru/external/login")


        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-0']" )))#
            email_field.send_keys("8fzxx1cby0gy@mail.ru")
        except:
            time.sleep(5)
            email_field.send_keys("8fzxx1cby0gy@mail.ru")


        try:
            password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-1']" )))
            password_field.send_keys("password3")
        except:
            time.sleep(5)
            password_field.send_keys("password3")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                     "/html/body/app-root/portal-login/div/mat-card/mat-card-content[2]/div/div/div/app-spinner-button/button")))

        try:
            if button_voity.is_displayed():  # если кнпока видна , то
                    button_voity.click()

        except:
            time.sleep(5)
            button_voity.click()



    def filter(self,driver):

        time.sleep(3)
        #К доставке
        WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='mat-tab-label mat-ripple ng-star-inserted']")))[1].click()

        time.sleep(2)
        # Выполненные
        WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='mat-tab-label mat-ripple ng-star-inserted']")))[2].click()

        time.sleep(2)
        # Отмененные
        WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='mat-tab-label mat-ripple ng-star-inserted']")))[3].click()


    def ordering_by_parametrs(self,driver):# упорядлочивает по нмоеру закзак, дате и т.д.

            time.sleep(3)
            # по номеру заказа
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Change sorting for id']"))).click()

            time.sleep(3)
            # по времени заказа
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Change sorting for time']"))).click()

            time.sleep(3)
            # по ФИО клиента
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Change sorting for client']"))).click()

            time.sleep(3)
            # по телеофну клиента
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Change sorting for phone']"))).click()

            time.sleep(3)
            # по адресу клиента
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Change sorting for address']"))).click()

            time.sleep(3)
            # по  названию рациона
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Change sorting for ration']"))).click()

            time.sleep(2)
            # по  типу оплаты
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Change sorting for payment']"))).click()

            time.sleep(2)
            # по  статусу оплаты
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Change sorting for status']"))).click()

            time.sleep(2)
            # по  статусу доставки
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Change sorting for delivery_status']"))).click()


    def setUp(self):

        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={
            "browserName": "chrome",
        })


        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна

        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_filter_deliveres(self):  # главный метод, надо чтобы он начинался  с test_

        try:
            driver = self.driver
            self.authorization(driver)  # вызов метода,котрый выше
            time.sleep(4)  # чтобы сразу окно не закрывалось

            # раздел Все доставки:
            WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,
                                                                                     "//a[@href='/main/deliveries']"))).click()


            time.sleep(5)

            # кликаем на каледндарь
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//button[@class='date-picker-btn mat-icon-button']"))).click()# кликаем на каледндарь
            time.sleep(2)

            for i in range(0,3): #кнопка следущего месяца >
                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Next month']"))).click()


            # кнопка преддыущего месяца <
            for i in range(6):

                WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//button[@aria-label='Previous month']"))).click()
                time.sleep(2)
                print(i, "th iteration")

            dates = WebDriverWait(driver, 10).until( # получаем список дат
                        ec.presence_of_all_elements_located((By.XPATH, "//div[@class='mat-calendar-body-cell-content']")))
            time.sleep(2)

            #print("len()dates equal", len(dates))


            index_dates = [] # здесь будем хранитьраномные индексы дат календаря
            for j in range(0,20):# index_dates будет состоять из 20 дат

                ind = randint(0, 27)
                index_dates.append(ind)

            for k in range(0, 3): # пробегаемся в цикле по датам k раз, возьмет  три рандомные даты


                 i = randint(0, len(index_dates))
                 #print("to ckick date with random index", index_dates[i])

                 dates[index_dates[i]].click() # кдикаем дату  с раномным инекос
                 driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)  # переходим вниз станицы
                 time.sleep(2)
                 driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)  # скроллит станицу наверх переходим вверх станицы

                 WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='date-picker-btn mat-icon-button']"))).click()  # кликаем на  зеленую иконку каледндаря

                 time.sleep(2)




            self.ordering_by_parametrs(driver)# вызов меода упорядочивания

            time.sleep(2)
            self.filter(driver)# вызов меода фильтрации

            time.sleep(3)

            # переключатель даты вперед и назад
            for i in range(randint(0,5)):
                time.sleep(2)
                WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
                    (By.XPATH, "//button[@class='day-switcher-btn mat-icon-button']")))[0].click()

            time.sleep(3)

            for i in range(randint(0, 5)):
                time.sleep(2)
                WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
                    (By.XPATH, "//button[@class='day-switcher-btn mat-icon-button']")))[1].click()

            time.sleep(3)

        except:
            print("my error")



    def tear_down(self):
        time.sleep(5)# чтобы окно сразу не закрывалось
        self.driver.close()



if __name__ == "__main__":
    unittest.main()



