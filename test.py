import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from credentials import credentials
from locators import LoginPageLocators, ResetPasswordPageLocators
from locators import RegisterPageLocators

username = credentials["username"]
password = credentials["password"]
invalid_name = credentials["invalid_name"]


def test_login_with_email():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()

    # Переход на страницу авторизации
    driver.get("https://b2c.passport.rt.ru")

    # Инициализация страницы авторизации
    login_page = LoginPageLocators(driver)

    # Нажатие на вкладку с почтой
    email_tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "t-btn-tab-mail")))
    email_tab.click()

    # Ввод логина
    login_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username")))
    login_input.send_keys(credentials["username"])

    # Ввод пароля
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password")))
    password_input.send_keys(credentials["password"])

    # Создание папки для сохранения скриншотов
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    # Сохранение скриншота
    driver.save_screenshot('test_login_with_email.png')

    # Нажатие на кнопку входа
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "kc-login")))
    login_button.click()


    # Проверка, что пользователь авторизовался успешно
    assert "Ростелеком ID" in driver.title

    # Закрытие браузера
    driver.quit()

def test_login_with_phone_tab():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()

    # Переход на страницу авторизации
    driver.get("https://b2c.passport.rt.ru")

    # Инициализация страницы авторизации
    login_page = LoginPageLocators(driver)

    # Нажатие на вкладку телефон
    phone_tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "t-btn-tab-phone")))
    phone_tab.click()

    # Ввод телефона
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username")))
    phone_input.send_keys(credentials["phone"])

    # Ввод пароля
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password")))
    password_input.send_keys(credentials["password"])

    # Нажатие на кнопку входа
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "kc-login")))
    login_button.click()

    # Ожидание загрузки страницы после входа
    WebDriverWait(driver, 10).until(
        EC.title_contains("Ростелеком ID"))

    # Проверка, что пользователь авторизовался успешно
    assert "Ростелеком ID" in driver.title

    # Создание папки для сохранения скриншотов
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    # Сохранение скриншота
    driver.save_screenshot('test_login_with_phone_tab.png')

    # Закрытие браузера
    driver.quit()

def test_login_with_invalid_phone():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()

    # Переход на страницу авторизации
    driver.get("https://b2c.passport.rt.ru")

    # Инициализация страницы авторизации
    login_page = LoginPageLocators(driver)

    # Нажатие на вкладку телефон
    phone_tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "t-btn-tab-phone")))
    phone_tab.click()

    # Ввод неверного номера телефона
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username")))
    phone_input.send_keys(credentials["not-valid-phone"])

    # Ввод верного пароля
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password")))
    password_input.send_keys("password")

    # Нажатие на кнопку входа
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "kc-login")))
    login_button.click()

    # Проверка, что появилось сообщение об ошибке
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "form-error-message")))
    assert error_message.text == "Неверно введен текст с картинки"

    # Создание папки для сохранения скриншотов
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    # Сохранение скриншота
    driver.save_screenshot('test_login_with_invalid_phone.png')

    # Закрытие браузера
    driver.quit()

def test_login_with_incorrect_password():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()

    # Переход на страницу авторизации
    driver.get("https://b2c.passport.rt.ru")

    # Инициализация страницы авторизации
    login_page = LoginPageLocators(driver)

    # Нажатие на вкладку телефон
    phone_tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "t-btn-tab-phone")))
    phone_tab.click()

    # Ввод верного номера телефона
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username")))
    phone_input.send_keys(credentials["phone"])

    # Ввод неверного пароля
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password")))
    password_input.send_keys("not-valid-password")

    # Нажатие на кнопку входа
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "kc-login")))
    login_button.click()

    # Проверка, что появилось сообщение об ошибке
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "form-error-message")))
    assert error_message.text == "Неверно введен текст с картинки"

    # Создание папки для сохранения скриншотов
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    # Сохранение скриншота
    driver.save_screenshot('screenshots/test_login_with_incorrect_password.png')

    # Закрытие браузера
    driver.quit()

