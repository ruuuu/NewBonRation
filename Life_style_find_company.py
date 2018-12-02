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
from selenium.webdriver.common.action_chains import ActionChains # lля сколддинга к нужному элементу импортируем класс ActionChains

# import pytest
 # здесь  посик компании, закзза  выбранного рациона

class Find_company(unittest.TestCase):


    def authorization(self, driver): # авторизация

        driver.get("https://devclient.bonration.ru/main") # меням на lifestyle

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
            "//button[@class='btn btn-border btn-border-black login-btn ripple']")))  # у тега button  есть атрибут  class со значение btn btn-border btn-border-black login-btn
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


    def setUp(self):

        self.driver = webdriver.Chrome()

        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_method_main_find_company(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(5)  # чтобы сразу окно не закрывалось


        try: #   На главной странице Кнопкк "наути компанию"
            find_button = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-fill ripple']" )))
            find_button.click()
        except TimeoutError:
            print("время ожидания вышло")

        time.sleep(2)
       #  На станцие всех компаний :
        try: # поле "Поиск":
            find_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@name='search']" )))
            find_field.send_keys("Тест_Компания Life")
            # кнопка Поиск
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//button[@class='btn search-btn ls-left ripple']"))).click()
            # спылвающая подсказка:
            #WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//*[@id='app-content']/app-search-company/div[1]/div[1]/div/div[1]/app-search/form/div[1]/div/div/button"))).click()
        except TimeoutError:
            print("время ожидания вышло")

        time.sleep(2)

        # нажимаем на корточку компании:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//div[@class='company-name']"))).click()

        # на старнице компании:






        actions = ActionChains(driver)  # создаем объект клааса ActionChains
        # выбираем вкладку рационы:
        # rations = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH,"//button[@class = 'btn tabs-switcher-item tabs-switcher-item-active")))[0]
        #
        # actions.move_to_element(rations).perform()
        # time.sleep(2)
        # rations.click()

        # переходити к поерделенной крате арицона
        actions = ActionChains(driver)
        ration_card = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='ration-card-wrapper']")))[4]

        time.sleep(2)
        actions.move_to_element(ration_card).perform()
        time.sleep(2)

        ration_card.click()
        time.sleep(2)

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/company/8']"))).click()


        # выбираем вкладку о компании:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app-content']/app-company/div/div/div[3]/app-company-large-card/div[1]/div[4]/div/div[2]"))).click()
        time.sleep(2)

        # выбираем вкладку отзывы:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app-content']/app-company/div/div/div[3]/app-company-large-card/div[1]/div[4]/div/div[3]"))).click()

        actions = ActionChains(driver)  # создаем объект клааса ActionChains
        otzyv = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app-content']/app-company/div/div/div[3]/app-company-large-card/div[2]/div/div[2]/div[5]")))
        time.sleep(3)
        actions.move_to_element(otzyv).perform()
        time.sleep(3)




    def tear_down(self):
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



