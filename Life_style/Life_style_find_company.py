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
from random import randint
# import pytest
 # здесь  посик компании, закзза  выбранного рациона

class Find_company(unittest.TestCase):


    def authorization(self, driver): # авторизация

        driver.get("https://devclient.bonration.ru/main") # меням на lifestyle

        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
            "//button[@class='btn btn-border btn-border-black login-btn ripple']")))  # у тега button  есть атрибут  class со значение btn btn-border btn-border-black login-btn
        button_voity.click()

        try:
            email_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@type='email']" )))# /html/body/app-root/app-modal/div/div[1]/div/app-login/div/div[2]/form/div[1]/input
            email_field.send_keys("rufinka_91@mail.ru")
        except TimeoutError:
            print("время ожидания поля емэйл вышло")

        try:
            password_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']" )))
            password_field.send_keys("7071991")
        except TimeoutError:
            print("время ожидания поля пароль вышло")
        button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-fill btn-fill-full needsclick ripple']")))
        button_voity.click()
        time.sleep(3)


    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна

        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_method_main_find_company(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(5)  # чтобы сразу окно не закрывалось


        try: #   На главной странице Кнопкк "наути рацион"
            find_button = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//a[@href='/search']" )))
            find_button.click()
        except TimeoutError:
            print("время ожидания вышло")

        time.sleep(2)
       #  На станцие всех компаний :
        try: # поле "Поиск":
            find_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@name='search']" )))
            find_field.send_keys("Company Life")
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

        list_ration_cards = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='ration-card-wrapper']")))

        print("count of ration_cards equal", len(list_ration_cards))

        rand_ind_card = randint(0, len(list_ration_cards)-1)
        print("randon index of card equal", rand_ind_card)

        ration_card = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='ration-card-wrapper']")))[rand_ind_card]

        time.sleep(2)
        driver.execute_script("arguments[0].scrollIntoView(true);", ration_card)  # скриллим к этому элемементу
        time.sleep(2)

        ration_card.click()
        time.sleep(2)


        time.sleep(2)

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/company/8']"))).click()
        time.sleep(2)

        # выбираем вкладку о компании:
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn tabs-switcher-item']")))[0].click()
        time.sleep(2)
        for i in range(0,10):
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN) # идем вниз страницы


        # выбираем вкладку отзывы:
        vkladka_otzuvy = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn tabs-switcher-item']")))[1]
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              vkladka_otzuvy)  # скриллим к этому элемементу(который не виден) calendar ПОМОГЛО!!и элемент этот подтянется к верху станицы
        time.sleep(2)
        vkladka_otzuvy.click()

        time.sleep(2)
        for i in range(0,100):
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN) # идем вниз страницы

        time.sleep(3)

        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)  # переходим вниз страницы




    def tear_down(self):
        time.sleep(5)
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