def test_login_button_phone_tab():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()

    # Переход на страницу авторизации
    driver.get("https://b2c.passport.rt.ru")

    # Инициализация страницы авторизации
    login_page = LoginPageLocators(driver)

    # Нажатие на вкладку телефон
    phone_tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "t-btn-tab-phone")))
    phone_tab.click()

    # Нажатие на кнопку входа
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "kc-login")))
    login_button.click()

    # Проверка, что появилось сообщение об ошибке "Введите номер телефона"
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container login-form-container']/div[@class='card-container__wrapper']/div[@class='card-container__content']/form[@class='login-form']/div[@class='tabs-input-container']/div[@class='rt-input-container rt-input-container--error tabs-input-container__login']/span[@class='rt-input-container__meta rt-input-container__meta--error']")))
    assert error_message.text == "Введите номер телефона"

    # Создание папки для сохранения скриншотов
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    # Сохранение скриншота
    driver.save_screenshot('screenshots/test_login_button_phone_tab.png')

    # Закрытие браузера
    driver.quit()

def test_login_with_invalid_Email():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()

    # Переход на страницу авторизации
    driver.get("https://b2c.passport.rt.ru")

    # Инициализация страницы авторизации
    login_page = LoginPageLocators(driver)

    # Нажатие на вкладку с почтой
    email_tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "t-btn-tab-mail")))
    email_tab.click()

    # Ввод неверной почты
    login_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username")))
    login_input.send_keys(credentials["not-validEmail"])

    # Ввод верного пароля
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password")))
    password_input.send_keys("password")

    # Нажатие на кнопку входа
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "kc-login")))
    login_button.click()

    # Проверка, что появилось сообщение об ошибке "Неверно введен текст с картинки"
    error_message = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.ID, "form-error-message")))
    assert error_message.text == "Неверно введен текст с картинки"

    # Создание папки для сохранения скриншотов
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    # Сохранение скриншота
    driver.save_screenshot('screenshots/test_login_with_invalid_Email.png')

    # Закрытие браузера
    driver.quit()

def test_login_button_Email_tab():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()

    # Переход на страницу авторизации
    driver.get("https://b2c.passport.rt.ru")

    # Инициализация страницы авторизации
    login_page = LoginPageLocators(driver)

    # Нажатие на вкладку с почтой
    email_tab = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "t-btn-tab-mail")))
    email_tab.click()

    # Нажатие на кнопку входа
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "kc-login")))
    login_button.click()

    # Проверка, что появилось сообщение об ошибке "Введите адрес указаный при регистрации"
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container login-form-container']/div[@class='card-container__wrapper']/div[@class='card-container__content']/form[@class='login-form']/div[@class='tabs-input-container']/div[@class='rt-input-container rt-input-container--error tabs-input-container__login']/span[@class='rt-input-container__meta rt-input-container__meta--error']")))
    assert error_message.text == "Введите адрес, указанный при регистрации"

    # Создание папки для сохранения скриншотов
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    # Сохранение скриншота
    driver.save_screenshot('screenshots/test_login_button_Email_tab.png')

    # Закрытие браузера
    driver.quit()

def test_login_with_invalidformat_phone():
    # Инициализация драйвера браузера
        driver = webdriver.Chrome()

        # Переход на страницу авторизации
        driver.get("https://b2c.passport.rt.ru")

        # Инициализация страницы авторизации
        login_page = LoginPageLocators(driver)

        # Нажатие на вкладку телефон
        phone_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "t-btn-tab-phone")))
        phone_tab.click()

        # Ввод номера телефона в неправильном формате менее 10 символов
        phone_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username")))
        phone_input.send_keys(credentials["invalid-format-phone"])

        # Нажатие на кнопку входа
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "kc-login")))
        login_button.click()

        # Проверка, что появилось сообщение об ошибке
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "/html/body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container login-form-container']/div[@class='card-container__wrapper']/div[@class='card-container__content']/form[@class='login-form']/div[@class='tabs-input-container']/div[@class='rt-input-container rt-input-container--error tabs-input-container__login']/span[@class='rt-input-container__meta rt-input-container__meta--error']")))
        assert error_message.text == "Неверный формат телефона"

        # Создание папки для сохранения скриншотов
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')

        # Сохранение скриншота
        driver.save_screenshot('test_login_with_invalidformat_phone.png')

        # Закрытие браузера
        driver.quit()

def test_register_link():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()

    # Переход на страницу авторизации
    driver.get("https://b2c.passport.rt.ru")

    # Инициализация страницы авторизации
    login_page = LoginPageLocators(driver)

    # Клик на ссылку "Зарегистрироваться"
    register_link = login_page.register_link
    register_link.click()

    # Проверка, что перешли на страницу регистрации
    register_page = RegisterPageLocators()
    register_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(register_page.REGISTER_TITLE))
    assert register_title.text == "Регистрация"

    # Создание папки для сохранения скриншотов
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    # Сохранение скриншота
    driver.save_screenshot('test_register_link.png')

    # Закрытие браузера
    driver.quit()


