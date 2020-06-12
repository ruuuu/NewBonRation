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
# заполнение формы клиента в его лк

class fill_out_anket(unittest.TestCase):

    def authorization(self, driver):

        driver.get("https://devclient.bonration.ru/main")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn btn-border btn-border-black login-btn ripple']"))) # у тега button  есть атрибут  class со значение btn btn-border btn-border-black login-btn
        button_voity.click()

        # заоплняем форму авторизации:
        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//input[@formcontrolname='email']")))
            email_field.send_keys("rufinka_91@mail.ru")
        except TimeoutError:
            print("время ожидания поля емэйл вышло")

        password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//input[@formcontrolname='password']")))
        if password_field.is_displayed(): # если поле вилимое то
            password_field.send_keys("7071991")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn btn-fill btn-fill-full needsclick ripple']")))

        if button_voity.is_displayed():  # если элемент видимый, то далбнейшие дествия те, что в скобках
            button_voity.click()


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
        self.driver = webdriver.Firefox() #.Chrome()
        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна

        #self.driver.maximize_window()
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



    def test_method_fill_out(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше

        time.sleep(5)  # чтобы увидеть

        # Нажимаем на лк:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn profile-btn']"))).click()
        time.sleep(3)

        # выбираем пнутк Настройки
        driver.find_elements_by_xpath("//div[@class='profile-drop-down-item']")[3].click()

        time.sleep(2)
        # поле Имя:
        field_name = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//*[@id='app-content']/app-profile/div/div/div[3]/div[2]/div/app-profile-settings/form/div[2]/input")))

        field_name.clear() # очищаем поле, перед тем как вбить дргое значение
        field_name.send_keys(self.my_metho_randem_stroka(randint(5, 10), randint(1,3)))


        # # поле Телефон:
        # field_phone = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        #     (By.XPATH,"//*[@id='app-content']/app-profile/div/div/div[3]/div[2]/div/app-profile-settings/form/div[3]/input")))

        # field_phone.clear()# очищаем поле, перед тем как вбить дргое значение
        # field_phone.send_keys("89765432789")

        time.sleep(2)
        # поле Адрас доставки:
        field_address = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//*[@id='app-content']/app-profile/div/div/div[3]/div[2]/div/app-profile-settings/form/div[4]/input")))

        field_address.clear()
        field_address.send_keys(self.my_metho_randem_stroka(randint(5, 10), randint(1,3)))

        time.sleep(2)
        # поле Дом:
        field_home = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//*[@id='app-content']/app-profile/div/div/div[3]/div[2]/div/app-profile-settings/form/div[5]/div[1]/input")))

        field_home.clear()# очищаем поле, перед тем как вбить дргое значение
        field_home.send_keys(str(randint(10, 99)))

        time.sleep(2)
        # поле подъезд:
        field_podezd = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH,"//*[@id='app-content']/app-profile/div/div/div[3]/div[2]/div/app-profile-settings/form/div[5]/div[2]/input")))

        field_podezd.clear()# очищаем поле, перед тем как вбить дргое значение
        field_podezd.send_keys(str(randint(1, 10)))

        time.sleep(2)
        # поле этаж:
        field_floor = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH,"//*[@id='app-content']/app-profile/div/div/div[3]/div[2]/div/app-profile-settings/form/div[5]/div[3]/input")))

        #if (name_dish_filed.get_attribute('value') != ''):
        #
        #     name_dish_filed.clear() # очищае поле если оно не пустое

        time.sleep(2)
        field_floor.clear()
        field_floor.send_keys(str(randint(10, 99)))
        time.sleep(2)

        # поле Квартира:
        field_code_on_door = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH,"//*[@id='app-content']/app-profile/div/div/div[3]/div[2]/div/app-profile-settings/form/div[5]/div[4]/input")))

        field_code_on_door.clear()# очищаем поле, перед тем как вбить дргое значение
        field_code_on_door.send_keys(str(randint(10, 1000)))
        time.sleep(2)

        #тоггрел переключаем
        for i in range(0,2):
           WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
              (By.XPATH, "//button[@class='toggler-label']")))[1].click()



        time.sleep(2)
        for i in range(0, 2):
            WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
                (By.XPATH, "//button[@class='toggler-label']")))[0].click()


        time.sleep(2)
        # кнопка Сохранить:
        save_button = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH,"//*[@id='app-content']/app-profile/div/div/div[3]/div[2]/div/app-profile-settings/form/div[6]/div[1]/button[2]")))

        if save_button.is_displayed():
            save_button.click()

        time.sleep(6)


    def tear_down(self):
        time.sleep(4)
        self.driver.quit()
        # pass
        time.sleep(4)

if __name__ == "__main__":
    unittest.main()



