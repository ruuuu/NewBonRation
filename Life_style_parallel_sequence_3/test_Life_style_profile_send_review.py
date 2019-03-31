# -*- coding: utf-8 -*-
import time
import unittest

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


class Profile_send_review(unittest.TestCase):

# оставляем отзыв о сделанном заказе и редактируем его


    def authorization(self, driver): # авторизация

        driver.get("https://devclient.bonration.ru/main") # меням на lifestyle

        button_voity = driver.find_element_by_xpath(
            "//button[@class='btn btn-border btn-border-black login-btn ripple']")  # у тега button  есть атрибут  class со значение btn btn-border btn-border-black login-btn
        button_voity.click()

        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='email']" )))# /html/body/app-root/app-modal/div/div[1]/div/app-login/div/div[2]/form/div[1]/input
            email_field.send_keys("rufinka_91@mail.ru")
        except NoSuchElementException:
            print("email_field is not founded")

        try:
            password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']" )))
            password_field.send_keys("7071991")
        except NoSuchElementException:
            print("password_field is not founded")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-fill btn-fill-full needsclick ripple']")))
        button_voity.click()
        time.sleep(3)



    def edit_review(self, driver):

        time.sleep(3)
        actions = ActionChains(driver)
        # список кнопок редактиования(карнадаш)
        list_elements_reviews = WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
                (By.XPATH,"//button[@class='btn profile-review-card-header-btn']")))

        rand_index_of_pencel = randint(0, len(list_elements_reviews)-1)

        actions.move_to_element(list_elements_reviews[rand_index_of_pencel]).perform()  # переходим к  эулменту lest_elements_reviews[rand_index_of_pencel]
        time.sleep(3)


        list_elements_reviews[rand_index_of_pencel].click() # кликаем на выбранный каранлаш

        time.sleep(5)
        text = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname='message']")))
        text.clear()
        time.sleep(2)




        i = 0
        while i < randint(5, 100):
            index_character = randint(0, len(self.list_characters) - 1)  # берет рандомный икднек сбуквы из спсика всех букв
            text.send_keys(str(self.list_characters[index_character]))
            i += 1


        time.sleep(2)
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-fill btn-fill-full ripple']"))).click()


    def  ostavot_ovzuv_on_page_orders(self, driver):# осталвем отзыв на странице заказов

        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//a[@href='/profile/orders']"))).click()# жме мна раздел Заказы
        time.sleep(2)
        WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@class='ls-radio btn']")))[1].click() # жмем на Итсрия заказков
        time.sleep(5)

        # список конпоок Остатвить отзыв
        list_buttons_ostavit_otzuv = WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located((By.XPATH,  "//button[@class='btn btn-flat btn-flat-upper ripple']")))

        random_index_of_button = randint(0, len(list_buttons_ostavit_otzuv)-1)

        driver.execute_script("arguments[0].scrollIntoView(true);",
                              list_buttons_ostavit_otzuv[random_index_of_button])  # скриллим к этому элемементу(который не виден) calendar ПОМОГЛО!!

        time.sleep(2)

        self.poput_otzuv(driver) # вызов метода соталвения отзыва в попапе


    def poput_otzuv(self, driver):

        # В попапе нажимаем кнпоку звездочка
        random_index_zvezdy = randint(0, 4) # рандомный индек звездочки

        WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//button[@class='btn set-rating-btn']")))[random_index_zvezdy].click()  # жме мна рандомную звезду
        time.sleep(2)
        if random_index_zvezdy == 4:
            # еще раз жме мна рандомную звезду
            WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
                (By.XPATH, "//button[@class='btn set-rating-btn set-rating-btn-active']")))[randint(0, 3)].click()

        # else:
        #     # еще раз жме мна рандомную звезду
        #     indexes_zvezda = WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
        #         (By.XPATH, "//button[@class='btn set-rating-btn set-rating-btn-active']")))
        #
        #     WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
        #         (By.XPATH, "//button[@class='btn set-rating-btn']")))[len(indexes_zvezda)-2].click()


        time.sleep(2)
        # оставялем сам текст отзыва
        i = 0
        while i < randint(5, 100):
            index_character = randint(0, len(
                self.list_characters) - 1)  # берет рандомный икднек сбуквы из спсика всех букв
            WebDriverWait(driver, 20).until(ec.presence_of_element_located(
                (By.XPATH, "//textarea[@placeholder='Напишите несколько строк']"))).send_keys(
                str(self.list_characters[index_character]))
            i += 1

        time.sleep(2)
        # кнопка Сохранить
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,
                                                                        "/html/body/app-root/app-modal/div[1]/div/div/app-modal-leave-feedback/div/div[2]/form/button"))).click()






    def setUp(self):

        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={
            "browserName": "chrome",
        })
        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


        self.list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S',
                        'T', 'U', 'W', 'X', 'Y', 'Z',
                        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's',
                        't', 'u', 'w', 'x', 'y', 'z',
                        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # поле


    def test_profile_send_review(self):  # главный метод, надо чтобы он начинался  с test_

            driver = self.driver
            self.authorization(driver)  # вызов метода,котрый выше
            time.sleep(3)  # чтобы сразу окно не закрывалось

            # кнопка Личный кабмнет:
            WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,
                                                                                     "//button[@class='btn profile-btn']"))).click()


            WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='profile-drop-down-item']")))[1].click() # item Мои отзывы
            time.sleep(2)


            try:
                # спсиок кнпоок Оставить отзыв
                list_of_buttons_ostavit_otzuv = WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
                    (By.XPATH,"//button[@class='profile-review-card-header-bottom-review-btn btn btn-flat btn-flat-upper ripple']")))
                time.sleep(2)

                #print("count of buttons_ostavit_onxyz equal", len(list_of_buttons_ostavit_otzuv))
                rand_index_of__buttons_ostavit_otzuv = randint(0, len(list_of_buttons_ostavit_otzuv)-1) #  hfyljvysq bylrrn ryjgrb jcnfdbnm jnpsd

                #print("rand_index_of__buttons_ostavit_otzuv equal", rand_index_of__buttons_ostavit_otzuv)
                driver.execute_script("arguments[0].scrollIntoView(true);", list_of_buttons_ostavit_otzuv[rand_index_of__buttons_ostavit_otzuv])  # скриллим к этому элемементу(который не виден) calendar ПОМОГЛО!!и элемент этот подтянется к верху станицы
                time.sleep(2)
                list_of_buttons_ostavit_otzuv[rand_index_of__buttons_ostavit_otzuv].click() #  жмем на выбарнную кнпоку

                time.sleep(2)
                #жме мн кретсик в попапе
                WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn ls-modal-close-btn']"))).click()

                time.sleep(2)
                # еще раз жмем на кнопку Отсавть отзыв
                list_of_buttons_ostavit_otzuv[rand_index_of__buttons_ostavit_otzuv].click()  # жмем на выбарнную кнпоку
                time.sleep(2)


                self.poput_otzuv(driver)# вызов метода попапа оствелния отызва
            except NoSuchElementException:
                print("senf_review button is not founded")

            time.sleep(2)



            self.edit_review(driver) # метод редактирования отзыва
            time.sleep(2)


    def tear_down(self):

        time.sleep(5)# чтобы окно сразу не закрывалось
        self.driver.close()



if __name__ == "__main__":
    unittest.main()



