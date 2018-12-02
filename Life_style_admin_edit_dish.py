import time
import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import Select  # работа со списками
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains # lля сколддинга к нужному элементу импортируем класс ActionChains

#from for_export_authorization import export_Admin_authorization # из файла for_export_authorization.py импортируиеи класс export_Admin_authorization


# import pytest
 # здесь  редактирование блюда

class Admin_edit_dishs(unittest.TestCase):

    def authorization(self, driver):  # авторизация
        driver.get("https://devadmin.bonration.ru/external/login")  # меням на lifestyle

        try:
            email_field = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-0']")))  #
            email_field.send_keys("rmstou6psmxz@mail.ru")
        except TimeoutError:
            print("время ожидания поля емэйл вышло")

        try:
            password_field = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-1']")))
            password_field.send_keys("qwerty")
        except TimeoutError:
            print("время ожидания поля пароль вышло")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                       "/html/body/app-root/portal-login/div/mat-card/mat-card-content[2]/div/div/div/app-spinner-button/button")))
        if button_voity.is_displayed():  # если кнпока видима, то
            button_voity.click()

    def setUp(self):

        self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_method_admin_edit_dish(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше

        time.sleep(4)  # чтобы сразу окно не закрывалось

        # выбираем пункт "все блюда":
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,  "/html/body/app-root/portal-layout-classic/mat-sidenav-container/mat-sidenav[1]/portal-menu-sidenav/div/div/mat-nav-list/a[4]/div/div[2]/h3"))).click()

        # # выбираем блюдо для редактирования сафачо
        # WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/portal-layout-classic/mat-sidenav-container/mat-sidenav-content/div/div/div/app-dishes/div/div/mat-table/mat-row[2]/mat-cell[1]"))).click()
        #
        # time.sleep(2)
        # name_dish = driver.find_element_by_xpath("//input[@placeholder='Название блюда']")
        #
        # name_dish.clear()
        #
        # name_dish.send_keys("другое блюдо")
        #
        # time.sleep(1)
        # sostav_dish = driver.find_element_by_xpath("//input[@placeholder='Состав']")
        #
        # sostav_dish.clear()# очищаем поле
        #
        # sostav_dish.send_keys("сахар1, олр лдр лрдр ордр масло2")
        #
        # time.sleep(3)
        # count_calory = driver.find_element_by_xpath("//input[@placeholder='Количество калорий (кк)']")
        #
        # count_calory.clear()# очищаем поле
        #
        # count_calory.send_keys("68")
        #
        # time.sleep(1)
        # count_weight = driver.find_element_by_xpath("//input[@placeholder='Вес (г)']")
        #
        # count_weight.clear() # очищаем поле
        #
        # count_weight.send_keys("29")
        #
        # time.sleep(1)
        # driver.find_element_by_xpath("//div[@type='button']").click() # кнопка "удалить фото"
        # driver.find_element_by_xpath("//input[@type='file']").send_keys(
        #     "/Users/rufina/Desktop/dishs/dinner.jpg")
        #
        # time.sleep(3)
        # # # кнопка Отмена:
        # # try:
        # #     cancel_button = driver.find_element_by_xpath("//button[@class='mat-button mat-primary']")
        # #     if cancel_button.is_displayed():
        # #         cancel_button.click()
        # # except ElementNotVisibleException:
        # #     print('нет кнопки Отмена')
        # #
        # # driver.find_element_by_xpath("//app-spinner-button[@class='ng-star-inserted']").click() # нажимаем отмнеить
        #
        # # кнопка "Сохранить":
        # save_button = driver.find_element_by_xpath("//*[@id='mat-dialog-0']/app-create-dish/div[3]/div[2]/app-spinner-button/button")
        # if save_button.is_displayed(): # если кнпока видима
        #     save_button.click()
        #
        # time.sleep(5)



        # выбираем блюдо для редактирования
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//mat-row[@class='dishes-table-row mat-row ng-star-inserted']")))[2].click()

        time.sleep(3)
        name_ration = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Название блюда']")))
        time.sleep(2)
        name_ration.clear()# очищаем поле
        time.sleep(2)
        name_ration.send_keys("другое название рациона")
        time.sleep(4)

        # нажимаем кнпоку Удалить:
        try:
            if driver.find_element_by_xpath("//button[@type='submit']").is_displayed():
                time.sleep(4)
                driver.find_element_by_xpath("//button[@type='submit']").click()
        except ElementNotVisibleException:
            print('нет кнопки УДАЛИТЬ')



    def tear_down(self):
        time.sleep(8)
        #self.driver.close()
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



