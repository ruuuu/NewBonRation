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
from random import randint
import string
# import pytest

class Registartion(unittest.TestCase):

    def generation_tel_phone(self): # генерит номер телфона

        list_digits = []
        for i in range(0, 11):
            if i != 0:
                # print(string.digits[randint(0,9)]) # 0123456789
                list_digits.append(string.digits[randint(1, 9)])

        # print(list_digits)

        return str(str(8) + ''.join(list_digits))


    def registration(self, driver):
        driver.get("https://devclient.bonration.ru/main")  # меням на lifestyle


        try:
            button_voity = driver.find_element_by_xpath(
                "//button[@class='btn btn-border btn-border-black login-btn']")  # у тега button  есть атрибут  class со значение btn btn-border btn-border-black login-btn
            if button_voity.is_displayed(): # елси кнопка видна, то дальнейшие ейсвтия в скобках
                button_voity.click()

        except:
            print("button_voity is not founded or not clickablse")


        # ссылка Регитсрация:
        registaration_link = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//a[@href='/main?popup=registration']")))
        registaration_link.click()

        time.sleep(2)

        # нажимамем на кнпоку Крестик:

        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn ls-modal-close-btn']"))).click()
        time.sleep(2)

        registaration_link.click()
        time.sleep(2)
        name_filed = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//input[@formcontrolname='name']")))
        name_filed.send_keys("company name")

        time.sleep(2)

        email_filed = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//input[@formcontrolname='email']")))
        email_filed.send_keys("hsdkhadfjafj@yandex.ru")

        phone_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//input[@formcontrolname='phone']")))
        phone_field.send_keys(self.generation_tel_phone())

        password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//input[@formcontrolname='password']")))
        password_field.send_keys(str(randint(1000, 9999)))

        check_box_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn checkbox policy-checkbox checkbox-btn']")))
        check_box_field.click()


        button_registration = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//button[@class='btn btn-fill btn-fill-full ripple']")))[1]

        if button_registration.is_enabled():  # если элемент-кнопка кликабельна(нездизейблина), то далбнейшие дествия те, что в скобках
            button_registration.click()
        else:
            print("button_registration is not clickable")

       
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна

        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()

    def test_method_main(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.registration(driver)  # вызов метода,котрый выше

        time.sleep(5)  # чтобы сразу окно не закрывалось

    def tear_down(self):
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