def test_vk_social_login():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()

    # Переход на страницу авторизации
    driver.get("https://b2c.passport.rt.ru")

    # Инициализация страницы авторизации
    login_page = LoginPageLocators(driver)

    # Нажатие на кнопку авторизации через VK
    vk_social_login = login_page.vk_social_login
    vk_social_login.click()

    # Проверка текста на странице авторизации
    vk_auth_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                     "/html/body[@class='VK oauth_centered']/div[@class='oauth_wrap']/div[@class='oauth_wrap_inner']/div[@id='oauth_wrap_content']/div[@class='oauth_content box_body clear_fix']/div[@class='box_msg_gray box_msg_padded']")))
    assert vk_auth_text.text == "Для продолжения вам необходимо войти ВКонтакте."

    # Закрытие окна авторизации
    driver.close()

def test_remember_me_checkbox():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()

    # Переход на страницу авторизации
    driver.get("https://b2c.passport.rt.ru")

    # Инициализация страницы авторизации
    login_page = LoginPageLocators(driver)

    # Ввод логина
    login_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username")))
    login_input.send_keys(credentials["username"])

    # Ввод пароля
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password")))
    password_input.send_keys(credentials["password"])

    # Поставить галочку в поле "Запомнить меня"
    login_page.remember_me_checkbox.click()

    # Перезагрузка страницы
    driver.refresh()

    # Проверка, что логин и пароль остаются введены
    assert login_page.login_field.get_attribute("value") == "username"
    assert login_page.password_field.get_attribute("value") == "password"

    # Закрытие браузера
    driver.quit()

def test_switch_to_email_tab(self=None):
        # Инициализация драйвера браузера
        driver = webdriver.Chrome()

        # Переход на страницу авторизации
        driver.get("https://b2c.passport.rt.ru")

        # Инициализация страницы авторизации
        login_page = LoginPageLocators(driver)

        # Ввод почты в поле телефон
        login_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username")))
        login_input.send_keys(credentials["username"])

        # Ввод пароля
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password")))
        password_input.send_keys(credentials["password"])

        # Подождите, пока вкладка электронной почты станет активной
        email_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container login-form-container']/div[@class='card-container__wrapper']/div[@class='card-container__content']/form[@class='login-form']/div[@class='tabs-input-container']/div[@class='rt-tabs rt-tabs--orange rt-tabs--small tabs-input-container__tabs']/div[@id='t-btn-tab-mail']"))
        )

        # проверяем что почтатаб активна
        assert "rt-tab--active" in email_tab.get_attribute("class")

        # Закрытие браузера
        driver.quit()

def test_forgot_password_link():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()

    # Переход на страницу авторизации
    driver.get("https://b2c.passport.rt.ru")

    # Инициализация страницы авторизации
    login_page = LoginPageLocators(driver)

    # Клик на кнопку "Забыли пароль?"
    forgot_password_link = login_page.forgot_password_link
    forgot_password_link.click()

    # Проверка, что мы находимся на странице восстановления пароля
    reset_password_page = ResetPasswordPageLocators(driver)
    reset_password_title = reset_password_page.reset_password_title
    assert reset_password_title.text == "Восстановление пароля"

    # Закрытие браузера
    driver.quit()


from credentials import invalid_name



def test_register_link_firstname_error():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()

    # Переход на страницу авторизации
    driver.get("https://b2c.passport.rt.ru")

    # Инициализация страницы авторизации
    login_page = LoginPageLocators(driver)

    # Клик на ссылку "Зарегистрироваться"
    register_link = login_page.register_link
    register_link.click()

    # Проверка, что перешли на страницу регистрации
    register_page = RegisterPageLocators()
    register_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(register_page.REGISTER_TITLE))
    assert register_title.text == "Регистрация"

    # Ввод некорректного имени
    invalid_name = "Дм"
    name_locator = register_page.name_input
    name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(name_locator))
    name_input.send_keys(credentials["invalid_name"])

    # Нажатие на кнопку "Зарегистрироваться"
    register_button = register_page.register_button
    register_button_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(register_button))
    register_button_element.click()

    # Проверка ошибки заполнения поля имени
    name_error = register_page.name_error
    name_error_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(name_error))
    assert name_error_element.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

    # Закрытие браузера
    driver.quit()

