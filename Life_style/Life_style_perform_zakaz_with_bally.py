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
from selenium.webdriver.common.action_chains import \
    ActionChains  # lля сколддинга к нужному элементу импортируем класс ActionChains

from random import randint


# import pytest
# здесь  посик компании, закзза  выбранного рациона

class Order_ration_with_bally(unittest.TestCase):

    def authorization(self, driver):  # авторизация

        driver.get("https://devclient.bonration.ru/main")  # меням на lifestyle

        button_voity = driver.find_element_by_xpath(
            "//button[@class='btn btn-border btn-border-black login-btn ripple']")  # у тега button  есть атрибут  class со значение btn btn-border btn-border-black login-btn
        button_voity.click()

        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                          "//input[@type='email']")))  # /html/body/app-root/app-modal/div/div[1]/div/app-login/div/div[2]/form/div[1]/input
            email_field.send_keys("rufinka_91@mail.ru")
        except:
            print("email_field is not clickable")

        try:
            password_field = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']")))
            password_field.send_keys("7071991")
        except:
            print("password_field is not clickable")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn btn-fill btn-fill-full needsclick ripple']")))
        button_voity.click()
        time.sleep(3)

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

    def my_metho_randem_stroka(self, kolvo_bukv_v_slove, count_slov):  # генерит предложение

        list_slov = []
        # kolvo_bukv_v_slove = randint(3,5) # генерим ково букв в i-ом  слове

        for i in range(count_slov):  # цикл по колву слов, будет 5 слов  строке

            list_bukv = []
            for j in range(kolvo_bukv_v_slove):  # цикл по бкувам в i-ом слове

                list_bukv.append(' '.join([self.list_characters[randint(0, len(self.list_characters) - 1)]]))

            list_slov.append(''.join(list_bukv))

        return str(' '.join(list_slov))


    def setUp(self):

        self.driver = webdriver.Chrome()

        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна

        # self.driver.maximize_window()
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

    def test_method_main_order_ration(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(1)  # чтобы сразу окно не закрывалось

        try:  # На главной странице Кнопкк "наути рацион"
            find_button = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//a[@href='/search']")))
            find_button.click()
        except:
            print("find_button is not founded or not clcikable")

        time.sleep(1)
        #  На станцие всех компаний :
        try:  # поле "Поиск":
            find_field = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//input[@name='search']")))
            find_field.send_keys("Company Life")
            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn search-company-list-item']")))[
                0].click()
            time.sleep(2)
        except:
            print("find_field  is not founded")

        time.sleep(2)

        # переходит к определенной карте рациона
        ration_cards = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='ration-card-wrapper']")))

        print("count of ration_cards", len(ration_cards))
        rand_index_for_ration = randint(0, len(ration_cards) - 1)

        #print("randonm index of ration equal", rand_index_for_ration)

        time.sleep(2)

        # # Добавила:
        # rand_index_for_ration = 32 # Тест !!!!!!!

        driver.execute_script("arguments[0].scrollIntoView(true);", ration_cards[rand_index_for_ration])  # скриллим к этому элемементу ration_cards[rand_index_for_ration]
        time.sleep(3)


        ration_cards[rand_index_for_ration].click()  # нажимаем на рандомную  карту рациона

        time.sleep(3)

        # на станице заказк кнопка Перейти к  меню рациона
        try:
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-flat btn-flat-upper']"))).click()
        except:
            print("knopki Pereyti k menu rationa net")



        try:  # если пробные раицоны есть, то выберет их, ели нет то просто распечатате что их нет
            # спсиок пробных рационов:
            trial_rations = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//div[@class='ration-discount-card-wrapper']")))

            print("count of trial rations equal", len(trial_rations))
            random_idex_of_trial_ration = randint(0, len(trial_rations) - 1)  # выбиратет рандомный индекс пробного рациона
            trial_rations[random_idex_of_trial_ration].click()




        except:

            print("trial ration  is not exist")
            # кнопка "Заказать": на странице рациона
            zakazat_button = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-fill ripple']")))
            driver.execute_script("arguments[0].scrollIntoView(true);",zakazat_button)  # скриллим к этому элемементу(который не виден) calendar ПОМОГЛО!!и элемент этот подтянется к верху станицы
            time.sleep(2)
            zakazat_button.click()

            # форма заполнения
            # нажимаем на выпадюащий список
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn ls-drop-down-btn select-drop-down-btn drop-down-default']"))).click()

            time.sleep(2)

            items = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='select-item']")))  # список пунктов в выпадающем спсике
            items[2].click() # добавить рандомнфй индекс itema!!!!!!!!!
            try:

                print("proveryem est li ssobchenir nedostatocho ballov")
                if WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='error-message error-message-active']"))).is_displayed(): # сообщение недостаочное колво баллов
                    print("element_error.is_displayed()", WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='error-message error-message-active']"))).is_displayed())
                    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn ls-drop-down-btn select-drop-down-btn']"))).click() # нажимаме на выпадающий список

                    time.sleep(4)
                    print("clickaem drugoe")
                    print("clickaem len(items) - 1", len(items) - 1)
                    items1 = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
                        (By.XPATH, "//div[@class='select-item']")))  # список пунктов в выпадающем спсике
                    items1[len(items1) - 1].click() # кликме Другое

                    time.sleep(4)
                    button_minus = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn ls-calc-btn ls-calc-minus']")))
                    while button_minus.is_enabled(): # нажимаем на кнпоку минус пока кнопка минус незадизейблеан(то есть активна)
                        button_minus.click()



            except:

                #
                # items = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='select-item']")))  # список пунктов в выпадающем спсике
                #
                # print("count of items equal", len(items))
                #
                # ranitem = randint(0, len(items) - 2)
                #
                # print("random item equl", ranitem)
                #
                # if ranitem == (len(items) - 1):  # если выбрали Другое то
                #     items[ranitem].click()
                #
                #     for j in range(0, 2):
                #         WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn ls-calc-btn ls-calc-minus']"))).click()
                # else:
                #     items[ranitem].click()  # кликаме выбранный item из спсика
                print("count of balls is enough")









        # Форма доставки:
        # Дата:
        day = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@id='date-input-2']")))  # наимаем на поле калндарь
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              day)  # скриллим к этому элемементу(который не виден) day ПОМОГЛО!!и элемент этот подтянется к верху станицы
        time.sleep(2)
        day.click()

        time.sleep(2)  # ждем пока календарь появится
        for i in range(0, 4):
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//div[@class='qs-arrow qs-right']"))).click()  # нажатие на струлку вправо (след месц)
            time.sleep(1)

        for i in range(0, 3):
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//div[@class='qs-arrow qs-left']"))).click()  # нажатие на струлку влево (пред месц)
            time.sleep(1)

        time.sleep(1)

        #  список дат:
        list_days = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='qs-num']")))

        random_index_date = randint(0, len(list_days) - 1)
        print("random_index_date is equal", random_index_date)

        list_days[random_index_date].click()  # кликаем рандомную дату

        # время доставки:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//input[@formcontrolname='time']"))).click()  # нажима на поле Врем доставки
        time.sleep(2)

        # из выпадающего спсика выбираем item
        list_items_time = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='select-item']")))
        print("count of items equal", len(list_items_time))

        random_index_of_item = randint(0, len(list_items_time) - 1)  # выбираем ранломный индекс item
        print("random_index_of_item is equal", random_index_of_item)

        list_items_time[random_index_of_item].click()  # нажимае мна рандомны йииндекс

        time.sleep(2)

        # Адрес доставки:
        address = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='address']")))
        address.clear()  # очищает поле
        time.sleep(1)
        address.send_keys(self.my_metho_randem_stroka(randint(6, 9), randint(3, 5)))

        time.sleep(2)
        house = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='house']")))
        house.clear()
        time.sleep(1)
        house.send_keys(str(randint(1, 9000)))

        time.sleep(2)
        entrence = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='entrance']")))
        entrence.clear()
        time.sleep(1)
        entrence.send_keys(str(randint(1, 50)))

        time.sleep(2)
        flooor = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='floor']")))
        flooor.clear()
        time.sleep(1)
        flooor.send_keys(str(randint(1, 100)))

        time.sleep(2)
        flat = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='flatNumber']")))
        flat.clear()
        time.sleep(1)
        flat.send_keys(str(randint(1, 2000)))
        time.sleep(1)

        # пожелание  к заказу
        i = 0
        while i < 140:
            index_character = randint(0, len(
                self.list_characters) - 1)  # берет рандомный икднек сбуквы из спсика всех букв
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname='comment']"))).send_keys(
                str(self.list_characters[index_character]))  # self.my_metho_randem_stroka(randint(5,8), randint(3,4))
            i += 1



        time.sleep(2)

        texsts = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='radio-card-description']")))  # список текстов на кнпоках способов оплаты

        elem_payments = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn radio-wrapper']")))



        if texsts[0].text == "Оплата баллами": #
            print("texsts.text  == 'Оплата баллами' is", texsts[0].text == "Оплата баллами")

            # кнопка Офрмить заказ
            WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-fill ordering-footer-btn ripple']"))).click()

        else: # если небальные способы оплаты
            # способ оплаты:elem_payments[rand_index_of_payment].click()
            rand_index_of_payment = randint(0, len(elem_payments) - 1)  # берет рандомный индекс способа оплаты
            print("random index of payment equal", rand_index_of_payment)

            time.sleep(3)
            if texsts[0].text == 'Visa, Master Card, МИР': # если онлайн оплата
                elem_payments[rand_index_of_payment].click()# нажимаем кнпоку Оофртмить заказк

                time.sleep(6)
                WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@name='pan']"))).send_keys("4111 1111 1111 1111")
                time.sleep(1)
                WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@name='cardholder']"))).send_keys("jdfhgljsh sgljsdhgds")
                time.sleep(1)
                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located((By.XPATH, "//input[@name='expired']"))).send_keys("12/19")
                time.sleep(1)
                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located((By.XPATH, "//input[@name='cvc']"))).send_keys("123")
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
                WebDriverWait(driver, 10).until(
                    ec.presence_of_element_located((By.XPATH, "//input[@value='Submit']"))).click()
                time.sleep(2)

            else:
                elem_payments[rand_index_of_payment].click()

                # кнопка Офрмить заказ
                WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-fill ordering-footer-btn ripple']"))).click()






        time.sleep(3)
        # "Продолжить" в попапе подтвержденяи оплаты
        WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-fill btn-fill-full ripple']"))).click()

        time.sleep(3)
        # на станице раицона, жмем Личный кабинет вверху:
        WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//button[@class='btn profile-btn']"))).click()

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='profile-drop-down-item']")))[0].click()

        time.sleep(3)

    def tear_down(self):
        time.sleep(3)
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



