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


# import pytest

class Registartion(unittest.TestCase):

    def registration(self, driver):
        driver.get("https://devclient.bonration.ru/main")  # меням на lifestyle


        try:
            button_voity = driver.find_element_by_xpath(
                "//button[@class='btn btn-border btn-border-black login-btn']")  # у тега button  есть атрибут  class со значение btn btn-border btn-border-black login-btn
            if button_voity.is_displayed(): # елси кнопка активна, то дальнейшие ейсвтия в скобках
                button_voity.click()

        except TimeoutError:
            print("время вышло")


        # ссылка Регитсрация:
        registaration_link = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "/html/body/app-root/app-modal/div/div[1]/div/app-login/div/div[2]/div[2]/a")))
        registaration_link.click()

        #
        name_filed = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "/html/body/app-root/app-modal/div/div[1]/div/app-registration/div/form/div[1]/div[2]/input")))
        name_filed.send_keys("Ollllga")

        email_filed = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "/html/body/app-root/app-modal/div/div[1]/div/app-registration/div/form/div[1]/div[3]/input")))
        email_filed.send_keys("etkjh@yandex.ru")

        phone_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "/html/body/app-root/app-modal/div/div[1]/div/app-registration/div/form/div[1]/div[4]/input")))
        phone_field.send_keys("89655906543")

        password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "/html/body/app-root/app-modal/div/div[1]/div/app-registration/div/form/div[1]/div[5]/input")))
        password_field.send_keys("7290")

        check_box_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "/html/body/app-root/app-modal/div/div[1]/div/app-registration/div/form/div[2]/div/label/div")))
        check_box_field.click()


        button_registration = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "/html/body/app-root/app-modal/div/div[1]/div/app-registration/div/form/div[1]/button")))

        if button_registration.is_displayed():  # если элемент-кнопка видимый, то далбнейшие дествия те, что в скобках
            button_registration.click()

       
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()

    def test_method_main(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.registration(driver)  # вызов метода,котрый выше

        time.sleep(5)  # чтобы сразу окно не закрывалось

    def tear_down(self):
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



