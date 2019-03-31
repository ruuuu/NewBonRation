import time
import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import Select  # работа со списками
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains # lля сколддинга к нужному элементу импортируем класс ActionChains
from random import randint

#from for_export_authorization import export_Admin_authorization # из файла for_export_authorization.py импортируиеи класс export_Admin_authorization


# import pytest
 # здесь  редактирование блюда

class Admin_edit_dishs(unittest.TestCase):

    def authorization(self, driver):  # авторизация

        driver.get("https://devadmin.bonration.ru/external/login")  # меням на lifestyle

        try:
            email_field = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-0']")))  #
            email_field.send_keys("8fzxx1cby0gy@mail.ru")
        except ValueError:
            print("you sent wrong login")

        try:
            password_field = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-1']")))
            password_field.send_keys("password3")
        except ValueError:
            print("you sent wrong password")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                       "/html/body/app-root/portal-login/div/mat-card/mat-card-content[2]/div/div/div/app-spinner-button/button")))
        if button_voity.is_enabled():  # если кнпока кликабельна, то
            button_voity.click()


    def my_metho_with_predlojenie(self, kolvo_bukv_v_slove, count_slov, count_predlojeniy):

        list_predloj = []

        for k in range(count_predlojeniy):  # цикл по колву предло;ений
            list_slov = []
            # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

            for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

                list_bukv = []
                for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                    list_bukv.append(' '.join([self.list_characters[randint(0, len(self.list_characters) - 1)]]))

                list_slov.append(''.join(list_bukv))

            list_predloj.append(' '.join(list_slov) + '.')

        return str(' '.join(list_predloj))







#   БЕРЕТ РАНДОМНОЕ БЛЮДО И РЕДАКТИРУЕТ ЕГО
    def setUp(self):

        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={
            "browserName": "chrome",
        })
        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна

        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()

        self.list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                'R', 'S',
                                'T', 'U', 'W', 'X', 'Y', 'Z',
                                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q',
                                'r', 's',
                                't', 'u', 'w', 'x', 'y', 'z',
                                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '&', '#', '*', '(', ')', '"', ',',
                                '/', ']',
                                '[', '}', '{', '"', '?', '!', '§', '±', '<', '№', ' ']  # поле




    def test_method_admin_create_dish(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше

        time.sleep(7)  # чтобы сразу окно не закрывалось

        # выбираем пункт "все блюда":
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,  "//a[@href='/main/dishes']"))).click()
        time.sleep(5)

        try:
            # жмем кнопку Добавить:
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='portal-layout']/app-dishes/div/div/div/div/div[2]/button"))).click()


            time.sleep(4)
            # нажимаем на крестик в окошке:
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn ls-close-btn']"))).click()
            time.sleep(5)

            # жмем  снова кнопку Добавить:
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//*[@id='portal-layout']/app-dishes/div/div/div/div/div[2]/button"))).click()
            time.sleep(2)

            name_dish = driver.find_element_by_xpath("//input[@placeholder='Название блюда']")



            name_dish.send_keys(str(self.my_metho_with_predlojenie(randint(6, 10), randint(4, 6), 1)))

            time.sleep(1)
            sostav_dish = driver.find_element_by_xpath("//textarea[@placeholder='Состав']")



            sostav_dish.send_keys(str(self.my_metho_with_predlojenie(randint(6, 10), randint(4, 6), randint(1, 3))))

            time.sleep(3)
            count_calory = driver.find_element_by_xpath("//input[@placeholder='Количество калорий (кк)']")



            count_calory.send_keys(str(randint(12, 9000)))

            time.sleep(1)
            count_weight = driver.find_element_by_xpath("//input[@placeholder='Вес (г)']")



            count_weight.send_keys(randint(12, 9000))



            time.sleep(1)

            file_dicitionary = {0: "/Users/rufina/Desktop/dishs/BjJ6inaYiWam0GGViLFHLQ-double.jpg", 1: "/Users/rufina/Desktop/dishs/4Rve51WmWfk.jpg", 2:"/Users/rufina/Desktop/dishs/2531.jpg", 3: "/Users/rufina/Desktop/dishs/salat_kinoa.jpg__1499258543__50030.jpg", 4: "/Users/rufina/Desktop/dishs/4703.jpg", 5:"/Users/rufina/Desktop/dishs/caption (1).jpg" }

            driver.find_element_by_xpath("//input[@type='file']").send_keys(
                file_dicitionary[randint(0, len(file_dicitionary) - 1)])

            time.sleep(3)


        # # кнопка Отмена:
        # try:
        #     cancel_button = driver.find_element_by_xpath("//button[@class='mat-button mat-primary']")
        #     if cancel_button.is_displayed():
        #         cancel_button.click()
        # except ElementNotVisibleException:
        #     print('нет кнопки Отмена')
        #
        # driver.find_element_by_xpath("//app-spinner-button[@class='ng-star-inserted']").click() # нажимаем отмнеить

            # кнопка "Сохранить":
            save_button = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//button[@class='mat-raised-button mat-primary ng-star-inserted']")))
            if save_button.is_displayed(): # если кнпока видима
                save_button.click()

            time.sleep(10)


        except ValueError:
            print("error of value")

        except SyntaxError:
            print("error of syntax")


    def tear_down(self):
        time.sleep(8)
        #self.driver.close()
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



