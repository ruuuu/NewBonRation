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
 # здесь  авторизация админа(компаний)

class Admin_edit_profile_company(unittest.TestCase):




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


    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver.maximize_window()
        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_method_admin_edit_profile_company(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось

        # нажимаем вкладку Профиль компании
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/portal-layout-classic/mat-sidenav-container/mat-sidenav[1]/portal-menu-sidenav/div/div/mat-nav-list/a[6]/div/div[2]/h3"))).click()

        #удаляем и добавляем фото(главное)
        time.sleep(2)
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@type='button']"))).click()  # кнопка "удалить фото"

        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys("/Users/rufina/Desktop/dishs/1-15.jpg") # в в индовс  "C:\\Users\\usse\\Desktop\\тест_блюда\\rsp.jpg"

        time.sleep(2)
        # удаляем и меняем фото(лого):
        #  кнопка "удалить фото"
        WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='btn remove-img-button ng-star-inserted']")))[1].click()

        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys("/Users/rufina/Desktop/dishs/m22680d0.jpg")  #в в индовс  "C:\\Users\\usse\\Desktop\\тест_блюда\\rsp.jpg"

        time.sleep(2)
        #вводим нащзвание компаии
        name_company = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='name']")))

        name_company.clear()# очишает поле прежде чем его заполнять
        name_company.send_keys("Отредактированная кломпания")

        address_company = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='address']")))
        address_company.clear()
        address_company.send_keys("Казань,Ул.Ершова,дом 78")

        phone_company = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='phone']")))
        phone_company.clear()
        phone_company.send_keys("89600345935")

        time.sleep(2)


        # время начала
        start_clock = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='mat-select-arrow-wrapper']")))
        start_clock.click()

        # выбираем из списка часы рвботы
        item_start_clock = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))[16] # время 8:00
        #item_start_clock.click()


        if item_start_clock.is_displayed():  # если item виден , то
            time.sleep(1)
            item_start_clock.click()
        else:
            #скроллим к нужному элменту
            actions = ActionChains(driver)  # создаем объект клааса ActionChains
            time.sleep(1)
            actions.move_to_element(item_start_clock).perform()  #переходим к нужному элементу
            time.sleep(1)
            item_start_clock.click()




        time.sleep(2)
        end_clock =  WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='mat-select-arrow']")))[1]
        end_clock.click()

        # Время окончания :
        time.sleep(2)# выбираем из списка часы рвботы
        item_end_clock = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))[4]


        if item_end_clock.is_displayed():# если item виден , то
            time.sleep(1)
            item_end_clock.click()
        else:
            # скроллим к нужному элменту
            actions = ActionChains(driver)  # создаем объект клааса ActionChains
            time.sleep(1)
            actions.move_to_element(item_end_clock).perform()  # переходим к нужному элементу
            time.sleep(1)
            item_end_clock.click()

        time.sleep(2)



        # Доставка заказков (Утро) от :
        WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
            (By.XPATH,  "//div[@class='mat-select-arrow']")))[2].click()
        time.sleep(2)
        # выбираем из списка часы
        item_start_clock_delivery_morning = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))[9] # 4:30


        if item_start_clock_delivery_morning.is_displayed(): # если item  виден то жмем
            item_start_clock_delivery_morning.click()


        else:
            # скроллим к нужному элменту
            actions = ActionChains(driver)  # создаем объект клааса ActionChains
            time.sleep(1)
            actions.move_to_element(item_start_clock_delivery_morning).perform()  # переходим к нужному элементу
            time.sleep(1)
            item_start_clock_delivery_morning.click()





        # Доставка заказков (Утро) до :
        WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='mat-select-arrow']")))[3].click()
        time.sleep(2)

        # выбираем из списка часы
        item_end_clock_delivery_morning = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))[30]  # 15:00

        if item_end_clock_delivery_morning.is_displayed():  # если item  виден то жмем
            item_end_clock_delivery_morning.click()


        else:
            # скроллим к нужному элменту
            actions = ActionChains(driver)  # создаем объект клааса ActionChains
            time.sleep(1)
            actions.move_to_element(item_end_clock_delivery_morning).perform()  # переходим к нужному элементу
            time.sleep(1)
            item_end_clock_delivery_morning.click()
        time.sleep(3)




        # Доставка заказво (Вечер)от :
        WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='mat-select-arrow']")))[4].click()
        time.sleep(2)

        # выбираем из списка часы
        item_start_clock_delivery_evening = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))[32]  # 16:00

        if item_start_clock_delivery_evening.is_displayed():
            item_start_clock_delivery_evening.click()


        else:
            # скроллим к нужному элменту
            actions = ActionChains(driver)  # создаем объект клааса ActionChains
            time.sleep(1)
            actions.move_to_element(item_start_clock_delivery_evening).perform()  # переходим к нужному элементу
            time.sleep(1)
            item_start_clock_delivery_evening.click()


        # Доставка заказво (Вечер)до :

        WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='mat-select-arrow']")))[5].click()
        time.sleep(2)

        # выбираем из списка часы
        item_end_clock_delivery_evening = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))[6]  # 18:00


        if item_end_clock_delivery_evening.is_displayed():  # если item  виден то жмем
            item_end_clock_delivery_evening.click()

        else:
            # скроллим к нужному элменту
            actions = ActionChains(driver)  # создаем объект клааса ActionChains
            time.sleep(1)
            actions.move_to_element(item_end_clock_delivery_evening).perform()  # переходим к нужному элементу
            time.sleep(1)
            item_end_clock_delivery_evening.click()


       # Прием заявок:
        WebDriverWait(driver, 20).until(ec.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='mat-select-arrow']")))[6].click()
        time.sleep(2)

        # выбираем из списка часы
        item_accept = WebDriverWait(driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))[36]  # 18:00

        if item_accept.is_displayed():  # если item  виден то жмем
            item_accept.click()
        else:
            # скроллим к нужному элменту
            actions = ActionChains(driver)  # создаем объект клааса ActionChains
            time.sleep(1)
            actions.move_to_element(item_accept).perform()  # переходим к нужному элементу
            time.sleep(1)
            item_accept.click()

        time.sleep(2)

        # тип оплаты выбираем чекбох (онлайн, курьеру наличными)
        i = 0
        for ch in driver.find_elements_by_xpath("//div[@class='mat-checkbox-inner-container']"):# из списка чекбоксов
          if (i == 1 ):
            ch.click()
          i += 1





        time.sleep(2)
        #texaerea:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//textarea[@formcontrolname='about']"))).send_keys("xfkdjgsk sgsd erfaetw sdfgs yuiry6i u4 tue w4 52435 t426ryrew ryer yeryhydhd fdgj tuew ywryw qtq tq")

        time.sleep(2)

        #тогглер: За баллы
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//div[@class='mat-slide-toggle-thumb']"))).click()

        # нажимаем на кнпоку "отмена":
        #WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='mat-button mat-primary']"))).click()#кнопка Отмена
        #time.sleep(3)
        #WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//app-spinner-button[@class='ng-star-inserted']"))).click() # в попаапе

        time.sleep(2)

        # кнопка "Сохранить"

        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//*[@id='portal-layout']/app-profile/div/div/div/app-spinner-button/button"))).click()

        time.sleep(10)  # много сек ставлю, чтобы успелось сохраниться и вышел попао с подтверждением об сохрании изменений


    def tear_down(self):
        time.sleep(8)# тобы окно сразу не закрывалось
        self.driver.quit()
        # pass


if __name__ == "__main__":
    unittest.main()



