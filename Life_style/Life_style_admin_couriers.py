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
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, NoSuchAttributeException
import string

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, NoSuchAttributeException

# ильтрация оп названи, еалорийносии, весу и поиск

class Admin_couriers(unittest.TestCase):




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

        # print(list_digits)

        return str(str(8) + ''.join(list_digits))


    def add_courir(self):
        # кнопка Добвить
        WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(
            (By.XPATH, "//*[@id='portal-layout']/app-couriers/div/div/div/div/div[2]/button/span"))).click()
        time.sleep(2)
        # кнопка Отмена в поапе
        WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='mat-button mat-primary']"))).click()
        time.sleep(2)
        # еще разжмем кнпоку Доавить
        WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(
            (By.XPATH, "//*[@id='portal-layout']/app-couriers/div/div/div/div/div[2]/button/span"))).click()
        time.sleep(2)

        WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='name']"))).send_keys(
            self.my_metho_randem_stroka(randint(1, 8), randint(1, 3)))

        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='phone']"))).send_keys(
            self.generation_tel_phone())

        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='email']"))).send_keys(
            self.my_metho_randem_stroka_for_email(randint(2, 14), 1))
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))).send_keys(
            self.my_metho_randem_stroka(randint(5, 10), 1))
        time.sleep(2)
        # кнпока Регитсрация
        WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='mat-raised-button mat-primary ng-star-inserted']"))).click()
        time.sleep(3)

    def delete_courier(self):

        time.sleep(3)
        # спсиок конопок Удалить
        list_of_delete_buttons = WebDriverWait(self.driver, 20).until(
            ec.presence_of_all_elements_located((By.XPATH, "//button[@class='mat-button mat-warn']")))
        rand_index_of_delete_button = randint(0, len(list_of_delete_buttons) - 1)
        list_of_delete_buttons[rand_index_of_delete_button].click()
        time.sleep(2)
        # кнопка Отмена в попапе
        WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='mat-button mat-primary']"))).click()
        time.sleep(2)
        list_of_delete_buttons[rand_index_of_delete_button].click()
        time.sleep(2)
        # кнопка Ок в паопе
        WebDriverWait(self.driver, 20).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='mat-raised-button mat-primary ng-star-inserted']"))).click()
        time.sleep(2)


    def setUp(self):

        self.driver = webdriver.Chrome()#


        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
        self.list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'W', 'X', 'Y', 'Z',
                           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'w', 'x', 'y', 'z',
                           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_admin_couriers(self):  # главный метод, надо чтобы он начинался  с test_


            driver = self.driver
            self.authorization(driver)  # вызов метода,котрый выше
            time.sleep(4)  # чтобы сразу окно не закрывалось

            # раздел Курьеры:
            WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,
                                                                                     "//a[@href='/main/couriers']"))).click()

            time.sleep(6)
            self.add_courir()# вызов сметода доавления курьера
            self.delete_courier()# метод удаления курьера
            time.sleep(2)






    def tear_down(self):
        time.sleep(5)# чтобы окно сразу не закрывалось
        self.driver.close()



if __name__ == "__main__":
    unittest.main()



