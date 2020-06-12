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
from random import randint
 # здесь  создание промокода

class Admin_create_promokode(unittest.TestCase):


    def my_metho_randem_stroka(self, kolvo_bukv_v_slove, count_slov):

        list_slov = []
        # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

        for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

            list_bukv = []
            for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                list_bukv.append(' '.join([self.list_characters[randint(0, len(self.list_characters) - 1)]]))

            list_slov.append(''.join(list_bukv))

        return str(' '.join(list_slov))



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
            #print("button is visible")


    def setUp(self):
        self.driver = webdriver.Chrome()

        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
        self.list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'W', 'X', 'Y', 'Z',
                           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'w', 'x', 'y', 'z',
                           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_method_admin_create_promocode(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(2)  # чтобы сразу окно не закрывалось

        # жме радел прмокды
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//a[@href='/superadmin/promocodes']"))).click()
        time.sleep(8)

        # # # спсиок конопок Удалитьу промокодов
        # list_deletes = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@class='mat-button mat-warn']")))
        #
        # rand_index_of_delete_buttons = randint(0,len(list_deletes)-1)
        #
        # list_deletes[rand_index_of_delete_buttons].click() # берем рандомную кнопку Удалить и удаляем
        # time.sleep(2)
        #
        # #  впопапе нажимаем на Отмену
        # WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='mat-button mat-primary']"))).click()
        #
        # rand_index_of_delete_buttons_1 = randint(0, len(list_deletes) - 1)
        # list_deletes[rand_index_of_delete_buttons_1].click()  # берем рандомную кнопку Удалить и удаляем
        # time.sleep(3)
        #
        # #  в поапе жме ок:
        # WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='mat-raised-button mat-primary ng-star-inserted']"))).click()
        #time.sleep(5)






        # кнопка ДОбавиь на странице всех промокодов
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//*[@id='portal-layout']/app-super-layout/mat-sidenav-container/mat-sidenav-content/div/div/div/app-superadmin-promocodes/div/div/div/div/button/span"))).click()
        time.sleep(5)


        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Название']"))).send_keys(self.my_metho_randem_stroka(randint(5, 9), randint(2, 4)))

        time.sleep(1)
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Придумайте промокод (до 12 символов)']"))).send_keys(self.my_metho_randem_stroka(randint(1, 12), 1))
        time.sleep(2)




        # срок действия Начало, жмем на иконку календаря
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Начало']"))).click()

        time.sleep(5)

        # список достпных дат, (незадизейбленных)
        list_dates_1 = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//td[@class='mat-calendar-body-cell ng-star-inserted']")))

        for i in range(0, len(list_dates_1)): # проходимся оп всем датам
            rand_index_date_1 = randint(0, len(list_dates_1)-1)

            print("list_dates_1 is equal", len(list_dates_1), "rand_index_date_1 is equal", rand_index_date_1)
            print("list_dates_1[rand_index_date_1].is_enabled() equal", list_dates_1[rand_index_date_1].is_enabled())
            if list_dates_1[rand_index_date_1].is_enabled(): # если дата активная то

                list_dates_1[rand_index_date_1].click() # кликаме рандомную дату
                break # как только кликнули, так сразу выходит из цикла
        time.sleep(3)

        #  срок действия Конец, жмем на иконку календаря
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Конец']"))).click()

        time.sleep(2)

        # список достпных дат, выбираем конец действия
        list_dates_2 = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//td[@class='mat-calendar-body-cell ng-star-inserted']")))
        rand_index_date_2 = randint(0, len(list_dates_2) - 1)

        time.sleep(6)
        print("list_dates_2 is equal", len(list_dates_2), "rand_index_date_2 is equal", rand_index_date_2)



        if list_dates_2[rand_index_date_2].is_enabled() is False: # если выбранная дата неклибклаьеная
             print("list_dates_2[rand_index_date_2].is_enabled() is False daet", list_dates_2[rand_index_date_2].is_enabled() is False)
             i = 0
             while list_dates_2[rand_index_date_2].is_enabled() is False: # покa кнпока некликбаельна идем дальше
                 rand_index_date_2 += 1
                 i += 1

             print("count i equal", i)
             new_rand_index_date_2 = rand_index_date_2
             print("new_rand_index_date_2 equal", new_rand_index_date_2)
             list_dates_2[new_rand_index_date_2].click()  # кликаме рандомную  кликабельную дату

        else:
             list_dates_2[rand_index_date_2].click()

        time.sleep(3)
        # #
        # #
        # #
        # # #----------------------------------------------------------------------------------
        # #
        # #
        # #
        list_type_radio_buttons = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//div[@class='mat-radio-container']"))) # спсиок радиокнопко (Регитсрация и  Заказ)

        rand_index_of_radio = randint(0, len(list_type_radio_buttons) - 1)  # выбираем ранломную кнпоку

        list_type_radio_buttons[rand_index_of_radio].click()
        time.sleep(3)
        if rand_index_of_radio == 0:  # если выбрали Регитсрация
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Кол-во бонусов']"))).send_keys(randint(1,100)) # вбиваем кол-во бонусов
            time.sleep(2)

        else:

            #  выбираем тип промокода: кдикаем на Выберите геолокацию
            select_geolocatin = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//mat-select[@placeholder='Выберите геолокацию']")))
            driver.execute_script("arguments[0].scrollIntoView(true);", select_geolocatin)  # скриллим к этому элемементу(который не виден)  v ПОМОГЛО!!и элемент этот подтянется к верху станицы
            time.sleep(4)
            select_geolocatin.click()
            time.sleep(2)

            # # список itemov геолокации
            list_items = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH,"//mat-option[@class='mat-option ng-star-inserted']")))

            rand_index_of_item = randint(0, len(list_items)-1)
            print("index of item geolocation equal",  rand_index_of_item)
            list_items[rand_index_of_item].click()
            time.sleep(3)

            # if rand_index_of_item == 0: # если выбрали пункт Везед
            #     pass

            if rand_index_of_item == 0: # если выбрали пункт Город

                WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//mat-select[@formcontrolname='city']"))).click() # жмем на поле Выберите городо
                time.sleep(3)
                list_cities_1 = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))# список городов
                rand_index_of_city = randint(0, len(list_cities_1)-1)# ранломный индекс города
                print(" vybrali geolaka gorod, rand_index_of_city equal", rand_index_of_city)

                list_cities_1[rand_index_of_city].click() # кликаме рандомный город



            if rand_index_of_item == 1:  # если выбрали пункт Компания

                WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//mat-select[@placeholder='Выберите город']"))).click()  #клкаме на  поле  Выберите город
                time.sleep(2)

                list_cities = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']")))  # itemy городов
                rand_index_of_city = randint(0, len(list_cities)-1)  # ранломный индекс города
                list_cities[rand_index_of_city].click()  # кликаме рандомный город
                time.sleep(2)
                WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//mat-select[@placeholder='Выберите компанию']"))).click()
                time.sleep(2)

                list_comapanies = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']"))) # itmy  компаний
                rand_index_of_campany = randint(0, len(list_comapanies)-1) # рандомный индекс компании
                print(" vybrali geolaka Kommpanya, rand_index_of_campany equal", rand_index_of_campany)
                list_comapanies[rand_index_of_campany].click()
                time.sleep(2)

                WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//mat-select[@placeholder='Выберите рацион']"))).click()  # клкаме поле  Выберите рацион
                time.sleep(2)
                list_rations = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@class='mat-option ng-star-inserted']"))) # itemy рационов

                rand_index_of_ration = randint(0, len(list_rations)-1)
                list_rations[rand_index_of_ration].click()

            time.sleep(2)

            list_type_radio_buttons = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//div[@class='mat-radio-container']"))) # спсиок радиокнопко

            rand_index_of_radio = randint(2, len(list_type_radio_buttons)-1) # выбираем ранломную кнпоку

            list_type_radio_buttons[rand_index_of_radio].click()
            time.sleep(3)

            if rand_index_of_radio == 2: # если выбрали "Процент от заказа"
                WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Процент от заказа']"))).send_keys(str(randint(1,100)))


            if rand_index_of_radio == 3: # если выбрали  "Скидка в рублях от заказа"
                WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Скидка (₽)']"))).send_keys(str(randint(1, 1000)))

            # выбраем чекбоксы: Способ оплаты
            time.sleep(2)
            # спсиок чекбоксов
            list_check_boxs = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='mat-checkbox-inner-container']")))


            # способ оплаты:
            for i in range(0, len(list_check_boxs)):
                 rand_index_of_check_boxes = randint(0, len(list_check_boxs)-1) # берет ранломный индекс чекбкса
                 list_check_boxs[rand_index_of_check_boxes].click()
                 time.sleep(2)

        # кнопка Сохранить
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//button[@class='mat-raised-button mat-primary ng-star-inserted']"))).click()
        time.sleep(5)



    def tear_down(self):
        time.sleep(3)
        #self.driver.quit()
        self.driver.close()
        #pass


if __name__ == "__main__":
    unittest.main()



