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
import string
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, NoSuchAttributeException

# import pytest
 # здесь  авторизация админа(компаний)

class Admin_edit_profile_company(unittest.TestCase):




    def authorization(self, driver): # авторизация

        driver.get("https://devadmin.bonration.ru/external/login")
        time.sleep(4)

        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-0']" )))#
            email_field.send_keys("wyvzmp5iy5oh@mail.ru")
        except TimeoutError:
            print("email_field is not founded")

        try:
            password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-1']" )))
            password_field.send_keys("qwerty")
        except TimeoutError:
            print("password_field is not founded")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                       "/html/body/app-root/portal-login/div/mat-card/mat-card-content[2]/div/div/div/app-spinner-button/button")))
        if button_voity.is_displayed():  # если кнпока видна , то
            button_voity.click()


    def generation_tel_phone(self): # генерит номер телфона

        list_digits = []
        for i in range(0, 11):
            if i != 0:
                # print(string.digits[randint(0,9)]) # 0123456789
                list_digits.append(string.digits[randint(1, 9)])

        # print(list_digits)

        return str(str(8) + ''.join(list_digits))


    def setUp(self):

        #self.driver = webdriver.Chrome()

        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={
            "browserName": "chrome",
        })

        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
        self.list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                'R', 'S',
                                'T', 'U', 'W', 'X', 'Y', 'Z',
                                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q',
                                'r', 's',
                                't', 'u', 'w', 'x', 'y', 'z',
                                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', ' ']  # поле

        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_method_admin_edit_profile_company(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось

        # нажимаем вкладку Профиль компании
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//h3[@class='mat-line']")))[6].click()

        #удаляем и добавляем фото(главное)
        time.sleep(6)
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@type='button']")))[0].click()  # кнопка "удалить фото"
        time.sleep(3)

        file_dicitionary = {0: "/Users/rufina/Desktop/dishs/BjJ6inaYiWam0GGViLFHLQ-double.jpg",
                            1: "/Users/rufina/Desktop/dishs/4Rve51WmWfk.jpg", 2: "/Users/rufina/Desktop/dishs/2531.jpg",
                            3: "/Users/rufina/Desktop/dishs/salat_kinoa.jpg__1499258543__50030.jpg",
                            4: "/Users/rufina/Desktop/dishs/4703.jpg", 5: "/Users/rufina/Desktop/dishs/caption (1).jpg"}

        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(file_dicitionary[randint(0, len(file_dicitionary) - 1)]) # в в индовс  "C:\\Users\\usse\\Desktop\\тест_блюда\\rsp.jpg"

        time.sleep(2)
        # удаляем и меняем фото(лого):
        #  кнопка "удалить фото"
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@type='button']")))[1].click()

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(file_dicitionary[randint(0, len(file_dicitionary) - 1)])  #в в индовс  "C:\\Users\\usse\\Desktop\\тест_блюда\\rsp.jpg"

        time.sleep(2)
        #вводим нащзвание компаии
        name_company = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='name']")))

        name_company.clear()# очишает поле прежде чем его заполнять
        i = 0
        while i < randint(5, 100):
            index_character = randint(0, len(self.list_characters) - 1)  # берет рандомный икднек сбуквы из спсика всех букв
            name_company.send_keys(self.list_characters[index_character])
            i += 1

        time.sleep(2)
        address_company = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='address']")))
        address_company.clear()
        time.sleep(2)
        i = 0
        while i < randint(5, 100):
            index_character = randint(0, len(
                self.list_characters) - 1)  # берет рандомный икднек сбуквы из спсика всех букв
            address_company.send_keys(str(self.list_characters[index_character]))
            i += 1


        phone_company = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='phone']")))
        phone_company.clear()
        phone_company.send_keys(self.generation_tel_phone())

        time.sleep(2)

        # время начала
        # выбираем из списка часы рвботы
        list_arrows = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='mat-select-arrow']")))
        list_arrows[0].click()

        # спсиок всех item даты начала:
        items_start_clock = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))
        rand_index_of_start_item = randint(0, len(items_start_clock)-1)

        items_start_clock[rand_index_of_start_item].click()# кликаме рандомный item

        # if item_start_clock.is_displayed():  # если item виден , то
        #     time.sleep(1)
        #     item_start_clock.click()
        # else:
        #     #скроллим к нужному элменту
        #     actions = ActionChains(driver)  # создаем объект клааса ActionChains
        #     time.sleep(1)
        #     actions.move_to_element(item_start_clock).perform()  #переходим к нужному элементу
        #     time.sleep(1)
        #     item_start_clock.click()
        #
        #


        time.sleep(2)
        list_arrows[1].click()

        # Время окончания :
        time.sleep(2)# выбираем из списка часы рвботы
        items_end_clock = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))
        rand_index_of_end_item = randint(0, len(items_end_clock) - 1) # выбираем аномный item

        items_end_clock[rand_index_of_end_item].click()  # кликаме рандомный item

        # if item_end_clock.is_displayed():# если item виден , то
        #     time.sleep(1)
        #     item_end_clock.click()
        # else:
        #     # скроллим к нужному элменту
        #     actions = ActionChains(driver)  # создаем объект клааса ActionChains
        #     time.sleep(1)
        #     actions.move_to_element(item_end_clock).perform()  # переходим к нужному элементу
        #     time.sleep(1)
        #     item_end_clock.click()

        time.sleep(2)

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//*[@id='portal-layout']/app-profile/div/div/form/div[2]/div[3]/div[2]/button/span/mat-icon"))).click()  # кнопка пуговка у доствок заказкво утром
        time.sleep(2)

        # Доставка заказков (Утро) от :
        list_arrows[2].click()
        time.sleep(2)
        # выбираем из списка часы
        items_start_clock_delivery_morning = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))

        rand_index_of_moring_clock = randint(0, len(items_start_clock_delivery_morning)-1)

        items_start_clock_delivery_morning[rand_index_of_moring_clock].click()


        # if item_start_clock_delivery_morning.is_displayed(): # если item  виден то жмем
        #     item_start_clock_delivery_morning.click()


        # else:
        #     # скроллим к нужному элменту
        #     actions = ActionChains(driver)  # создаем объект клааса ActionChains
        #     time.sleep(1)
        #     actions.move_to_element(item_start_clock_delivery_morning).perform()  # переходим к нужному элементу
        #     time.sleep(1)
        #     item_start_clock_delivery_morning.click()
        #




        # Доставка заказков (Утро) до :
        list_arrows[3].click()
        time.sleep(2)

        # выбираем из списка часы
        items_end_clock_delivery_morning = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))

        rand_index_of_item_till_morning = randint(0, len(items_end_clock_delivery_morning)-1)

        items_end_clock_delivery_morning[rand_index_of_item_till_morning].click()

        # if item_end_clock_delivery_morning.is_displayed():  # если item  виден то жмем
        #     item_end_clock_delivery_morning.click()
        #
        #
        # else:
        #     # скроллим к нужному элменту
        #     actions = ActionChains(driver)  # создаем объект клааса ActionChains
        #     time.sleep(1)
        #     actions.move_to_element(item_end_clock_delivery_morning).perform()  # переходим к нужному элементу
        #     time.sleep(1)
        #     item_end_clock_delivery_morning.click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//*[@id='portal-layout']/app-profile/div/div/form/div[2]/div[4]/div[2]/button/span/mat-icon"))).click()  # кнопка пуговка у доствок заказкво вечером
        time.sleep(2)

        # Доставка заказво (Вечер)от :
        list_arrows[4].click()
        time.sleep(2)

        # выбираем из списка часы
        item_start_clock_delivery_evening = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))

        rand_index_of_evening_from_item = randint(0, len(item_start_clock_delivery_evening)-1)

        item_start_clock_delivery_evening[rand_index_of_evening_from_item].click()
        # if item_start_clock_delivery_evening.is_displayed():
        #     item_start_clock_delivery_evening.click()
        #
        #
        # else:
        #     # скроллим к нужному элменту
        #     actions = ActionChains(driver)  # создаем объект клааса ActionChains
        #     time.sleep(1)
        #     actions.move_to_element(item_start_clock_delivery_evening).perform()  # переходим к нужному элементу
        #     time.sleep(1)
        #     item_start_clock_delivery_evening.click()


        # Доставка заказво (Вечер)до :

        list_arrows[5].click()
        time.sleep(2)

        # выбираем из списка часы
        items_end_clock_delivery_evening = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))

        rand_index_of_evening_till_item = randint(0, len(items_end_clock_delivery_evening)-1)

        items_end_clock_delivery_evening[rand_index_of_evening_till_item].click()


        # if item_end_clock_delivery_evening.is_displayed():  # если item  виден то жмем
        #     item_end_clock_delivery_evening.click()
        #
        # else:
        #     # скроллим к нужному элменту
        #     actions = ActionChains(driver)  # создаем объект клааса ActionChains
        #     time.sleep(1)
        #     actions.move_to_element(item_end_clock_delivery_evening).perform()  # переходим к нужному элементу
        #     time.sleep(1)
        #     item_end_clock_delivery_evening.click()

        time.sleep(2)
        # Прием заявок:
        list_arrows[6].click()
        time.sleep(2)

        # выбираем из списка часы
        items_accept = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))

        rand_index_of_item_accept = randint(0, len(items_accept)-1)
        items_accept[rand_index_of_item_accept].click()


        # if item_accept.is_displayed():  # если item  виден то жмем
        #     item_accept.click()
        # else:
        #     # скроллим к нужному элменту
        #     actions = ActionChains(driver)  # создаем объект клааса ActionChains
        #     time.sleep(1)
        #     actions.move_to_element(item_accept).perform()  # переходим к нужному элементу
        #     time.sleep(1)
        #     item_accept.click()

        time.sleep(2)

        # тип оплаты выбираем чекбох (онлайн, курьеру наличными)
        i = 0
        # for ch in driver.find_elements_by_xpath("//div[@class='mat-checkbox-inner-container']"):# из списка чекбоксов
        #   if (i == 1 ):
        #     ch.click()
        #   i += 1

        list_checkboxs = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='mat-checkbox-inner-container']")))

        for i in range(0,3):
            list_checkboxs[i].click()
            time.sleep(1)

        #rand_index_chebox = randint(0, len(list_checkboxs)-1)
        for i in range(0, 3):
            if list_checkboxs[i].is_selected(): # если четкбок выделен
                continue # переходит на следующую итерацию
            else:
                list_checkboxs[i].click()
                break # как только чекнули оин раз так сразу выходим


        time.sleep(2)
        # texaerea:
        text = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname='about']")))

        text.clear()
        time.sleep(2)

        i = 0
        while i < randint(5, 200):
            index_character = randint(0, len(self.list_characters) - 1)  # берет рандомный икднек сбуквы из спсика всех букв
            text.send_keys(str(self.list_characters[index_character]))
            i += 1

        time.sleep(2)

        #тогглер: За баллы
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//div[@class='mat-slide-toggle-thumb']"))).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='mat-slide-toggle-thumb']"))).click()

        # нажимаем на кнпоку "отмена":
        #WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='mat-button mat-primary']"))).click()#кнопка Отмена
        #time.sleep(3)
        #WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//app-spinner-button[@class='ng-star-inserted']"))).click() # в попаапе

        time.sleep(2)

        # кнопка "Сохранить"

        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='mat-raised-button mat-primary ng-star-inserted']"))).click()

        time.sleep(10)  # много сек ставлю, чтобы успелось сохраниться и вышел попао с подтверждением об сохрании изменений


    def tear_down(self):
        time.sleep(8)# тобы окно сразу не закрывалось
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



