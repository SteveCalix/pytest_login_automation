from pages.login_page import LoginPage
from pages.login_success_page import LoginSuccessPage
from tests.test_data import valid_username,valid_password,invalid_password,invalid_username, partial_url

def submit_credentials(username, password, driver):
    login = LoginPage(driver)
    login.enter_username(username)
    login.enter_password(password)
    login.click_login_button()
    return login