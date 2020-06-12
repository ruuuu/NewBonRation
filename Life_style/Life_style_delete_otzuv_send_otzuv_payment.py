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
# import pytest


class Delete_otzuv_send_review_payment(unittest.TestCase):

#нужно чтобы были кнпоки оставть отзыв в Исотрия заказков


    def authorization(self, driver): # авторизация

        driver.get("https://devclient.bonration.ru/main") # меням на lifestyle

        button_voity = driver.find_element_by_xpath(
            "//button[@class='btn btn-border btn-border-black login-btn ripple']")  # у тега button  есть атрибут  class со значение btn btn-border btn-border-black login-btn
        button_voity.click()

        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@type='email']" )))# /html/body/app-root/app-modal/div/div[1]/div/app-login/div/div[2]/form/div[1]/input
            email_field.send_keys("rufinka_91@mail.ru")
        except :
            print("время ожидания поля емэйл вышло")

        try:
            password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']" )))
            password_field.send_keys("7071991")
        except :
            print("время ожидания поля пароль вышло")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-fill btn-fill-full needsclick ripple']")))
        button_voity.click()
        time.sleep(3)









    def online_oplata(self, driver): # нажав на кнпоку Отплатви в  Заказы ,в раделе Текущие
        try: # если есть кнока Оплатить то жмем
            #список  кнопок оплатить:
            list_oplatits = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn btn-flat btn-flat-upper ripple']")))
            rand_index_of_button_oplatit = randint(0, len(list_oplatits)-1)
            time.sleep(2)
            driver.execute_script("arguments[0].scrollIntoView(true);",
                                  list_oplatits[rand_index_of_button_oplatit])  # скриллим к этому элемементу(который не виден) calendar ПОМОГЛО!!
            time.sleep(2)
            list_oplatits[rand_index_of_button_oplatit].click()

            time.sleep(2)
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@name='pan']"))).send_keys(
                "4111 1111 1111 1111")


            time.sleep(1)
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@name='cardholder']"))).send_keys(
                "jdfhgljsh sgljsdhgds")
            time.sleep(1)
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@name='expired']"))).send_keys(
                "12/19")
            time.sleep(1)
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@name='cvc']"))).send_keys("123")
            time.sleep(1)
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@id='submit']"))).click()  # оплатить
            time.sleep(2)
            password_field = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//input[@type='password']")))
            password_field.clear()
            time.sleep(2)
            password_field.send_keys("12345678")

            time.sleep(2)
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@value='Submit']"))).click()
            time.sleep(2)
        except:
            pass

    def setUp(self):

        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
         # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()

        self.list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                        'Q',
                                        'R', 'S',
                                        'T', 'U', 'W', 'X', 'Y', 'Z',
                                        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p',
                                        'q',
                                        'r', 's',
                                        't', 'u', 'w', 'x', 'y', 'z',
                                        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '&', '#', '*', '(', ')', '"',
                                        ',',
                                        '/', ']',
                                        '[', '}', '{', '"', '?', '!', '§', '±', '<', '№', ' ']  # поле


    def test_profile_delete_review_send_payment(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(3)  # чтобы сразу окно не закрывалось

        # кнопка Личный кабмнет:
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,
                                                                            "//button[@class='btn profile-btn']"))).click()

        WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='profile-drop-down-item']")))[1].click()  # item Мои отзывы
        time.sleep(2)


        # спсиок кнопок крестик
        try: # еси еть кнопки то жмет выбирая любую
            list_buttons_krestik = WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn profile-review-card-header-btn close-btn']")))

            random_index_of_buttons_krestik = randint(0, len(list_buttons_krestik ) -1) # рандомнй индекс кнопки  Крестика


            driver.execute_script("arguments[0].scrollIntoView(true);",
                                      list_buttons_krestik
                                          [random_index_of_buttons_krestik])  # скриллим к этому элемементу(который не виден) calendar ПОМОГЛО!!и элемент этот подтянется к верху станицы


            time.sleep(2)
            list_buttons_krestik[random_index_of_buttons_krestik].click()
            time.sleep(2)
        except:# если нет кнопки крестик , то  ничгоне нделает
             pass


        time.sleep(2)

        # удаляем рfндомнй отзыв:
        # спсик клноок удаления
        list_delete_buttons = WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//img[@src = '../../../assets/icons/delete.svg']")))
        random_index_of_delete_button = randint(0, len(list_delete_buttons) -1)
        print("random_index_of_delete_button equal" , random_index_of_delete_button)

        print("list_delete_buttons[random_index_of_delete_button].is_enabled() equl", list_delete_buttons[random_index_of_delete_button].is_enabled() )


        i = 0
        while list_delete_buttons[random_index_of_delete_button].is_enabled() is False:  # пока элемент не виден скроллом, как только он станет видным, выход из цикла
            print(i, "-th iteration")
            driver.execute_script("arguments[0].scrollIntoView(true);", list_delete_buttons[random_index_of_delete_button])  # скриллим к этому элемементу(который не виден) calendar ПОМОГЛО!!и элемент этот подтянется к верху станицы
            i += 1
            if list_delete_buttons[random_index_of_delete_button].is_enabled() is True:
                break # выход из цикла

        time.sleep(6)
        list_delete_buttons[random_index_of_delete_button].click()
        time.sleep(2)

        # попапе удаления жме мна кнпоку Отмена:
        WebDriverWait(driver, 20).until(ec.presence_of_element_located
                ((By.XPATH, "//button[@class='btn btn-flat-upper confirm-footer-btn btn-flat ripple']"))).click()
        time.sleep(2)

        list_delete_buttons[random_index_of_delete_button].click()
        time.sleep(2)

        # кнопка Удалить  в попапе удаления отзыва
        WebDriverWait(driver, 20).until(ec.presence_of_element_located
                ((By.XPATH, "//button[@class='btn btn-flat-upper confirm-footer-btn btn-flat-red ripple']"))).click()
        time.sleep(2)

         # на станице История заказов:
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,  "//a[@href='/profile/orders']"))).click()
        time.sleep(2)

        WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@class='ls-radio btn']")))[1].click()# История заказов
        time.sleep(2)

        try: # если есть кнпоки Оставить отзыв то жмет
        # список конпоок Остатвить отзыв
            list_buttons_ostavit_otzuv1 = WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn btn-flat btn-flat-upper ripple']")))

            random_index_of_button = randint(0, len(list_buttons_ostavit_otzuv1) - 1)

            # если чтодобавить while list_buttons_ostavit_otzuv1[random_index_of_button].is_enabled() is False: # пока элемент не виден скроллом, как только он станет видным, выход из цикла
            driver.execute_script("arguments[0].scrollIntoView(true);", list_buttons_ostavit_otzuv1[random_index_of_button])  # скриллим к этому элемементу(который не виден) calendar ПОМОГЛО!!

            time.sleep(2)
            list_buttons_ostavit_otzuv1[random_index_of_button].click() # жмем кнопку Отсавить отзыыв

            # в попапе отзыва
            list_zvezdas = WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn set-rating-btn']")))
            time.sleep(2)
            randint_zvezda = randint(0, len(list_zvezdas)-1)
            list_zvezdas[randint_zvezda].click()
            time.sleep(2)

            text = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname='message']")))

            i = 0
            while i < randint(5, 100):
                index_character = randint(0, len(self.list_characters) - 1)  # берет рандомный икднек сбуквы из спсика всех букв
                text.send_keys(str(self.list_characters[index_character]))
                i += 1
            time.sleep(4)

            # кнопка Сохранить
            WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-fill btn-fill-full ripple']"))).click()

        except: # если нет кнпоки Отсавить отзыв то ниегоне далет
            pass


        time.sleep(6)
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//button[@class='ls-radio btn']"))).click() # жмем на Текущие
        time.sleep(2)



        # Кнопка Оплатить на санице Заказы в разедле текушие:
        self.online_oplata(driver)

    def tear_down(self):
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()
