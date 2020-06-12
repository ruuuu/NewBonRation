
import unittest
import  time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # ожидания различных событий
from selenium.webdriver.support.ui import Select  # работа со списками
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from random import randint

#driver = webdriver.Firefox()
#driver = webdriver.Chrome()
#driver.get("http://www.python.org")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q") # получение поля поиска по его атрибуту  name
#elem.send_keys("Руфина") # вводим в поле поиска "Руфина"
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close() # закрывает браузер

class LoginMailBox(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Chrome()
        #self.driver.implicitly_wait(5)
        
        
    def test_user_login(self): 
        driver = self.driver
#        driver.get("https://mail.ukr.net/desktop/login")
#        #login_field = driver.find_element_by_id("id-1") #поиск элемента по его id=id-1
#        login_field = driver.find_element_by_name("Login")
#        login_field.send_keys("autotestorgua") #ввод autotestorgua в элемент(в  нашем случае поле логина)
#        password_field = driver.find_element_by_id("id-2")#поиск элемента по его id=id-2
#        password_field.send_keys("testpass")#ввод testpass в элемент(в  нашем случае поле пароля)
#        button_login = driver.find_element_by_xpath("//*[text()='Увійти']")
#        button_login.click()#нажатие на элемент
#        #user_mail = driver.find_element_by_xpath("//*[@class='login-button__user']")
#        assert "No results found." not in driver.page_source
#        #assert user_mail.text == "autotestorgua@ukr.net"
        

        #driver.get("https://devclient.bonration.ru/main")
        #login_field = driver.find_element_by_name("login")
        #login_field.send_keys("admin@mail.ru") #ввод autotestorgua в элемент(в  нашем случае поле логина)
#        password_field = driver.find_element_by_name("password")
#        password_field.send_keys("password")
#        button_login = driver.find_element_by_xpath("//*[text()='ВОЙТИ']")
#       # driver.find_elements_by_class_name()        
#        button_login.click()#нажатие на элемент
    
        # login_field = driver.find_element_by_class_name("lm-input.ng-pristine.ng-invalid.ng-touched")
        # login_field.send_keys("admin@mail.ru")
        # password_field = driver.find_element_by_class_name("lm-input ng-pristine ng-invalid ng-touched")
        # password_field.send_keys("password")

        # enter_button = WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        #     (By.XPATH, "//button[@class='btn btn-border btn-border-black login-btn ripple']"))) # кнопка Войти
        #
        # print("test on enter_button is ", enter_button.text) # тектс сн эелементе нахож
        #driver.get("https://devadmin.bonration.ru/external/login")
        # time.sleep(2)
        # enter_button.click()
        # time.sleep(2)
        # email_field = WebDriverWait(driver, 10).until(
        #     ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Email']")))  #
        # email_field.send_keys("rufinka_91@mail.ru")
        #
        # password_field = WebDriverWait(driver, 10).until(
        #     ec.presence_of_element_located((By.XPATH, "//input[@placeholder='Пароль']")))
        # password_field.send_keys("7071991")
        #
        # button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//button[@class='btn btn-fill btn-fill-full needsclick ripple']")))
        # time.sleep(3)
        #
        # button_voity.click()
        #
        # time.sleep(3)
        # driver.get("https://devclient.bonration.ru/search")
        #
        # list_names_comanies = []
        # WebDriverWait(driver, 10).until(ec.presence_of_element_located(
        #     (By.XPATH, "//button[@class='btn search-btn ripple']"))).click() # кнопка Найти рацион
        # time.sleep(5)
        # list_names = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,  "//div[@class='company-name']")))
        # for i in range(0, len(list_names)-1):
        #     time.sleep(2)
        #     print(list_names[i])
    #-------------------------------------------
        driver.get("https://devadmin.bonration.ru/external/login")
        driver.set_window_position(0, 0)  # устанавливает позицию левого вурзнего угла окна браузера
        driver.set_window_size(1440, 900)  # устанавливае мразмеры окна

        time.sleep(2)
        try:
            email_field = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-0']")))  #
            email_field.send_keys("wyvzmp5iy5oh@mail.ru")
        except:
            time.sleep(5)
            email_field.send_keys("wyvzmp5iy5oh@mail.ru")

        # try:
        #     password_field = WebDriverWait(driver, 10).until(
        #         ec.presence_of_element_located((By.XPATH, "//*[@id='mat-input-1']")))
        #     password_field.send_keys("qwerty")
        # except:
        #     time.sleep(5)
        #     password_field.send_keys("qwerty")
        #
        # button_voity = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,
        #                                                                                "/html/body/app-root/portal-login/div/mat-card/mat-card-content[2]/div/div/div/app-spinner-button/button")))
        # if button_voity.is_displayed():  # если кнпока видна , то
        #     button_voity.click()
        #     print("button is visible")
        # time.sleep(6)
        #
        # WebDriverWait(driver, 10).until(
        #         ec.presence_of_element_located((By.XPATH, "//a[@href='/main/rations']"))).click()
        # time.sleep(8)
        # list_names_compamies = []
        # list_rations = WebDriverWait(driver, 10).until(
        #         ec.presence_of_all_elements_located((By.XPATH, "//mat-cell[@class='mat-cell cdk-column-name mat-column-name ng-star-inserted']")))
        #
        # for i in range(0, len(list_rations)):
        #     print(list_rations[i].text, ' ')
        #     list_names_compamies.append(list_rations[i].text)
        #     time.sleep(2)
        #
        #
        # print("список арвен", list_names_compamies)
        # WebDriverWait(driver, 10).until(
        #         ec.presence_of_element_located((By.XPATH,  "//input[@type='search']"))).send_keys(list_rations[randint(0, len(list_rations)-1)].text)
        #
        # time.sleep(6)


    def tear_down(self):
        time.sleep(6)
        self.driver.quit()   
        
if __name__ == "__main__":
    unittest.main()        