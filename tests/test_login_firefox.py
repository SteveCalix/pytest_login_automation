from pages.login_page import LoginPage
from pages.login_success_page import LoginSuccessPage
from tests.test_data import valid_username,valid_password,invalid_password,invalid_username, partial_url

def submit_credentials(username, password, driver):
    login = LoginPage(driver)
    login.enter_username(username)
    login.enter_password(password)
    login.click_login_button()
    return login


def test_login_success_chrome(firefox_driver):
    submit_credentials(valid_username, valid_password, firefox_driver)
    success_login_url = firefox_driver.current_url
    assert success_login_url.find(partial_url) >= 0
    login_success = LoginSuccessPage(firefox_driver)
    assert login_success.get_success_message().find("Congratulations") >= 0
    assert login_success.get_success_message().find("successfully logged in") >= 0
    assert login_success.find(LoginSuccessPage.LOGOUTBUTTON)


def test_wrong_username_chrome(firefox_driver):
    login = submit_credentials(invalid_username, valid_password, firefox_driver)
    for i in range(3):
        try:
            assert login.get_error_message() == 'Your username is invalid!'
            break
        except AssertionError as msg:
            print(msg)
            continue


def test_wrong_password_chrome(firefox_driver):
    login = submit_credentials(valid_username, invalid_password, firefox_driver)
    for i in range(3):
        try:
            assert login.get_error_message() == 'Your password is invalid!'
            break
        except AssertionError as msg:
            print(msg)
            continue
