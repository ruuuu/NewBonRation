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

# import pytest


class Profile_send_review(unittest.TestCase):

# оставляем отзыв о сделанном заказе и редактируем его


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
        time.sleep(3)



    def edit_review(self,driver):

        time.sleep(3)
        actions = ActionChains(driver)
        element_review = WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
                (By.XPATH,"//div[@class='profile-review-card-wrapper']")))[3]

        actions.move_to_element(element_review).perform()  # переходим к этому эулменту
        time.sleep(3)

        # кнпока Редактирвания:
        WebDriverWait(driver, 20).until(ec.presence_of_element_located(
                (By.XPATH,"//*[@id='app-content']/app-profile/div/div/div[3]/div[2]/div/app-profile-reviews/div[33]/app-profile-review-card/div/div[1]/div[2]/div[1]/div[2]/button[1]"))).click()

        time.sleep(3)
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,"//textarea[@formcontrolname='message']"))).send_keys("отредактиваонно сообщение")
        time.sleep(2)
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,"//button[@class='btn btn-fill btn-fill-full ripple']"))).click()


    def setUp(self):

        self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_profile_send_review(self):  # главный метод, надо чтобы он начинался  с test_
        try:
            driver = self.driver
            self.authorization(driver)  # вызов метода,котрый выше
            time.sleep(3)  # чтобы сразу окно не закрывалось

            # кнопка Личный кабмнет:
            WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,
                                                                                     "//button[@class='btn profile-btn']"))).click()


            WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='profile-drop-down-item']")))[1].click() # item Мои отзывы
            time.sleep(2)



            # кнопка оставить отзыв
            WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
                (By.XPATH,"//button[@class='profile-review-card-header-bottom-review-btn btn btn-flat btn-flat-upper ripple']")))[2].click()
            time.sleep(2)

            #В попапе нажимаем кнпоку звездочка
            WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
                (By.XPATH,"//button[@class='btn set-rating-btn']")))[2].click()

            time.sleep(2)
            # оставялем сам тест отзыва
            WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,"//textarea[@placeholder='Напишите несколько строк']"))).send_keys(",fgnm.dfm fdgldfkjg;ld sdgsjdlkg gdkaslgjd")

            time.sleep(2)
            # кнопка Сохранить
            WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH,"/html/body/app-root/app-modal/div[1]/div/div/app-modal-leave-feedback/div/div[2]/form/button"))).click()
            time.sleep(6)

            self.edit_review(driver) # метод редактирования отзыва

            time.sleep(7)


        except TimeoutError:
            print("тест упал")


    def tear_down(self):
        time.sleep(5)# чтобы окно сразу не закрывалось
        self.driver.close()



if __name__ == "__main__":
    unittest.main()



