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
 # здесь  создание рациона

class Admin_create_ration(unittest.TestCase):




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


    def test_method_admin_create_ration(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось

        # раздел Упралвение рационами:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"/html/body/app-root/portal-layout-classic/mat-sidenav-container/mat-sidenav[1]/portal-menu-sidenav/div/div/mat-nav-list/a[3]/div/div[2]/h3"))).click()

        time.sleep(2)
        #  вполе Поиск ищет рацион:
        find =  WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//input[@type='search']")))

        find.send_keys("рацион2")
        time.sleep(3)

        # нажатие на кнопку "Добавить":
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//button[@class='add-ration-button mat-button mat-primary']"))).click()

        time.sleep(3)
        # добавляем  главное фото рациона
        driver.find_element_by_xpath("//input[@type='file']").send_keys("/Users/usse/Desktop/dichs/b073d139.jpg")
        time.sleep(2)

        #  поле Название:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='name']"))).send_keys("новый новый рацион плровд")

        # краткое описание
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='shortDescription']"))).send_keys("краткое опсиание этого рациона")


        time.sleep(2)
        # поле калории

        field_calory = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='calories']")))

        field_calory.location_once_scrolled_into_view
        time.sleep(3)
        field_calory.send_keys("67")

        time.sleep(2)

    #    #
        #  # выбмраем чекбоксы:
    #
        vegetarion =  WebDriverWait(driver, 10).until(
             ec.presence_of_element_located((By.XPATH, "//mat-checkbox[@formcontrolname='vegetarian']")))
    #
    #
        time.sleep(2)
        vegetarion.location_once_scrolled_into_view
        time.sleep(2)
        vegetarion.click()

        time.sleep(2)
        vegan = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//mat-checkbox[@formcontrolname='vegan']")))
        vegan.click()


    #    #
    #     time.sleep(2)
    #
    # #  # поле Описание рациона
        textarea = WebDriverWait(driver, 10).until(
    # #      ec.presence_of_element_located((By.XPATH, "//div[@data-placeholder='Введите описание рациона...']"))).send_keys("kgjhlkdjh dfhdfhdfh dfhfdh reytwry tyewyew rywry tyityi jtjfgj fghjgdjd")
    # #
    # #  time.sleep(2)
    #    #
    #    #  # загрузка рисунков рациона
    #    #  # 1ая картинка
    #    #  WebDriverWait(driver, 10).until(
    #    #      ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys("C:\\Users\\usse\\Desktop\\тест_блюда\\rsp.jpg")
    #    #
    #    #  time.sleep(1)
    #    #  # 2ая картинка
    #    #  WebDriverWait(driver, 10).until(
    #    #      ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(
    #    #      "C:\\Users\\usse\\Desktop\\тест_блюда\\catering1.jpg")
    #    #
    #    #  time.sleep(1)
    #    #  # 3ая картинка
    #    #  WebDriverWait(driver, 10).until(
    #    #      ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(
    #    #      "C:\\Users\\usse\\Desktop\\тест_блюда\\eda21.jpg")
    #    #
    #    #  time.sleep(3)
    #    #
    #    #  #type_priem.click()
    #    #  actions = ActionChains(driver)  # создаем объект клааса ActionChains для скролла к нужному элементу
    #    #
    #    #  # выбираем тип приема пищи: Затврак, Обед Ужин и тд.
    #    #  type_priem = WebDriverWait(driver, 10).until(
    #    #      ec.presence_of_all_elements_located((By.XPATH, "//mat-select[@placeholder='Выберите тип приема пищи']")))[0]
    #    #  time.sleep(3)
    #    #  # if type_priem.is_displayed() == False:  # если  Невидима поле
    #    #  #actions.move_to_element(type_priem).perform()  # кродллим к  этому элементу
    #    #  # actions.move_to_element(type_priem).perform()  # кродллим к  этому элементу
    #    #  # actions.move_to_element(type_priem).perform()  # кродллим к  этому элементу
    #    #  #time.sleep(3)
    #    #  type_priem.click()
    #    #
    #    #  time.sleep(2)
    #    #  zavtrak = WebDriverWait(driver, 10).until(
    #    #      ec.presence_of_all_elements_located((By.XPATH,"//span[@class='mat-option-text']")))[0] # из спсика выбираем Затврак,.
    #    #  #actions.move_to_element(zavtrak).perform()  # скроллим к  этой
    #    #  time.sleep(3)
    #    #  zavtrak.click()
    #    #
    #    #  time.sleep(3)
    #    #
    #    #  WebDriverWait(driver, 10).until(
    #    #      ec.presence_of_element_located((By.XPATH,"//input[@placeholder='Название блюда']"))).click() # ажимае на поле Название блюда
    #    #
    #    #
    #    #  time.sleep(2)
    #    #  # выбираем блюдо первое
    #    #  WebDriverWait(driver, 10).until(
    #    #      ec.presence_of_all_elements_located((By.XPATH,"//input[@placeholder='Название блюда']")))[0].click()
    #    #  driver.find_elements_by_xpath("//mat-option[@class ='mat-option ng-star-inserted']")[1].click() # выбиарем из спсика блюдо
    #    #
    #    #  time.sleep(2)
    #    #  # выбираем блюдо второе
    #    #  driver.find_elements_by_xpath("//input[@placeholder='Название блюда']")[1].click()
    #    #  driver.find_elements_by_xpath("//mat-option[@class ='mat-option ng-star-inserted']")[2].click()# выбиарем из спсика блюдо
    #    #
    #    #  time.sleep(2)
    #    #  # выбираем блюдо третье
    #    #  driver.find_elements_by_xpath("//input[@placeholder='Название блюда']")[2].click()
    #    #  driver.find_elements_by_xpath("//mat-option[@class ='mat-option ng-star-inserted']")[3].click()  # выбиарем из спсика блюдо
    #    #
    #    #  driver.find_elements_by_xpath("//button[@class ='btn ls-trash-btn ng-star-inserted']")[3].click() # удаляем поснеенее добавленно блюдо
    #    #
    #    #  # i = 0
    #    #  # j = 0
    #    #  # for elem in driver.find_elements_by_xpath("//input[@placeholder='Название блюда']"):
    #    #  #     time.sleep(2)
    #    #  #     if elem.is_displayed():
    #    #  #         elem.click()
    #    #  #         time.sleep(2)
    #    #  #         driver.find_elements_by_xpath("//mat-option[@class ='mat-option ng-star-inserted']")[j].click() # выбираем и кливаем по блюду
    #    #  #         j += 1
    #    #  #         i += 1
    #    #
    #    #  time.sleep(4)
    #    #
    #    #  # кнпока Доьавить прием пищи:
    #    #  #actions = ActionChains(driver)  # создаем объект клааса ActionChains для скролла к нужному элементу
    #    #  add_type_button = WebDriverWait(driver, 10).until(
    #    #      ec.presence_of_element_located((By.XPATH,"//button[@class='ls-white-bg mat-raised-button']")))
    #    #
    #    #  # if add_type_button.is_displayed()== False: # если кнопка Невидима
    #    #  #     print("неидимая кнопка")
    #    #  #
    #    #  #
    #    #  #     actions.move_to_element(add_type_button).perform()  # кродллим к  этой кнопке
    #    #  #
    #    #  #     time.sleep(4)
    #    #  add_type_button.click()
    #    #  # else:
    #    #  #     add_type_button.click()
    #    #
    #    #
    #    #
    #    #
    #    #  # выбираем тип приема пищи:
    #    #  time.sleep(3)
    #    #  driver.find_elements_by_xpath("//mat-select[@placeholder='Выберите тип приема пищи']")[1].click()
    #    #  driver.find_elements_by_xpath("//span[@class='mat-option-text']")[3].click()  # из спсика выираем Затврак, ужит и тд.
    #    #
    #    #  time.sleep(3)
    #    #  driver.find_elements_by_xpath("//input[@placeholder='Название блюда']")[3].click()
    #    #  time.sleep(3)
    #    #  driver.find_elements_by_xpath("//mat-option[@class ='mat-option ng-star-inserted']")[2].click()# выбиарем из спсика блюдо
    #    #
    #    #  driver.find_elements_by_xpath("//input[@placeholder='Название блюда']")[4].click()
    #    #  time.sleep(3)
    #    #  driver.find_elements_by_xpath("//mat-option[@class ='mat-option ng-star-inserted']")[0].click()# выбиарем из спсика блюдо
    #    #
    #    #  time.sleep(4)
    #    # #
    #    # #
    #    # #  # ценообразовнаие рациона
    #    # #  actions = ActionChains(driver)  # создаем объект клааса ActionChains для скролла к нужному элементу
    #    #  type_ration = driver.find_element_by_xpath("//mat-select[@placeholder='Тип рациона']")
    #    # #  if type_ration.is_displayed()!= True: # если  полн не видимое
    #    # #
    #    # #      actions.move_to_element(type_ration).perform()  # переходим  к этому полю
    #    # #      time.sleep(3)
    #    #  type_ration.click()
    #    # #
    #    # #      time.sleep(1)
    #    #  # выбираем Обычный
    #    #  driver.find_elements_by_xpath("//mat-option[@class='mat-option mat-selected mat-active']")[0].click()
    #    # #
    #    #  time.sleep(1)
    #    #  # цена раицона
    #    #  driver.find_element_by_xpath("//input[@formcontrolname='price']").send_keys("145")
    #    #
    #    # #
    #    # #
    #    # #  # тогглер Скидка на пробный рацион
    #    # #  #WebDriverWait(driver, 10).until(
    #    # #      #ec.presence_of_element_located((By.XPATH, "//input[@class='mat-slide-toggle-input cdk-visually-hidden']"))).click()
    #    # #
    #    # #
    #    # #  # toogl= driver.find_element_by_xpath("input[@class='mat-slide-toggle-input cdk-visually-hidden']")
    #    # #  # if toogl.is_displayed()!= True: # или ==False
    #    # #  #     toogl.click()
    #    # #
    #    # #
    #    # #  # цена за пробный рацион
    #    # # # WebDriverWait(driver, 10).until(
    #    # #      #ec.presence_of_element_located((By.XPATH,"//input[@formcontrolname='trialPrice']"))).send_keys("190")
    #    # #
    #    #  time.sleep(4)
    #    #
    #    #  # ситсема скидок:
    #    #  driver.find_element_by_xpath("//mat-select[@placeholder='От (дней)']").click() #  нажимаем От дней
    #    #  time.sleep(2)
    #    #  driver.find_elements_by_xpath("//mat-option[@class='mat-option ng-star-inserted']")[2].click() # ыбмраем пункт из спсика
    #    #
    #    #  time.sleep(2)
    #    #  driver.find_element_by_xpath("//mat-select[@placeholder='До (дней)']").click()# выбираем До дней
    #    #
    #    #  time.sleep(2)
    #    #  driver.find_elements_by_xpath("//mat-option[@class='mat-option ng-star-inserted']")[1].click()  # ыбмраем пункт из спсика
    #    #
    #    #  driver.find_elements_by_xpath("//input[@placeholder='Цена (₽/день)']")[1].send_keys("105")
    #    #
    #    #  # след строка
    #    #  driver.find_elements_by_xpath("//mat-select[@placeholder='От (дней)']")[1].click()# нажимаем От дней
    #    #  time.sleep(2)
    #    #  driver.find_elements_by_xpath("//mat-option[@class='mat-option ng-star-inserted']")[1].click()  # ыбмраем пункт из спсика
    #    #
    #    #  time.sleep(2)
    #    #  driver.find_elements_by_xpath("//mat-select[@placeholder='До (дней)']")[1].click()  # выбираем До дней
    #    #  time.sleep(2)
    #    #  driver.find_elements_by_xpath("//mat-option[@class='mat-option ng-star-inserted']")[3].click()  # ыбмраем пункт из спсика
    #    #
    #    #  driver.find_elements_by_xpath("//input[@placeholder='Цена (₽/день)']")[2].send_keys("45")
    #    #
    #    #  time.sleep(2)
    #    #  driver.find_element_by_xpath("//button[@class='btn ls-trash-btn ng-star-inserted']").click() # кнопка Корзина, чтобы сохрнаилось, надо послеюднюю пустую строку убирать
    #    #
    #    #  time.sleep(2)
    #    #  button = driver.find_element_by_xpath("//button[@class='mat-raised-button mat-primary ng-star-inserted']") # rкнпока Сохранить
    #    #  time.sleep(3)
    #    #  button.click()
    #    #
    #    #
    #    #  time.sleep(10)

    def tear_down(self):

        time.sleep(5)# чтобы окно сразу не закрывалось
        self.driver.close()
        time.sleep(5)
        # pass


if __name__ == "__main__":
    unittest.main()



