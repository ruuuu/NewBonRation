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


class Admin_promouters(unittest.TestCase):


    def authorization(self, driver): # авторизация

        driver.get("https://devadmin.bonration.ru/external/login")


        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-0']" )))#
            email_field.send_keys("b10ocgshrnwu@mail.ru")
        except :
            time.sleep(5)
            email_field.send_keys("b10ocgshrnwu@mail.ru")

        try:
            password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-1']" )))
            password_field.send_keys("password")
        except:
            time.sleep(5)
            password_field.send_keys("password")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                       "/html/body/app-root/portal-login/div/mat-card/mat-card-content[2]/div/div/div/app-spinner-button/button")))
        if button_voity.is_displayed():  # если кнпока видна , то
            button_voity.click()
            print("button is visible")


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

        for i in range(count_slov):  # цикл по колву слов,

            list_slov = []
            # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

            for k in range(count_slov):  # цикл по колву слов,

                list_bukv = []
                for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                    list_bukv.append(' '.join([list_characters[randint(0, len(list_characters) - 1)]]))

                list_slov.append(''.join(list_bukv))

        for_email = {0: "@yandex.ru", 1: "@mail.ru", 2: "@gmail.com"}
        return str(' '.join(list_slov)) + for_email[randint(0, 2)]



    def my_metho_randem_stroka_for_promocode(self, kolvo_bukv_v_slove, count_slov):


        list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'W', 'X', 'Y', 'Z',
                           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'w', 'x', 'y', 'z',
                           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        list_slov = []
        for i in range(count_slov):  # цикл по колву слов,

            list_slov = []
            # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

            for k in range(count_slov):  # цикл по колву слов,

                list_bukv = []
                for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                    list_bukv.append(' '.join([list_characters[randint(0, len(list_characters) - 1)]]))

                list_slov.append(''.join(list_bukv))


        return str(' '.join(list_slov))








    def generation_tel_phone(self):  # генерит номер телфона

        list_digits = []
        for i in range(0, 11):
            if i != 0:
                # print(string.digits[randint(0,9)]) # 0123456789
                list_digits.append(string.digits[randint(1, 9)])

        # print(list_digits)

        return str(str(8) + ''.join(list_digits))


    def add_promouter(self):

        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/superadmin/promoters']"))).click()
        time.sleep(5)

        # кнопка Добавить
        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//*[@id='portal-layout']/app-super-layout/mat-sidenav-container/mat-sidenav-content/div/div/div/app-promoters/div/div/div/div/button"))).click()
        time.sleep(2)

        # кнпока Закртыия в окне
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//button[@class='btn ls-close-btn']"))).click()
        time.sleep(1)

        #  снова кнопка Добавить
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@id='portal-layout']/app-super-layout/mat-sidenav-container/mat-sidenav-content/div/div/div/app-promoters/div/div/div/div/button"))).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='name']"))).send_keys(self.my_metho_randem_stroka(randint(5,10), randint(1,2)))
        time.sleep(1)


        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='phone']"))).send_keys(self.generation_tel_phone())

        time.sleep(1)

        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='email']"))).send_keys(
            self.my_metho_randem_stroka_for_email(randint(1, 10), 1))
        time.sleep(1)

        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='post']"))).send_keys(self.my_metho_randem_stroka(randint(5,10), randint(1,3)))

        time.sleep(1)

        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='organization']"))).send_keys(
            self.my_metho_randem_stroka(randint(5, 10), randint(1, 3)))

        time.sleep(1)

        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='percent']"))).send_keys(randint(1,100))

        time.sleep(1)

        WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='promocode']"))).send_keys(self.my_metho_randem_stroka_for_promocode(randint(1, 12), 1))

        time.sleep(1)

        # жмем кнпку Сохранить
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH,  "//button[@class='mat-raised-button mat-primary ng-star-inserted']"))).click()

        time.sleep(2)



    def setUp(self):
        self.driver = webdriver.Firefox()

        self.driver.set_window_position(0, 0)  #  для сафари убмораем эту строку устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна


        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()
        self.list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'W', 'X', 'Y', 'Z',
                           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'w', 'x', 'y', 'z',
                           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def test_method_admin_promouters(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось
        self.add_promouter()  # вызов метода,котрый выше



    def tear_down(self):
        self.driver.close()
        self.driver.quit()

        # pass




if __name__ == "__main__":
    unittest.main()



