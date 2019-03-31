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

from random import randint


# import pytest
#

class Admin_edit_order(unittest.TestCase):


    def generating_timesss(self):  # гененрирует время

        x_hours = randint(8, 19)
        x_minutes = randint(0, 60)
        y_hours = randint(9, 20)
        y_minutes = randint(0, 60)
        # print("%H:%M-%H:%M", x_hours, x_minutes, y_hours, y_minutes)

        if x_hours < y_hours:
            return '{0}:{1}-{2}:{3}'.format(x_hours, x_minutes, y_hours, y_hours)
        else:
            return '{0}:{1}-{2}:{3}'.format(y_hours, x_minutes, x_hours, y_hours)


    def my_metho_randem_stroka(self, kolvo_bukv_v_slove, count_slov): # генерит предложение

        list_slov = []
        # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

        for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

            list_bukv = []
            for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                list_bukv.append(' '.join([self.list_characters[randint(0, len(self.list_characters) - 1)]]))

            list_slov.append(''.join(list_bukv))

        return str(' '.join(list_slov))



    def authorization(self, driver):



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



    def setUp(self):
        #
        self.driver = webdriver.Chrome()

        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна#self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()
        self.list_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                'R',
                                'S', 'T', 'U', 'W', 'X', 'Y', 'Z',
                                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'k', 'm', 'n', 'o', 'p', 'q',
                                'r',
                                's', 't', 'u', 'w', 'x', 'y', 'z',
                                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '&', '#', '*', '(', ')', '"', ',',
                                '/',
                                ']', '[', '}', '{', '"', '?', '!', '§', '±', '<', '№']

    def test_method_edit_order(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше

        time.sleep(5)  # чтобы увидеть

        # перееходим в раздел заказы:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//h3[@class='mat-line']"))).click()

        time.sleep(7)

        # список заказков:
        list_orders = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
            (By.XPATH,"//a[@class='ls-table-row-link ng-star-inserted']")))
        rand_index_order = randint(0, len(list_orders)-1)

        print("rand_index_order equal", rand_index_order)

        list_orders[rand_index_order].click()# выбираем рандомнй заказ

        time.sleep(2)

        # редактируем дату начала рациона, жмем на иконку каранддаша

        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH,"//button[@class='mat-icon-button mat-accent ng-star-inserted']"))).click()

        time.sleep(2)
        #  впоапе редактирвоания :
        try: # попытаемся оердактировать дату и рвемя

            # нажимаем на каледнарь
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//button[@aria-label='Open calendar']"))).click()
            time.sleep(2)

            # жмем в календаре на правый треугольничек, следующий месяц
            for i in range(0, 5):
                WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                    (By.XPATH, "//button[@aria-label='Next month']"))).click()

            time.sleep(2)
            list_dates = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
                (By.XPATH, "//td[@class='mat-calendar-body-cell ng-star-inserted']")))

            rand_index_od_date = randint(0, len(list_dates)-1)
            list_dates[rand_index_od_date].click()
            time.sleep(2)

            field_time = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//input[@formcontrolname='time']")))

            field_time.clear()
            time.sleep(1)
            field_time.send_keys(self.generating_timesss()) # всnавляем время
            time.sleep(2)

            # жмем кнопку Сохранить
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//button[@class='mat-raised-button mat-primary ng-star-inserted']"))).click()
            time.sleep(2)



        except:
            pass




        try: # попытаемся поменять статус оплаты, ели уде Оплачено, то идем дальше
            # менем статутс оплаты, перключем тоглер
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH,"//div[@class='mat-slide-toggle-thumb-container']"))).click()
            time.sleep(2)

            # в  поппапе подтверждения жмем ок
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//button[@class='mat-raised-button mat-primary ng-star-inserted']"))).click()
        except:
            pass

        time.sleep(2)


        # статус заказа меняем (НОВЫЙ ПРИНЯТ ВЫПОЛНЯЕТСЯ ВЫПОЛНЕН)
        # жем на маленький теругоьничек
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//mat-select[@placeholder='Статус']"))).click()

        time.sleep(2)
        # список статутсов [НОВЫЙ ПРИНЯТ ВЫПОЛНЯЕТСЯ ВЫПОЛНЕН]
        list_status_items = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))

        rand_index_status = randint(0, len(list_status_items)-1)# берем рандомный статус заказа
        list_status_items[rand_index_status].click()

        time.sleep(2)

        # нажимаме в поапе потвержедня на крестик
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn ls-close-btn']"))).click()
        time.sleep(2)

        # еще раз нажимаме на маленький треугольничек
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//mat-select[@placeholder='Статус']"))).click()
        time.sleep(2)
        # список статутсов [НОВЫЙ ПРИНЯТ ВЫПОЛНЯЕТСЯ ВЫПОЛНЕН]
        list_status_items_1 = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))

        rand_index_status_1 = randint(0, len(list_status_items_1) - 1)  # берем рандомный статус заказа
        list_status_items_1[rand_index_status_1].click()

        time.sleep(2)
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//button[@class='mat-raised-button mat-primary ng-star-inserted']"))).click()  # кликаме кнопку OK

        if rand_index_status_1 == (len(list_status_items_1) - 1): # есои нажли на Отменен
            # в попапе указываем причину отмены:
            # список радиокнопок отмены
            list_radios_cancel = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//input[@type='radio']")))

            rand_index_radioo_cancel = randint(0, len(list_radios_cancel)-1)
            print("rand_index_radioo_cancelequal", rand_index_radioo_cancel)
            list_radios_cancel[rand_index_radioo_cancel].click()

            if (rand_index_radioo_cancel == (len(list_radios_cancel)-1)):# есои выбрали Дугое в попапе отмены закакза
                # пишем текст
                WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Напишите причину']"))).send_keys("ljhlkzmz,dfughl")

            time.sleep(2)
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='mat-raised-button mat-primary ng-star-inserted']"))).click() # кликаме кнопку OK


        time.sleep(2)



        try: # попоытаемся еще раз имзенить статeс зазкак, есkи он не кликабелн то ничего не будет делать
            # снова жмем на маленлький трегугольничек в смене статуса заказа
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//mat-select[@placeholder='Статус']"))).click()

            time.sleep(1)
            # список статутсов
            list_1 = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))



            time.sleep(1)

            rand_index_status = randint(1, len(list_1) - 1)  # берем рандомный статус заказа
            list_1[rand_index_status].click()

        except:
            pass
            #print("status order is  vupolnen")

        time.sleep(2)
        list_arrows = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH,  "//div[@class='mat-select-arrow']"))) # в доставках у статуосв список треугольничков

        print("count of list_errows of deliveries equal", len(list_arrows))
        rand_index_od_arrow = randint(1, len(list_arrows)-1)

        time.sleep(3)
        list_arrows[rand_index_od_arrow].click() #  кликаме на рандомный треугольничек у доставок
        print("rand_index_od_arrow equal", rand_index_od_arrow)
        time.sleep(1)

        lest_statuses_deleiveries = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-option[@role='option']"))) # список статутсов доставок Доставлено/Не доставлено

        index_staus_delivery = randint(0, 1)# выбиарем раномный статутс доставки

        if index_staus_delivery == 0:# еси выбрали Доставлено

            lest_statuses_deleiveries[index_staus_delivery].click() # кликаме статус

            # поапе подтверждения доставки
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='mat-raised-button mat-primary ng-star-inserted']"))).click() # нажимаем кнпоку ОК


        if index_staus_delivery == 1:  # если выбрали Недоставлено

            lest_statuses_deleiveries[index_staus_delivery].click()  # кликаме статус
          # поапе список причин выбора недоставки
            list_cancel_deliveeries = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH,"//mat-radio-button[@class='cancel-delivery-cause mat-radio-button mat-primary ng-star-inserted']")))

            rand_index_cancel = randint(0, len(list_cancel_deliveeries)-1)
            list_cancel_deliveeries[rand_index_cancel].click() #  кликаем радиокнопку
            time.sleep(2)
            if rand_index_cancel == len(list_cancel_deliveeries) - 1:  # ксли выбрали Другое
                # пищем текст причины отмны
                WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//textarea[id='cancel-comment']"))).send_keys(self.my_metho_randem_stroka(randint(5,8), randint(4,8),2))
            # кнопка Ок
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='mat-raised-button mat-primary ng-star-inserted']"))).click() # кнопка Ок
























        time.sleep(4)

    def tear_down(self):
        time.sleep(4)
        self.driver.close()
        self.driver.quit() # закрывает барузер
        # pass
        time.sleep(4)


if __name__ == "__main__":
    unittest.main()



