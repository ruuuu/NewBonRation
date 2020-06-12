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

        self.driver = webdriver.Chrome() #Firefox()
        self.driver.set_window_size(1440, 900)  # устанавливае мразмеры окна
        #self.driver.maximize_window() # раотает только  в FF

        # self.driver.implicitly_wait(10) # для  явных ожиданий, будет вызываться перед каждвм методом find_element()


    def test_method_admin_create_ration(self):  # главный метод, надо чтобы он начинался  с test_

        driver = self.driver
        self.authorization(driver)  # вызов метода,котрый выше
        time.sleep(4)  # чтобы сразу окно не закрывалось

        # раздел Упралвение рационами:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"/html/body/app-root/portal-layout-classic/mat-sidenav-container/mat-sidenav[1]/portal-menu-sidenav/div/div/mat-nav-list/a[3]/div/div[2]/h3"))).click()

        time.sleep(5)
        #  вполе Поиск ищет рацион:
        find =  WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//input[@type='search']")))

        find.send_keys("рацион2")
        time.sleep(3)

        try:
            # нажатие на кнопку "Добавить":
            add_button = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"//button[@class='add-ration-button mat-button mat-primary']")))
            add_button.click()
        except:
           time.sleep(6)
           add_button.click()

        time.sleep(5)
        # добавляем  главное фото рациона
        driver.find_element_by_xpath("//input[@type='file']").send_keys("/Users/rufina/Desktop/dishs/IMG_0848.jpg")
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

        #(660, 604)
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              field_calory)  # скриллим к этому элемементу(который не виден) field_calory ПОМОГЛО!!
        time.sleep(3)
        field_calory.send_keys("67")

        time.sleep(2)





        # выбмраем чекбоксы:

        vegetarion =  WebDriverWait(driver, 10).until(
             ec.presence_of_element_located((By.XPATH, "//mat-checkbox[@formcontrolname='vegetarian']")))

        driver.execute_script("arguments[0].scrollIntoView(true);",
                              vegetarion)  # скриллим к этому элемементу(который не виден) vegetarion ПОМОГЛО!!

        time.sleep(2)
        vegetarion.click()

        time.sleep(2)
        vegan = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//mat-checkbox[@formcontrolname='vegan']")))
        vegan.click()
        time.sleep(2)
        vegan.click()
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//mat-checkbox[@formcontrolname='halal']"))).click()


        time.sleep(2)

        # поле Описание рациона
        textarea = WebDriverWait(driver, 10).until(
         ec.presence_of_element_located((By.XPATH, "//div[@data-placeholder='Введите описание рациона...']"))).send_keys("kgjhlkdjh dfhdfhdfh dfhfdh reytwry tyewyew rywry tyityi jtjfgj fghjgdjd")

        time.sleep(2)

        # загрузка рисунков рациона
        # 1ая картинка
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys("/Users/rufina/Desktop/dishs/Bulgur-Salat-mit-Roter-Bete-und-Kichererbsen-c64688bad91b6f26599f9689acef4aca_et2012021151.jpg")

        time.sleep(1)
        # 2ая картинка
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(
            "/Users/rufina/Desktop/dishs/big_28801.jpg")

        time.sleep(1)
        # 3ая картинка
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(
            "/Users/rufina/Desktop/dishs/caption (1).jpg")

        time.sleep(2)






        # если колв блюд ранво 4, если увелиить коло блюд, то здесь тоже надо увеличить
        #dict_nums = {0: range(0, 4), 1: range(4, 8), 2: range(8, 12), 3: range(12, 16), 4: range(16, 20), 5: range(20, 24), 6: range(24, 12), 7: range(28, 32)}

        for j in range(0, 3): # проохдимся повсем типам приема пищи их 7 типов, чтоы долго неддать огранчилсь до 3

            if j == 0:
                # выбираем тип приема пищи: Затврак, Обед Ужин и тд.
                type_priem = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located(
                        (By.XPATH, "//mat-select[@placeholder='Выберите тип приема пищи']")))[j]  # 0  из 8

                driver.execute_script("arguments[0].scrollIntoView(true);",
                                      type_priem)  # скриллим к этому элемементу(который не виден) type_priem ПОМОГЛО!
                type_priem.click()

                type_food = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))[  # 0  из 8
                    j]  # Выбираем Обед6Ужин и т/д/
                time.sleep(2)
                type_food.click()

                for i in range(0, 4):
                    time.sleep(2)
                    #  выбираем блюдо первое
                    WebDriverWait(driver, 10).until(
                        ec.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Название блюда']")))[i].click()
                    time.sleep(2)
                    WebDriverWait(driver, 10).until(
                        ec.presence_of_all_elements_located(
                        (By.XPATH, "//mat-option[@class ='mat-option ng-star-inserted']")))[i].click()  # выбиарем из спсика блюдо
                    time.sleep(2)
                # кнпока Добавить тип приема пищи
                add_button = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='ls-white-bg mat-raised-button']")))
                driver.execute_script("arguments[0].scrollIntoView(true);",
                                      add_button)  # скриллим к этому элемементу(который не виден) calendar ПОМОГЛО!

                add_button.click()
                time.sleep(2)



            if j == 1:
                # выбираем тип приема пищи: Затврак, Обед Ужин и тд.
                type_priem = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located(
                        (By.XPATH, "//mat-select[@placeholder='Выберите тип приема пищи']")))[j]  # 0  из 8

                driver.execute_script("arguments[0].scrollIntoView(true);",
                                      type_priem)  # скриллим к этому элемементу(который не виден) type_priem ПОМОГЛО!
                type_priem.click()

                type_food = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))[  # 0  из 8
                    j]  # Выбираем Обед6Ужин и т/д/
                time.sleep(2)
                type_food.click()

                for i in range(4, 8):
                    time.sleep(2)
                 #  выбираем блюдо первое
                    WebDriverWait(driver, 10).until(
                        ec.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Название блюда']")))[i-4].click()
                    time.sleep(2)

                    WebDriverWait(driver, 10).until(
                        ec.presence_of_all_elements_located(
                        (By.XPATH, "//mat-option[@class ='mat-option ng-star-inserted']")))[i-4].click()  # выбиарем из спсика блюдо
                # кнпока Добавить тип приема пищи
                add_button = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
                    (By.XPATH, "//button[@class='ls-white-bg mat-raised-button']")))
                driver.execute_script("arguments[0].scrollIntoView(true);",
                                      add_button)  # скриллим к этому элемементу(который не виден) calendar ПОМОГЛО!

                add_button.click()
                time.sleep(2)

            if j == 2:
                # выбираем тип приема пищи: Затврак, Обед Ужин и тд.
                type_priem = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located(
                        (By.XPATH, "//mat-select[@placeholder='Выберите тип приема пищи']")))[j]  # 0  из 8

                driver.execute_script("arguments[0].scrollIntoView(true);",
                                      type_priem)  # скриллим к этому элемементу(который не виден) type_priem ПОМОГЛО!
                type_priem.click()

                type_food = WebDriverWait(driver, 10).until(
                    ec.presence_of_all_elements_located((By.XPATH, "//span[@class='mat-option-text']")))[  # 0  из 8
                    j]  # Выбираем Обед6Ужин и т/д/
                time.sleep(2)
                type_food.click()


                for i in range(8, 12):
                    time.sleep(2)
                    #  выбираем блюдо первое
                    dish = WebDriverWait(driver, 10).until(
                        ec.presence_of_all_elements_located((By.XPATH, "//input[@placeholder='Название блюда']")))[i]
                    driver.execute_script("arguments[0].scrollIntoView(true);",
                                          dish)  # скриллим к этому элемементу(который не виден) type_priem ПОМОГЛО!
                    dish.click()
                    time.sleep(2)

                    WebDriverWait(driver, 10).until(
                            ec.presence_of_all_elements_located(
                                (By.XPATH, "//mat-option[@class ='mat-option ng-star-inserted']")))[i-8].click()  # выбиарем из спсика блюдо



        time.sleep(3)
        #ценообразовнаие рациона
        type_ration = WebDriverWait(driver, 10).until(
                        ec.presence_of_element_located((By.XPATH, "//mat-select[@placeholder='Тип рациона']")))

        driver.execute_script("arguments[0].scrollIntoView(true);",
                              type_ration)  # скриллим к этому элемементу(который не виден) type_ration ПОМОГЛО!
        time.sleep(2)
        type_ration.click()

        # выбираем Обычный
        WebDriverWait(driver, 10).until(
                        ec.presence_of_all_elements_located((By.XPATH,"//mat-option[@class='mat-option mat-selected mat-active']")))[0].click()

        time.sleep(1)
        # цена раицона
        WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='price']"))).send_keys("145")

        time.sleep(2)
        # тогглер Скидка на пробный рацион
        toggle = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//div[@class='mat-slide-toggle-thumb-container']")))

        driver.execute_script("arguments[0].scrollIntoView(true);", toggle)  # скриллим к этому элемементу(который не виден) calendar ПОМОГЛО!
        time.sleep(2)
        toggle.click()



        # цена за пробный рацион
        WebDriverWait(driver, 10).until(
             ec.presence_of_element_located((By.XPATH, "//input[@formcontrolname='trialPrice']"))).send_keys("190")

        time.sleep(4)

        sales_price = {0: 456, 1: 367, 2: 290}
        # ситсема скидок:
        for i in range(0, 3): # сделаем три строки

            start_day = driver.find_elements_by_xpath("//mat-select[@placeholder='От (дней)']")[i]
            driver.execute_script("arguments[0].scrollIntoView(true);",
                                  start_day)  # скриллим к этому элемементу(который не виден) calendar ПОМОГЛО!

            start_day.click() # нажимаем От дней
            time.sleep(2)
            driver.find_elements_by_xpath("//mat-option[@class='mat-option ng-star-inserted']")[i+1].click()  # ыбмраем пункт из спсика  # колво дней = 2,3,4, .....,25
            time.sleep(2)
            driver.find_elements_by_xpath("//mat-select[@placeholder='До (дней)']")[i].click()  # выбираем До дней
            time.sleep(2)
            driver.find_elements_by_xpath("//mat-option[@class='mat-option ng-star-inserted']")[i+2].click()  # ыбмраем пункт из спсика
            time.sleep(2)
            driver.find_elements_by_xpath("//input[@placeholder='Цена (₽/день)']")[i+2].send_keys(sales_price[i]) # вбиваем цену

        #
        time.sleep(2) #!!!!здесь подправить, удаляет не ту корзину
        driver.find_element_by_xpath("//button[@class='btn ls-trash-btn ng-star-inserted']").click() # кнопка Корзина, чтобы сохрнаилось, надо послеюднюю пустую строку убирать

        button = driver.find_element_by_xpath(
            "//button[@class='mat-raised-button mat-primary ng-star-inserted']")  # кнпока Сохранить
        if button.is_enabled(): #  если true т/е/ если кнпока кликабельна
            time.sleep(2)
            button.click()
        else:

            print("кнопка  Сохранить некликбаеьлна")
        time.sleep(10)

        # #ситсема скидок:
        # driver.find_element_by_xpath("//mat-select[@placeholder='От (дней)']").click() #  нажимаем От дней
        # time.sleep(2)
        # driver.find_elements_by_xpath("//mat-option[@class='mat-option ng-star-inserted']")[2].click() # ыбмраем пункт из спсика
        #
        # time.sleep(2)
        # driver.find_element_by_xpath("//mat-select[@placeholder='До (дней)']").click()# выбираем До дней
        #
        # time.sleep(2)
        # driver.find_elements_by_xpath("//mat-option[@class='mat-option ng-star-inserted']")[1].click()  # ыбмраем пункт из спсика
        #
        # driver.find_elements_by_xpath("//input[@placeholder='Цена (₽/день)']")[1].send_keys("105")
        #
        #
        #
        # # след строка
        # driver.find_elements_by_xpath("//mat-select[@placeholder='От (дней)']")[1].click()# нажимаем От дней
        # time.sleep(2)
        # driver.find_elements_by_xpath("//mat-option[@class='mat-option ng-star-inserted']")[1].click()  # ыбмраем пункт из спсика
        #
        # time.sleep(2)
        # driver.find_elements_by_xpath("//mat-select[@placeholder='До (дней)']")[1].click()  # выбираем До дней
        # time.sleep(2)
        # driver.find_elements_by_xpath("//mat-option[@class='mat-option ng-star-inserted']")[3].click()  # ыбмраем пункт из спсика
        #
        # driver.find_elements_by_xpath("//input[@placeholder='Цена (₽/день)']")[2].send_keys("45")
        #
        # time.sleep(2)
        # driver.find_element_by_xpath("//button[@class='btn ls-trash-btn ng-star-inserted']").click() # кнопка Корзина, чтобы сохрнаилось, надо послеюднюю пустую строку убирать







    def tear_down(self):
        time.sleep(10)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()



