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
from selenium.webdriver.common.action_chains import ActionChains # lля сколддинга к нужному элементу импортируем класс ActionChains

import pytest
 # здесь  авторизация админа(компаний)

class Admin_authorization(unittest.TestCase):


    def authorization(self, driver): # авторизация

        driver.get("https://devadmin.bonration.ru/external/login")


        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-0']" )))#
            email_field.send_keys("wyvzmp5iy5oh@mail.ru")
        except :
            time.sleep(5)
            email_field.send_keys("wyvzmp5iy5oh@mail.ru")

        try:
            password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-1']" )))
            password_field.send_keys("qwerty")
        except:
            time.sleep(5)
            password_field.send_keys("qwerty")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                       "/html/body/app-root/portal-login/div/mat-card/mat-card-content[2]/div/div/div/app-spinner-button/button")))
        if button_voity.is_displayed():  # если кнпока видна , то
            button_voity.click()
            print("button is visible")


    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={
            "browserName": "chrome",
        })

        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна


        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_method_admin_authorization(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось




    def tear_down(self):
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