def test_register_link_lastname_error():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()

    # Переход на страницу авторизации
    driver.get("https://b2c.passport.rt.ru")

    # Инициализация страницы авторизации
    login_page = LoginPageLocators(driver)

    # Клик на ссылку "Зарегистрироваться"
    register_link = login_page.register_link
    register_link.click()

    # Проверка, что перешли на страницу регистрации
    register_page = RegisterPageLocators()
    register_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(register_page.REGISTER_TITLE))
    assert register_title.text == "Регистрация"

    # Ввод корректного имени
    name_locator = register_page.name_input
    name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(name_locator))
    name_input.send_keys(credentials["name"])

    # Ввод некорректной фамилии
    invalid_lastname = "Ш"
    surname_locator = register_page.surname_input
    surname_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(surname_locator))
    surname_input.send_keys(credentials["invalid_lastname"])

    # Нажатие на кнопку "Зарегистрироваться"
    register_button = register_page.register_button
    register_button_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(register_button))
    register_button_element.click()

    # Проверка ошибки заполнения поля фамилии
    surname_error = register_page.surname_error
    surname_error_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(surname_error))
    assert surname_error_element.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

    # Закрытие браузера
    driver.quit()

def test_register_link_emailphone_error():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()

    # Переход на страницу авторизации
    driver.get("https://b2c.passport.rt.ru")

     # Инициализация страницы авторизации
    login_page = LoginPageLocators(driver)

    # Клик на ссылку "Зарегистрироваться"
    register_link = login_page.register_link
    register_link.click()

    # Проверка, что перешли на страницу регистрации
    register_page = RegisterPageLocators()
    register_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(register_page.REGISTER_TITLE))
    assert register_title.text == "Регистрация"

    # Ввод корректного имени
    name_locator = register_page.name_input
    name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(name_locator))
    name_input.send_keys(credentials["name"])

    # Ввод корректной фамилии

    surname_locator = register_page.surname_input
    surname_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(surname_locator))
    surname_input.send_keys(credentials["lastname"])

    # Ввод некорректного телефона/почты
    email_phone_locator = register_page.email_phone_input
    email_phone_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(email_phone_locator))
    email_phone_input.send_keys(credentials["invalid-format-phone"])

    # Нажатие на кнопку "Зарегистрироваться"
    register_button = register_page.register_button
    register_button_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(register_button))
    register_button_element.click()

    # Проверка ошибки заполнения поля телефона/почты
    email_phone_error = register_page.email_phone_error
    email_phone_error_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(email_phone_error))
    assert email_phone_error_element.text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"

    # Закрытие браузера
    driver.quit()


def test_register_link_done():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()

    # Переход на страницу авторизации
    driver.get("https://b2c.passport.rt.ru")

    # Инициализация страницы авторизации
    login_page = LoginPageLocators(driver)

    # Клик на ссылку "Зарегистрироваться"
    register_link = login_page.register_link
    register_link.click()

    # Проверка, что перешли на страницу регистрации
    register_page = RegisterPageLocators()
    register_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(register_page.REGISTER_TITLE))
    assert register_title.text == "Регистрация"

    # Ввод корректного имени
    name_locator = register_page.name_input
    name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(name_locator))
    name_input.send_keys(credentials["name"])

    # Ввод корректной фамилии

    surname_locator = register_page.surname_input
    surname_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(surname_locator))
    surname_input.send_keys(credentials["lastname"])

    # Ввод корректного телефона/почты
    email_phone_locator = register_page.email_phone_input
    email_phone_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(email_phone_locator))
    email_phone_input.send_keys(credentials["phone"])

    # Ввод корректного пароля
    password_locator = register_page.password_input
    password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(password_locator))
    password_input.send_keys(credentials["password"])

    # Ввод подтверждения пароля
    confirm_password_locator = register_page.confirm_password_input
    confirm_password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(confirm_password_locator))
    confirm_password_input.send_keys(credentials["password"])

    # Нажатие кнопки "Зарегистрироваться"
    register_button_locator = register_page.register_button
    register_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(register_button_locator))
    register_button.click()

    # Проверка наличия локатора с сообщением об ошибке
    account_already_exists_message_locator = register_page.account_already_exists_message
    account_already_exists_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(account_already_exists_message_locator))
    assert account_already_exists_message.text == "Учётная запись уже существует"

    # Закрытие браузера
    driver.quit()

