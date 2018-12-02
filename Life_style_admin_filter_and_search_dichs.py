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

#import pytest

# ильтрация оп названи, еалорийносии, весу и поиск

class Admin_filters_dishes(unittest.TestCase):

# фильтрация   раздела  все блюда фильтраия  и поиск


    def authorization(self, driver): # авторизация

        driver.get("https://devadmin.bonration.ru/external/login")


        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-0']" )))#
            email_field.send_keys("wyvzmp5iy5oh@mail.ru")
        except TimeoutError:
            print("время ожидания поля емэйл вышло")

        try:
            password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-1']" )))
            password_field.send_keys("qwerty")
        except TimeoutError:
            print("время ожидания поля пароль вышло")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                       "/html/body/app-root/portal-login/div/mat-card/mat-card-content[2]/div/div/div/app-spinner-button/button")))
        if button_voity.is_displayed():  # если кнпока видна , то
            button_voity.click()
        time.sleep(3)


    def search_diches(self, driver):

        search_filed = WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, ""
                                                                              "//input[@type='search']")))
        search_filed.send_keys("блюдо3") # поиск по названию
        time.sleep(3)
        search_filed.clear()# очищвем поле
        time.sleep(2)

        search_filed.send_keys("4567")# поиск по калоринйти
        time.sleep(3)
        search_filed.clear()  # очищвем поле
        time.sleep(2)

        search_filed.send_keys("90")  # поиск по весу
        time.sleep(3)
        search_filed.clear()  # очищвем поле
        time.sleep(2)



    def setUp(self):

        self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_filter_dishes(self):  # главный метод, надо чтобы он начинался  с test_
        try:
            driver = self.driver
            time.sleep(3)
            self.authorization(driver)  # вызов метода,котрый выше
            time.sleep(4)  # чтобы сразу окно не закрывалось

            # раздел Все блюда:
            WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,""
                                                                                     "//a[@href='/main/dishes']"))).click()

            # # Новые
            # new = driver.find_elements_by_xpath("//div[@class='mat-tab-label mat-ripple ng-star-inserted']")[0]
            # time.sleep(10)
            # if new.is_displayed():
            #
            #     new.click()
            # else:
            #     time.sleep(7)
            #     new.click()
            # time.sleep(3)

            # фИЛЬТР по навзанию блюда
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//button[@aria-label='Change sorting for name']"))).click()
            time.sleep(2)

            # фИЛЬТР по калорийности блюда
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Change sorting for calories']"))).click()
            time.sleep(2)

            # фИЛЬТР по весу блюда
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@aria-label='Change sorting for weight']"))).click()
            time.sleep(2)

            self.search_diches(driver) # вызов метода поиска

        except:
            print("ошибка")



    def tear_down(self):
        time.sleep(5)# чтобы окно сразу не закрывалось
        self.driver.close()



if __name__ == "__main__":
    unittest.main()



