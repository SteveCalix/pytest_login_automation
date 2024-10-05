from selenium.webdriver.common.by import By
from pages.helpers.common import CommonOps

class LoginSuccessPage(CommonOps):

    LOGINSUCCESSMESSAGE = (By.CSS_SELECTOR, ".has-text-align-center > strong:nth-child(1)")
    LOGOUTBUTTON = (By.XPATH, "//div[@class='wp-block-group']/div/div/a")

    def click_logout_button(self):
        self.wait_for(self.LOGOUTBUTTON).click()

    def get_success_message(self):
        return self.wait_for(self.LOGINSUCCESSMESSAGE).text

    def find_string_on_successful_login(self, search_string):
        return self.get_success_message().find(search_string)