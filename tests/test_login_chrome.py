from pages.login_page import LoginPage
from pages.login_success_page import LoginSuccessPage
from tests.test_data import valid_username,valid_password,invalid_password,invalid_username, partial_url
from pages.helpers.common_actions import submit_credentials

def test_login_success_chrome(chrome_driver):
    submit_credentials(valid_username, valid_password, chrome_driver)
    success_login_url = chrome_driver.current_url
    assert success_login_url.find(partial_url) >= 0
    login_success = LoginSuccessPage(chrome_driver)
    assert login_success.get_success_message().find("Congratulations") >= 0
    assert login_success.get_success_message().find("successfully logged in") >= 0
    assert login_success.find(LoginSuccessPage.LOGOUTBUTTON)


def test_wrong_username_chrome(chrome_driver):
    login = submit_credentials(invalid_username, valid_password, chrome_driver)
    for i in range(3):
        try:
            assert login.get_error_message() == 'Your username is invalid!'
            break
        except AssertionError as msg:
            print(msg)
            continue


def test_wrong_password_chrome(chrome_driver):
    login = submit_credentials(valid_username, invalid_password, chrome_driver)
    for i in range(3):
        try:
            assert login.get_error_message() == 'Your password is invalid!'
            break
        except AssertionError as msg:
            print(msg)
            continue
