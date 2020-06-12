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
 # здесь  создание рациона

class Admin_create_ration(unittest.TestCase):




    def authorization(self, driver): # авторизация

        driver.get("https://devadmin.bonration.ru/external/login")


        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-0']" )))#
            email_field.send_keys("wyvzmp5iy5oh@mail.ru")
        except:
            print("email_field is not founded")

        try:
            password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-1']" )))
            password_field.send_keys("qwerty")
        except:
            print("password_field is not founded")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                       "/html/body/app-root/portal-login/div/mat-card/mat-card-content[2]/div/div/div/app-spinner-button/button")))
        if button_voity.is_displayed():  # если кнпока видна , то
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


    def my_metho_randem_stroka(self, kolvo_bukv_v_slove, count_slov): # генерит предложение

        list_slov = []
        # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

        for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

            list_bukv = []
            for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                list_bukv.append(' '.join([self.list_characters[randint(0, len(self.list_characters) - 1)]]))

            list_slov.append(''.join(list_bukv))

        return str(' '.join(list_slov))






    def setUp(self):

        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities={
            "browserName": "chrome",
        })
        #self.driver = webdriver.Chrome()
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
        #self.driver.maximize_window() # раотает только  в FF

        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()
        self.list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                'R', 'S',
                                'T', 'U', 'W', 'X', 'Y', 'Z',
                                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q',
                                'r', 's',
                                't', 'u', 'w', 'x', 'y', 'z',
                                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # поле

    def test_method_admin_create_ration(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось

        # раздел Упралвение рационами:
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH,"//h3[@class='mat-line']")))[3].click()

        time.sleep(5)
        #  вполе Поиск ищет рацион:
        find = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//input[@type='search']")))

        find.send_keys("kjfglkdfjgkldf")
        time.sleep(3)
        # нажатие на кнопку "Добавить":

        add_button = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='add-button-wrapper']")))

        add_button.click()

        time.sleep(10)

        # загрузка рисунков рациона
        file_dicitionary = {0: "/Users/rufina/Desktop/dishs/BjJ6inaYiWam0GGViLFHLQ-double.jpg",
                            1: "/Users/rufina/Desktop/dishs/4Rve51WmWfk.jpg", 2: "/Users/rufina/Desktop/dishs/2531.jpg",
                            3: "/Users/rufina/Desktop/dishs/salat_kinoa.jpg__1499258543__50030.jpg",
                            4: "/Users/rufina/Desktop/dishs/4703.jpg", 5: "/Users/rufina/Desktop/dishs/caption (1).jpg"}

        # добавляем  главное фото рациона
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(file_dicitionary[randint(0, len(file_dicitionary) - 1)])
        time.sleep(5)

        #  поле Название:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='name']"))).send_keys(self.my_metho_randem_stroka(randint(5,10), randint(1, 3)))

        time.sleep(5)
        # краткое описание
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Краткое описание']"))).send_keys(self.my_metho_with_predlojenie(randint(6, 10), randint(5, 10), randint(1, 4)))


        time.sleep(2)

        # поле калории
        field_calory = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='calories']")))

        #(660, 604)
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              field_calory)  # скриллим к этому элемементу(который не виден) field_calory ПОМОГЛО!!
        time.sleep(3)
        field_calory.send_keys(randint(1,9000))

        time.sleep(2)





        # выбмраем чекбоксы:

        vegetarion =  WebDriverWait(driver, 10).until(
             ec.presence_of_element_located((By.XPATH, "//mat-checkbox[@formcontrolname='vegetarian']")))

        driver.execute_script("arguments[0].scrollIntoView(true);",
                              vegetarion)  # скриллим к этому элемементу(который не виден) vegetarion ПОМОГЛО!!

        time.sleep(2)
        vegetarion.click()

        time.sleep(2)
        vegan = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//mat-checkbox[@formcontrolname='vegan']")))
        vegan.click()
        time.sleep(2)
        vegan.click()
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//mat-checkbox[@formcontrolname='halal']"))).click()


        time.sleep(2)

        # поле Описание рациона
        textarea = WebDriverWait(driver, 10).until(
         ec.presence_of_element_located((By.XPATH, "//div[@data-placeholder='Введите описание рациона...']"))).send_keys(self.my_metho_with_predlojenie(randint(6,10), randint(5,10), randint(1,10)))

        time.sleep(2)

        file_boxes = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//input[@type='file']")))

        for j in range(0, 3):  # прикрепляем фото, 3 фотки
            file_boxes[j].send_keys(file_dicitionary[randint(0, len(file_dicitionary) - 1)])
            time.sleep(2)

        # # 1ая картинка
        # WebDriverWait(driver, 10).until(
        #     ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(
        #     file_dicitionary[randint(0, len(file_dicitionary) - 1)])
        #
        # time.sleep(1)
        # # 2ая картинка
        # WebDriverWait(driver, 10).until(
        #     ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(
        #     file_dicitionary[randint(0, len(file_dicitionary) - 1)])
        #
        # time.sleep(1)
        # # 3ая картинка
        # WebDriverWait(driver, 10).until(
        #     ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(
        #     file_dicitionary[randint(0, len(file_dicitionary) - 1)])

        time.sleep(2)


        # поле Тип примема пищи:
        type_priem = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-select[@placeholder='Выберите тип приема пищи']")))[0]  # 0  из 8
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              type_priem)  # скриллим к этому элемементу(который не виден) type_priem ПОМОГЛО!
        type_priem.click()
        list_type_foods = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//span[@class='mat-option-text']")))  # список типов приемов пищ:  Обед6Ужин и т/д/
        time.sleep(2)
        rand_type_ondex_food = randint(0, len(list_type_foods) - 1)
        list_type_foods[rand_type_ondex_food].click()  # кликаме рандомный тип пищи

        time.sleep(2)
        #  нажимаем на поле Название блюда
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Название блюда']")))[0].click()
        time.sleep(2)
        listdishes_items = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//mat-option[@class ='mat-option ng-star-inserted']")))  # спсик блюд
        rand_index_of_dishes = randint(0, len(listdishes_items) - 1)  # выбираем арнломное блюдо из спсика
        listdishes_items[rand_index_of_dishes].click()
        time.sleep(2)

        for i in range(1, 4): # 4 приемов пищи будет
            print("om", i, "th interation:" )
            # кнпока Добавить тип приема пищи
            add_button = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='ls-white-bg mat-raised-button']")))
            driver.execute_script("arguments[0].scrollIntoView(true);",
                                  add_button)  # скриллим к этому элемементу(который не виден) calendar ПОМОГЛО!
            add_button.click()
            time.sleep(2)
            # поле Тип примема пищи:
            type_priem = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-select[@placeholder='Выберите тип приема пищи']")))[i]  # 0  из 8
            driver.execute_script("arguments[0].scrollIntoView(true);", type_priem)  # скриллим к этому элемементу(который не виден) type_priem ПОМОГЛО!
            type_priem.click()
            list_type_foods = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))  # список типов приемов пищ:  Обед6Ужин и т/д/
            time.sleep(2)
            rand_type_ondex_food = randint(0, len(list_type_foods) - 1)
            list_type_foods[rand_type_ondex_food].click()  # кликаме рандомный тип пищи

            time.sleep(2)
            # нажимаем на поле Название блюда
            WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Название блюда']")))[i*2].click()  # к пердудущему инедсу этого элемента+2
            time.sleep(2)
            listdishes_items = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
                (By.XPATH, "//mat-option[@class ='mat-option ng-star-inserted']")))  # спсик блюд
            rand_index_of_dishes = randint(0, len(listdishes_items) - 1)  # выбираем арнломное блюдо из спсика
            listdishes_items[rand_index_of_dishes].click()
            time.sleep(2)







        time.sleep(3)
        #ценообразовнаие рациона
        type_ration = WebDriverWait(driver, 10).until(
                        ec.presence_of_element_located((By.XPATH, "//mat-select[@placeholder='Тип рациона']")))

        driver.execute_script("arguments[0].scrollIntoView(true);", type_ration)  # скриллим к этому элемементу(который не виден) type_ration ПОМОГЛО!
        time.sleep(2)
        type_ration.click()

        # выбираем тп оплаты
        WebDriverWait(driver, 10).until(
                        ec.presence_of_all_elements_located((By.XPATH,"//mat-option[@class='mat-option mat-selected mat-active']")))[0].click()

        time.sleep(1)
        # цена раицона
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='price']"))).send_keys(str(randint(1, 4000)))

        time.sleep(2)
        # тогглер Скидка на пробный рацион
        toggle = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='mat-slide-toggle-thumb-container']")))

        driver.execute_script("arguments[0].scrollIntoView(true);", toggle)  # скриллим к этому элемементу(который не виден) calendar ПОМОГЛО!
        time.sleep(2)
        toggle.click()



        # цена за пробный рацион
        WebDriverWait(driver, 10).until(
             ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='trialPrice']"))).send_keys(str(randint(1, 2000)))

        time.sleep(4)


        # ситсема скидок:
        for i in range(0, 3): # сделаем три строки

            start_day = driver.find_elements_by_xpath("//mat-select[@placeholder='От (дней)']")[i]
            driver.execute_script("arguments[0].scrollIntoView(true);",
                                  start_day)  # скриллим к этому элемементу(который не виден) calendar ПОМОГЛО!

            start_day.click() # нажимаем От дней
            time.sleep(2)
            driver.find_elements_by_xpath("//mat-option[@class='mat-option ng-star-inserted']")[i+1].click()  # ыбмраем пункт из спсика  # колво дней = 2,3,4, .....,25
            time.sleep(2)
            driver.find_elements_by_xpath("//mat-select[@placeholder='До (дней)']")[i].click()  # выбираем До дней
            time.sleep(2)
            driver.find_elements_by_xpath("//mat-option[@class='mat-option ng-star-inserted']")[i+2].click()  # ыбмраем пункт из спсика
            time.sleep(2)
            driver.find_elements_by_xpath("//input[@placeholder='Цена (₽/день)']")[i+2].send_keys(str(randint(1,800))) # вбиваем цену

        #
        time.sleep(2)
        list_trashs = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn ls-trash-btn ng-star-inserted']"))) # список кнопок Корзина, чтобы сохрнаилось, надо послеюднюю пустую строку убирать

        list_trashs[len(list_trashs)-1].click() # кликаме посдленюю корзину

        time.sleep(4)

        button = driver.find_element_by_xpath(
            "//button[@class='mat-raised-button mat-primary ng-star-inserted']")  # кнпока Сохранить
        if button.is_enabled(): #  если true т/е/ если кнпока кликабельна
            time.sleep(2)
            button.click()
        else:

            print("save button is not clickable")
        time.sleep(20)





    def tear_down(self):
        time.sleep(10)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()



