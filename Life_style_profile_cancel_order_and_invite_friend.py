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
from selenium.webdriver.common.action_chains import ActionChains  # lля сколддинга к нужному элементу импортируем класс ActionChains


# import pytest
# здесь  посик компании, закзза  выбранного рациона

class Cancel_order_and_Invite_friend(unittest.TestCase):

    def authorization(self, driver):  # авторизация

        driver.get("https://devclient.bonration.ru/main")  # меням на lifestyle

        button_voity = driver.find_element_by_xpath(
            "//button[@class='btn btn-border btn-border-black login-btn ripple']")  # у тега button  есть атрибут  class со значение btn btn-border btn-border-black login-btn
        button_voity.click()

        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                                          "//input[@formcontrolname='email']")))  # /html/body/app-root/app-modal/div/div[1]/div/app-login/div/div[2]/form/div[1]/input
            email_field.send_keys("rufinka_91@mail.ru")
        except TimeoutError:
            print("время ожидания поля емэйл вышло")

        try:
            password_field = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']")))
            password_field.send_keys("rufina")
        except TimeoutError:
            print("время ожидания поля пароль вышло")

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//button[@class='btn btn-fill btn-fill-full needsclick ripple']")))
        button_voity.click()
        time.sleep(3)

    def invite_friend(self, driver):


        # раздел Пригласить друга
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//a[@class='link link-inline-block btn profile-controls-item ripple']"))).click()

        time.sleep(3)

        # поле Email
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(
            (By.XPATH, "//input[@formcontrolname='email']"))).send_keys("nbvcqz@mail.ru")

        time.sleep(2)

        # кнопка Пригласить
        invite_button = driver.find_element_by_xpath("//button[@class='btn btn-fill btn-fill-full ripple']")

        if invite_button.is_displayed(): #  если кнопка ]активная то нажимаем на нее
            invite_button.click()


        time.sleep(3)



    def setUp(self):

        self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()

    def test_method_cancel_order_invite_friend(self):  # главный метод, надо чтобы он начинался  с test_


        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(3)  # чтобы сразу окно не закрывалось

        try:
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH,"//button[@class='btn profile-btn']"))).click() # кнпока Личный кбинет

            time.sleep(2)

            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//div[@class='profile-drop-down-item']")))[0].click()# Раздел Заказы

            time.sleep(2)

            card_order = WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//div[@class='profile-order-card-wrapper']")))[2] # каточка заказа

            actions = ActionChains(driver)
            actions.move_to_element(card_order).perform()  # переходим к этому эулменту
            time.sleep(3)
            card_order.click()

            #кнопка Отмена в заказе , котрый неоплачен
            WebDriverWait(driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn btn-flat-red btn-flat-red-upper ripple']")))[2].click()

            time.sleep(4)

            # в попапе выбираем причину отмены:
            WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located(
                (By.XPATH, "//label[@class='ls-input-radio-wrapper']")))[3].click()
            time.sleep(2)

            #нажимаем кнопку "отмнеить" в ппопапе
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                (By.XPATH, "//button[@class='btn btn-fill btn-fill-full ripple']"))).click()




            time.sleep(3)
            # переходим в раздел Историзя заказов
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, "#app-content > app-profile > div > div > div.profile-content-wrapper > div.profile-col-2 > div > app-profile-orders > div > div.profile-orders-header > div > app-ls-radio-text > div > button:nth-child(2) > div"))).click()


            time.sleep(6)
            self.invite_friend(driver) # вызов метода приглашения друга

            time.sleep(3)

        except:
            print("где-то ошибка")



    def tear_down(self):
        time.sleep(2)
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



