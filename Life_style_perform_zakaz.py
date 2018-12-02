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

class Order_ration(unittest.TestCase):


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



    def setUp(self):

        self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_method_main_order_ration(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(3)  # чтобы сразу окно не закрывалось

        try:  # На главной странице Кнопкк "наути компанию"
            find_button = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-fill ripple']")))
            find_button.click()
        except TimeoutError:
            print("время ожидания вышло")

        time.sleep(2)
        #  На станцие всех компаний :
        try:  # поле "Поиск":
            find_field = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//input[@name='search']")))
            find_field.send_keys("Тест_Компания Life")
            # кнопка Поиск
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//button[@class='btn search-btn ls-left ripple']"))).click()
            # спылвающая подсказка:
            # WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//*[@id='app-content']/app-search-company/div[1]/div[1]/div/div[1]/app-search/form/div[1]/div/div/button"))).click()
        except TimeoutError:
            print("время ожидания вышло")

        time.sleep(2)

        # нажимаем на корточку компании:
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='company-name']"))).click()

        # на старнице компании:
        # выбираем вкладку рационы:
        #WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
                                                                        #"//*[@id='app-content']/app-company/div/div/div[3]/app-company-large-card/div[1]/div[4]/div/div[1]"))).click()
        time.sleep(2)

        # переходити к поерделенной крате арицона
        actions = ActionChains(driver)  # создаем объект клааса ActionChains
        ration_card = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='ration-card-wrapper']")))[2] # НОВЫЙ  МЕТОД!!!

        time.sleep(2)
        actions.move_to_element(ration_card).perform()
        time.sleep(2)
        ration_card.click() # нажимаем накрату рациона

        time.sleep(3)

        #кнопка "Заказать": на странице рациона

        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-fill ripple']"))).click()

        #форма заполнения                                                                       "//*[@id="app-content"]/app-ordering/div/div/div[3]/div[2]/section[1]/app-ordering-duration/button"
        count_days = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app-content']/app-ordering/div/div/div[3]/div[2]/section[1]/app-ordering-duration/button")))
        if count_days.is_displayed():# если полде видное т
            count_days.click()

        # нажимаем кнопку + :
        for i in range(4):
            time.sleep(2)
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn ls-calc-btn ls-calc-plus']" ))).click()


        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn ls-calc-btn ls-calc-minus']"))).click()

        # Форма доставки:
        # Дата:

        day = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@id='date-input-2']"))) # из каоендаря выбирвае дату
        day.click()
        time.sleep(3) # ждем пока календарь появится
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app-content']/app-ordering/div/div/div[3]/div[2]/section[3]/app-ordering-delivery/form/div[1]/div[1]/div[3]/div[2]/div[37]"))).click() # выбрали дату

        time.sleep(1)
        #время доставки:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='time']"))).click()
        time.sleep(2)
        # из выпадающего спсика выбираем item
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='select-item']")))[5].click()

        time.sleep(2)

        # поделание  к заказу
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname='comment']"))).send_keys("kgjhl dfhdfl dfhf dfhj;kdfj kdjhds mdghjld dhjdl")


       #для неавторизованного клиента:
       #  # Адрес
       # # WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app-content']/app-ordering/div/div/div[3]/div[2]/section[2]/app-ordering-delivery/form/div[2]/input"))).send_keys("ул")
       # #Дом
       #  home =  WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app-content']/app-ordering/div/div/div[3]/div[2]/section[2]/app-ordering-delivery/form/div[3]/div[1]/input")))
       #  home.clear()# если поле не очищенное то егон адо очишатьс перва
       #  home.send_keys("6")
       #  # подъезд:
       #  WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app-content']/app-ordering/div/div/div[3]/div[2]/section[2]/app-ordering-delivery/form/div[3]/div[2]/input"))).send_keys("67")
       #  # Этаж
       #  WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='app-content']/app-ordering/div/div/div[3]/div[2]/section[2]/app-ordering-delivery/form/div[4]/div[1]/input"))).send_keys("3")
       #

         #способ оплаты:
        WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//button[@class='btn radio-wrapper']")))[4].click()
        time.sleep(3)

        #кнопка Офрмить заказ
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-fill ordering-footer-btn ripple']"))).click()

        time.sleep(3)
        # "Продолжить" в попапе подтвержденяи оплаты
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-fill btn-fill-full ripple']"))).click()

        time.sleep(3)
        # на станице раицона, жмем Личный кабинет вверху:
        WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn profile-btn']"))).click()

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH,"//div[@class='profile-drop-down-item']")))[0].click()

        time.sleep(3)

    def tear_down(self):
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



