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


# import pytest
#

class Find_company_on_main_page(unittest.TestCase):

    def authorization(self, driver):

        driver.get("https://devclient.bonration.ru/main")

        button_voity = driver.find_element_by_xpath(
            "//button[@class='btn btn-border btn-border-black login-btn ripple']")  # у тега button  есть атрибут  class со значение btn btn-border btn-border-black login-btn
        button_voity.click()

        # заоплняем форму авторизации:
        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//input[@formcontrolname='email']")))
            email_field.send_keys("rufinka_91@mail.ru")
        except TimeoutError:
            print("время ожидания поля емэйл вышло")

        password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//input[@formcontrolname='password']")))
        if password_field.is_displayed(): # если поле вилимое то
            password_field.send_keys("rufina")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn btn-fill btn-fill-full needsclick ripple']")))

        if button_voity.is_displayed():  # если элемент видимый, то далбнейшие дествия те, что в скобках
            button_voity.click()


    def setUp(self):
     #
        self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_method_find_company(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше

        time.sleep(5)  # чтобы увидеть

        #поле поиск по названию компании на гланйо станице
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Поиск по названию компании']"))).send_keys("Жить здорово")
        time.sleep(2)
        # кнопка Поиск
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@type='submit']"))).click()

        time.sleep(2)
        driver.get("https://devclient.bonration.ru/main") # пеереходим на главную станийцу
        time.sleep(2)

        #поле колво калорий
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
            (By.XPATH,"//button[@class='btn search-drop-down-btn']")))[0].click()
        time.sleep(2)

        # из выпадающего спсика выбираем пункт:
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='drop-down-item']")))[2].click()


        #поле цена До
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//button[@class='btn search-drop-down-btn']")))[1].click()
        time.sleep(2)
        # из выпадающего спсика выбираем пункт:
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='drop-down-item']")))[1].click()

        time.sleep(2)
        # кнопка Поиск
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@type='submit']"))).click()

        time.sleep(2)
        # # фильтры на стhанице компаниq
        for i in range(4): #выбираем Веганскую
            if i == 2:
                WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='btn checkbox checkbox-btn']"))).click()

        time.sleep(2)
       # принмиают заявки на завтра
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//*[@id='app-content']/app-search-company/div/div[2]/div/div[2]/div[1]/div/div/app-search-filter/div/div[4]/label/button"))).click()

        time.sleep(4)


        # кнопка Сбросить
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='btn btn-fill btn-fill-full clear-btn ls-md-none']"))).click()


        time.sleep(6)

        # по Цене упоряочить
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='btn ls-drop-down-btn select-drop-down-btn']"))).click()

        time.sleep(3)
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
                    (By.XPATH, "//div[@class ='select-item']")))[1].click()

        time.sleep(5)

        # лого  в ерхнем левом углу
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                    (By.XPATH,"//div[@class='ls-logo']"))).click()

        time.sleep(4)

    def tear_down(self):
        time.sleep(4)
        self.driver.quit()
        # pass
        time.sleep(4)

if __name__ == "__main__":
    unittest.main()