def test_register_link_confirm_password_error():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()

    # Переход на страницу авторизации
    driver.get("https://b2c.passport.rt.ru")

    # Инициализация страницы авторизации
    login_page = LoginPageLocators(driver)

    # Клик на ссылку "Зарегистрироваться"
    register_link = login_page.register_link
    register_link.click()

    # Проверка, что перешли на страницу регистрации
    register_page = RegisterPageLocators()
    register_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(register_page.REGISTER_TITLE))
    assert register_title.text == "Регистрация"

    # Ввод корректного имени
    name_locator = register_page.name_input
    name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(name_locator))
    name_input.send_keys(credentials["name"])

    # Ввод корректной фамилии

    surname_locator = register_page.surname_input
    surname_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(surname_locator))
    surname_input.send_keys(credentials["lastname"])

    # Ввод корректного телефона/почты
    email_phone_locator = register_page.email_phone_input
    email_phone_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(email_phone_locator))
    email_phone_input.send_keys(credentials["phone"])

    # Ввод корректного пароля
    password_locator = register_page.password_input
    password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(password_locator))
    password_input.send_keys(credentials["password"])

    # Ввод неккоректного подтверждения пароля
    confirm_password_locator = register_page.confirm_password_input
    confirm_password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(confirm_password_locator))
    confirm_password_input.send_keys(credentials["not-valid-password"])

    # Нажатие кнопки "Зарегистрироваться"
    register_button_locator = register_page.register_button
    register_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(register_button_locator))
    register_button.click()

    # Проверка появления ошибки
    password_confirm_error_locator = register_page.password_confirm_error
    password_confirm_error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(password_confirm_error_locator))
    assert password_confirm_error.text == "Пароли не совпадают"

    # Закрытие браузера
    driver.quit()


def test_register_link_password_error():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()

    # Переход на страницу авторизации
    driver.get("https://b2c.passport.rt.ru")

    # Инициализация страницы авторизации
    login_page = LoginPageLocators(driver)

    # Клик на ссылку "Зарегистрироваться"
    register_link = login_page.register_link
    register_link.click()

    # Проверка, что перешли на страницу регистрации
    register_page = RegisterPageLocators()
    register_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(register_page.REGISTER_TITLE))
    assert register_title.text == "Регистрация"

    # Ввод некорректного пароля кирилицей
    password_locator = register_page.password_input
    password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(password_locator))
    password_input.send_keys(credentials["ruspassword"])

    # Нажатие кнопки "Зарегистрироваться"
    register_button_locator = register_page.register_button
    register_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(register_button_locator))
    register_button.click()

    # Находим элемент с ошибкой
    password_error_message_locator = register_page.password_error_message
    password_error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(password_error_message_locator))

    # Проверяем текст ошибки
    assert password_error_message.text == "Пароль должен содержать только латинские буквы"

    # Закрытие окна браузера
    driver.quit()

def test_register_link_smallpassword_error():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()

    # Переход на страницу авторизации
    driver.get("https://b2c.passport.rt.ru")

    # Инициализация страницы авторизации
    login_page = LoginPageLocators(driver)

    # Клик на ссылку "Зарегистрироваться"
    register_link = login_page.register_link
    register_link.click()

    # Проверка, что перешли на страницу регистрации
    register_page = RegisterPageLocators()
    register_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(register_page.REGISTER_TITLE))
    assert register_title.text == "Регистрация"

    # Ввод некорректного пароля кирилицей
    password_locator = register_page.password_input
    password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(password_locator))
    password_input.send_keys(credentials["smallpassword"])

    # Нажатие кнопки "Зарегистрироваться"
    register_button_locator = register_page.register_button
    register_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(register_button_locator))
    register_button.click()

    # Находим элемент с ошибкой
    PASSWORD_LENGTH_ERROR_MESSAGE_locator = register_page.PASSWORD_LENGTH_ERROR_MESSAGE
    PASSWORD_LENGTH_ERROR_MESSAGE = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PASSWORD_LENGTH_ERROR_MESSAGE_locator))

    # Проверяем текст ошибки
    assert PASSWORD_LENGTH_ERROR_MESSAGE.text == "Длина пароля должна быть не менее 8 символов"

    # Закрытие окна браузера
    driver.quit()






