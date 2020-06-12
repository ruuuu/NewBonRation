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
from random import randint
import string


import pytest
 # здесь  htubnchfwbz админа(компаний)

class Admin_registration(unittest.TestCase):


    def my_metho_randem_stroka(self, kolvo_bukv_v_slove, count_slov):

        list_slov = []
        # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

        for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

            list_bukv = []
            for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                list_bukv.append(' '.join([self.list_characters[randint(0, len(self.list_characters) - 1)]]))

            list_slov.append(''.join(list_bukv))

        return str(' '.join(list_slov))


    def my_metho_randem_stroka_for_email(self, kolvo_bukv_v_slove, count_slov):

        list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'W', 'X', 'Y', 'Z',
                           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'w', 'x', 'y', 'z',
                           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        list_slov = []
        # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

        for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

            list_slov = []
            # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

            for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

                list_bukv = []
                for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                    list_bukv.append(' '.join([list_characters[randint(0, len(list_characters) - 1)]]))

                list_slov.append(''.join(list_bukv))

        for_email = {0: "@yandex.ru", 1: "@mail.ru", 2: "@gmail.com"}
        return str(' '.join(list_slov)) + for_email[randint(0, 2)]


    def generation_tel_phone(self):  # генерит номер телфона

        list_digits = []
        for i in range(0, 11):
            if i != 0:
                # print(string.digits[randint(0,9)]) # 0123456789
                list_digits.append(string.digits[randint(1, 9)])





    def admin_registration(self, driver): # регитсрация

        driver.get("https://devadmin.bonration.ru/external/login")

        # кнопка Регитсрация
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@class='ls-white-btn mat-raised-button']"))).click()

        time.sleep(2)
        try:
           name_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='name']")))
           name_field.send_keys(self.my_metho_randem_stroka(randint(5, 10), 1))
        except:
            time.sleep(5)


        time.sleep(2)
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//div[@class='mat-select-arrow']"))).click() # нажимаем на стрелки
        time.sleep(2)
        # спсиок городов:
        list_cities = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))

        rand_index_for_city = randint(0, len(list_cities)-1)
        list_cities[rand_index_for_city].click() # выбираем рандомныйй город

        time.sleep(2)

        #поле email
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='email']"))).send_keys(self.my_metho_randem_stroka_for_email(randint(7, 10), 1))
        time.sleep(2)

        # поле пароль
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))).send_keys("password")

        time.sleep(2)
        # чекбокс:
        for i in range(0,1):

            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin']"))).click()
            time.sleep(2)

        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//span[@class='mat-button-wrapper']"))).click()







    def setUp(self):
        self.driver = webdriver.Chrome()

        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
        self.list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                'R',
                                'S', 'T', 'U', 'W', 'X', 'Y', 'Z',
                                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q',
                                'r',
                                's', 't', 'u', 'w', 'x', 'y', 'z',
                                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_method_admin_registration(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.admin_registration(driver)  # вызов метода,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось




    def tear_down(self):
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



