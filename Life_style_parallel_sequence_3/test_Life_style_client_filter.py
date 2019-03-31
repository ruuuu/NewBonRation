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
from random import randint
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, NoSuchAttributeException

# import pytest

# фильтация  у клиента

class Climet_Filters(unittest.TestCase):

# Раздел статистика


    def authorization(self, driver): # авторизация

        driver.get("https://devclient.bonration.ru/external/login")
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-border btn-border-black login-btn ripple']"))).click()

        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Email']" )))#
            email_field.send_keys("rufinka_91@mail.ru")
        except :
            print("email_field is not founded")

        try:
            password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Пароль']" )))
            password_field.send_keys("7071991")
        except :
            print("password_field is not founded")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                       "//button[@class='btn btn-fill btn-fill-full needsclick ripple']")))
        if button_voity.is_enabled():  # если кнпока кликабельна, то
            button_voity.click()
            time.sleep(3)
        else:
            print("authorization button is not clickable")





    def setUp(self):

        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={
            "browserName": "chrome",
        })
        #поле

        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна

        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_filter(self):  # главный метод, надо чтобы он начинался  с test_

        self.authorization(self.driver)
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@href='/search']"))).click() # кнпока Найти раицон

        time.sleep(2)

        for i in range(1, 7): # маленькие треугольнички

            WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH,"//button[@class='btn ls-drop-down-btn select-drop-down-btn']")))[i].click()
            time.sleep(2)
            list_items = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='select-item']")))# список айтемов из выпадающео псика

            rand_index_of_item = randint(0, len(list_items)-1) # выбираем рандомный item
            list_items[rand_index_of_item].click()

        list_chekboxes = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn checkbox checkbox-btn']"))) # спсиок чекбоксов

        # кликаме чекбоксы:
        for i in range(0, 5):
            list_chekboxes[i].click()
            time.sleep(2)

        for i in range(0, 2):
            rand_of_chekboxes_index = randint(0, len(list_chekboxes)-1)
            list_chekboxes[rand_of_chekboxes_index].click()
            time.sleep(2)


    def tear_down(self):
        time.sleep(5)# чтобы окно сразу не закрывалось
        #self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()



