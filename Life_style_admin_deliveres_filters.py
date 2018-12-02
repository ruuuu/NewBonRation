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

# ильтрация оп названи, еалорийносии, весу и поиск

class Admin_filters_deliveres(unittest.TestCase):

# фильтрация   раздела  Досатвки


    def authorization(self, driver): # авторизация

        driver.get("https://devadmin.bonration.ru/external/login")


        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-0']" )))#
            email_field.send_keys("wyvzmp5iy5oh@mail.ru")
        except TimeoutError:
            print("время ожидания поля емэйл вышло")

        try:
            password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-1']" )))
            password_field.send_keys("qwerty")
        except TimeoutError:
            print("время ожидания поля пароль вышло")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                       "/html/body/app-root/portal-login/div/mat-card/mat-card-content[2]/div/div/div/app-spinner-button/button")))
        if button_voity.is_displayed():  # если кнпока видна , то
            button_voity.click()
        time.sleep(3)


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

        self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_filter_deliveres(self):  # главный метод, надо чтобы он начинался  с test_

        try:
            driver = self.driver
            self.authorization(driver)  # вызов метода,котрый выше
            time.sleep(4)  # чтобы сразу окно не закрывалось

            # раздел Все доставки:
            WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,
                                                                                     "//a[@href='/main/deliveries']"))).click()

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

            time.sleep(2)

            # кликаем на каледндарь
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//button[@class='date-picker-btn mat-icon-button']"))).click()# кликаем на каледндарь
            time.sleep(4)

            # # выбираем дату в каледнаре
            # date= WebDriverWait(driver, 10).until(
            #     ec.presence_of_element_located((By.XPATH, "//td[@aria-label='19 ноября 2018 г.']")))
            #
            # date.click()
            # time.sleep(2)

            self.ordering_by_parametrs(driver)# вызов меода упорядочивания


            self.filter(driver)# вызов меода фильтрации

            time.sleep(3)

            # ереключатель даты вперед и назад
            WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
                (By.XPATH, "//button[@class='day-switcher-btn mat-icon-button']")))[0].click()

            time.sleep(3)
            WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
                (By.XPATH, "//button[@class='day-switcher-btn mat-icon-button']")))[1].click()

            time.sleep(3)

        except:
            print(" где-то у меня ошибка")



    def tear_down(self):
        time.sleep(5)# чтобы окно сразу не закрывалось
        self.driver.close()



if __name__ == "__main__":
    unittest.main()



