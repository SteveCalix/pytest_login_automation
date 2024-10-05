from selenium.webdriver.common.by import By
from pages.helpers.common import CommonOps

class LoginPage(CommonOps):

    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    SUBMITBUTTON = (By.ID, 'submit')
    ERRORMESSAGE = (By.ID, 'error')

    def enter_username(self, username):
        self.wait_for(self.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.wait_for(self.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.wait_for(self.SUBMITBUTTON).click()

    def get_error_message(self):
        return self.wait_for(self.ERRORMESSAGE).text
