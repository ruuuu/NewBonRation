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
from selenium.webdriver.common.action_chains import ActionChains # lля скроллнга к нужному элементу импортируем класс ActionChains


# import pytest

class Calculation(unittest.TestCase):


    def authorization(self, driver): # авторизация
        driver.get("https://devclient.bonration.ru/main") # меням на lifestyle

        button_voity = driver.find_element_by_xpath(
            "//button[@class='btn btn-border btn-border-black login-btn ripple']")  # у тега button  есть атрибут  class со значение btn btn-border btn-border-black login-btn
        button_voity.click()

        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='email']" )))# /html/body/app-root/app-modal/div/div[1]/div/app-login/div/div[2]/form/div[1]/input
            email_field.send_keys("rufinka_91@mail.ru")
        except TimeoutError:
            print("время ожидания поля емэйл вышло")

        try:
            password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']" )))
            password_field.send_keys("rufina")
        except TimeoutError:
            print("время ожидания поля пароль вышло")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-fill btn-fill-full needsclick ripple']")))
        button_voity.click()


    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_method_main(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось


        # переходим к элементу калькулятор, СКРОЛЛИМ
        actions = ActionChains(driver)  # создаем объект клааса ActionChains
        ration_card = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                      "//*[@id='calories-calc']")))
        actions.move_to_element(ration_card).perform() # переходим в к калькулятору

        # рассчет на  калькуляторе :
        time.sleep(3)
        try: # пол , изменила
            sex_field = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@class='ls-radio btn']" )))[0]
            sex_field.click()
        except TimeoutError:
            print("время ожидания вышло")

        # выберите  цель:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//*[@id='calories-calc']/div/app-ls-calc/form/div[2]/div[2]/app-select-drop-down/div/div/div[2]/button"))).click()

        target_field = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='select-item']")))[2]
        target_field.click()
        time.sleep(2)

        # выбираем из списка:
        select_item_target_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='calories-calc']/div/app-ls-calc/form/div[1]/div[2]/app-ls-radio-text/div/button[1]")))
        select_item_target_field.click()
        time.sleep(2)

        # рост изменила
        height_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                       "//*[@id='calories-calc']/div/app-ls-calc/form/div[3]/div[1]/div[2]/app-select-drop-down/div/div/div/button")))
        height_field.click()

        # из спсика выираем пункт
        select_item_height_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                                   "//*[@id='calories-calc']/div/app-ls-calc/form/div[3]/div[1]/div[2]/app-select-drop-down/div/div[2]/div[3]")))
        select_item_height_field.click()

        # возраст
        age_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                    "//*[@id='calories-calc']/div/app-ls-calc/form/div[3]/div[2]/div[2]/app-select-drop-down/div/div/div/button")))
        age_field.click()
        time.sleep(1)

        # из спсика выираем пункт
        select_item_age_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                                "//*[@id='calories-calc']/div/app-ls-calc/form/div[3]/div[2]/div[2]/app-select-drop-down/div/div[2]/div[8]")))
        select_item_age_field.click()
        time.sleep(2)

        # вес
        weight_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='calories-calc']/div/app-ls-calc/form/div[3]/div[3]/div[2]/app-select-drop-down/div/div/div/button")))
        weight_field.click()
        time.sleep(1)

        # выбор из списка:
        select_item_weight_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='calories-calc']/div/app-ls-calc/form/div[3]/div[3]/div[2]/app-select-drop-down/div/div[2]/div[3]")))
        select_item_weight_field.click()
        time.sleep(2)


        # уровень активности
        level_activity_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                               "//*[@id='calories-calc']/div/app-ls-calc/form/div[3]/div[4]/div[2]/app-select-drop-down/div/div/div[2]/button")))
        level_activity_field.click()
        time.sleep(1)

        select_item_level_activity_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                                           "//*[@id='calories-calc']/div/app-ls-calc/form/div[3]/div[4]/div[2]/app-select-drop-down/div/div[2]/div[4]")))
        select_item_level_activity_field.click()
        time.sleep(2)




        button_calculate = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='calories-calc']/div/app-ls-calc/form/div[5]/div/button")))
        if button_calculate.is_displayed():  # если элемент-кнопка видимый, то далбнейшие дествия те, что в скобках
            button_calculate.click()
        time.sleep(2)

        # кнопка "Найти компании":
        try:
            button_find_company = driver.find_elements_by_xpath("//button[@class='btn btn-fill ripple']")[1]
            if button_find_company.is_displayed():  # если элемент-кнопка видимый
                button_find_company.click()
            time.sleep(2)
        except:
            print("такого элемента нет")








    def tear_down(self):
        time.sleep(4) # чтобы сразу окно не закрыввалось
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



