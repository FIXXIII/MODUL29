from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPageLocators:

    RESET_PASSWORD_TITLE = None
    RESET_PASSWORD_LINK = None

    @property
    def forgot_password_link(self):
        locator = (By.ID, 'forgot_password')
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator))

    FORGOT_PASSWORD_LINK = (By.ID, "forgot_password")

    def __init__(self, driver):
        self.forgot_password_link = None
        self.browser = None
        self.driver = driver

    # таб-кнопка авторизации по телефону
    @property
    def phone_tab(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container login-form-container']/div[@class='card-container__wrapper']/div[@class='card-container__content']/form[@class='login-form']/div[@class='tabs-input-container']/div[@class='rt-tabs rt-tabs--orange rt-tabs--small tabs-input-container__tabs']/div[@id='t-btn-tab-phone']"))
        )

        # кнопка зарегистрироваться
    @property
    def register_link(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container login-form-container']/div[@class='card-container__wrapper']/div[@class='card-container__content']/form[@class='login-form']/div[@class='login-form__register-con']/a[@id='kc-register']"))
        )

    # кнопка авторизации через сайт вконтакте
    @property
    def vk_social_login(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container login-form-container']/div[@class='card-container__wrapper']/div[@class='card-container__content']/form[@class='login-form']/div[@class='social-providers-container login-form__social-providers']/div[@class='social-providers']/a[@id='oidc_vk']"))
        )

    # поле ввода логина
    @property
    def login_input(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container login-form-container']/div[@class='card-container__wrapper']/div[@class='card-container__content']/form[@class='login-form']/div[@class='tabs-input-container']/div[@class='rt-input-container tabs-input-container__login']/div[@class='rt-input rt-input--rounded rt-input--orange rt-input--active']/input[@id='username']"))
        )

    # поле ввода пароля
    @property
    def password_input(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container login-form-container']/div[@class='card-container__wrapper']/div[@class='card-container__content']/form[@class='login-form']/div[@class='rt-input-container']/div[@class='rt-input rt-input--rounded rt-input--orange rt-input--actions']/input[@id='password']"))
        )

    # кнопка вход в лк
    @property
    def login_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/html/body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container login-form-container']/div[@class='card-container__wrapper']/div[@class='card-container__content']/form[@class='login-form']/button[@id='kc-login']")))

    # кнопка-таб почта
    @property
    def email_tab(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container login-form-container']/div[@class='card-container__wrapper']/div[@class='card-container__content']/form[@class='login-form']/div[@class='tabs-input-container']/div[@class='rt-tabs rt-tabs--orange rt-tabs--small tabs-input-container__tabs']/div[@id='t-btn-tab-mail']"))
        )

    # локатор "Запомнить меня" (checkbox)
    @property
    def remember_me_checkbox(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//span[@class='rt-checkbox__shape rt-checkbox__shape--circular rt-checkbox__shape--orange']"))
        )

    @forgot_password_link.setter
    def forgot_password_link(self, value):
        self._forgot_password_link = value


class ResetPasswordPageLocators:
    RESET_PASSWORD_TITLE = (By.XPATH, "/html/body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container reset-form-container']/div[@class='card-container__wrapper']/h1[@class='card-container__title']")

    def __init__(self, driver):
        self.driver = driver

    @property
    def reset_password_title(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ResetPasswordPageLocators.RESET_PASSWORD_TITLE)
        )

class RegisterPageLocators:
    def __init__(self):
        self.REGISTER_TITLE = None

    pass

class RegisterPageLocators:
    REGISTER_TITLE = (By.XPATH, "/html/body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container register-form-container']/div[@class='card-container__wrapper']/h1[@class='card-container__title']")
    # локатор надписи регистрация над формой регистрации

    @property
    def name_input(self):
        return (By.XPATH, "//input[@name='firstName']")

    @property
    def surname_input(self):
        return (By.XPATH, "//input[@name='lastName']")

    @property
    def region_dropdown(self):
        return (By.XPATH, "//select[@name='region']")

    @property
    def email_phone_input(self):
        return (By.XPATH, "//input[@id='address']")

    @property
    def password_input(self):
        return (By.XPATH, "//input[@name='password']")

    @property
    def confirm_password_input(self):
        return (By.XPATH, "//form[@class='register-form']//input[@id='password-confirm']")

    @property
    def register_button(self):
        return (By.XPATH, "//button[@class='rt-btn rt-btn--orange rt-btn--medium rt-btn--rounded register-form__reg-btn']")

    @property
    def name_error(self):
        return (By.XPATH,
                "//span[@class='rt-input-container__meta rt-input-container__meta--error'][text()='Необходимо заполнить поле кириллицей. От 2 до 30 символов.']")


    @property
    def surname_error(self):
       return (By.XPATH,
            "//div[@class='name-container']//div[@class='rt-input-container rt-input-container--error']//span[@class='rt-input-container__meta rt-input-container__meta--error'][text()='Необходимо заполнить поле кириллицей. От 2 до 30 символов.']")

    @property
    def email_phone_error(self):
        return (By.XPATH,
                "/html/body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container register-form-container']/div[@class='card-container__wrapper']/div[@class='card-container__content']/form[@class='register-form']/div[@class='rt-input-container rt-input-container--error email-or-phone register-form__address']/span[@class='rt-input-container__meta rt-input-container__meta--error']")

    @property
    def account_already_exists_message(self):
        return (By.XPATH,
                "/html/body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container register-form-container']/div[@class='card-container__wrapper']/div[@class='card-container__content']/form[@class='register-form']/div[@class='base-modal-wrapper card-modal']/div[@class='card-modal__card-wrapper']/div[@class='card-modal__card']/h2[@class='card-modal__title']")

    @property
    def password_confirm_error(self):
        return (By.XPATH,
                "/html/body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container register-form-container']/div[@class='card-container__wrapper']/div[@class='card-container__content']/form[@class='register-form']/div[@class='new-password-container']/div[@class='rt-input-container rt-input-container--error new-password-container__confirmed-password']/span[@class='rt-input-container__meta rt-input-container__meta--error' and text()='Пароли не совпадают']")

    @property
    def password_error_message(self):
        return (By.XPATH, "/html/body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container register-form-container']/div[@class='card-container__wrapper']/div[@class='card-container__content']/form[@class='register-form']/div[@class='new-password-container']/div[@class='rt-input-container rt-input-container--error new-password-container__password']/span[@class='rt-input-container__meta rt-input-container__meta--error']")

    @property
    def PASSWORD_LENGTH_ERROR_MESSAGE(self):
        return (By.XPATH,
                "/html/body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[@class='card-container register-form-container']/div[@class='card-container__wrapper']/div[@class='card-container__content']/form[@class='register-form']/div[@class='new-password-container']/div[@class='rt-input-container rt-input-container--error new-password-container__password']/span[@class='rt-input-container__meta rt-input-container__meta--error' and text()='Длина пароля должна быть не менее 8 символов']")