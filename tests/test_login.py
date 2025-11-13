import pytest
from pages.login_page import LoginPage
from utilities.config_reader import read_config
from utilities.logger import get_logger

@pytest.mark.usefixtures("setup")
class TestLogin:

    @pytest.fixture()
    def set_logger(self):
        self.logger = get_logger("LoginTest")

    def test_valid_login(self, set_logger):
        driver = self.driver
        driver.get(read_config("DEFAULT", "base_url"))
        self.logger.info("Launched the login page")

        login_page = LoginPage(driver)
        login_page.enter_username(read_config("DEFAULT", "username"))
        login_page.enter_password(read_config("DEFAULT", "password"))
        login_page.click_login()

        # login_page.handle_change_password_popup()
        success_message = login_page.get_success_message()
        self.logger.info("Captured success message: " + success_message)

        assert "You logged into a secure area!" in success_message

    def test_invalid_login(self, set_logger):
        driver = self.driver
        driver.get(read_config("DEFAULT", "base_url"))
        self.logger.info("Launched the login page with invalid credentials")

        login_page = LoginPage(driver)
        login_page.enter_username("wrongUser")
        login_page.enter_password("wrongPass")
        login_page.click_login()

        error_message = login_page.get_error_message()
        self.logger.info("Captured error message: " + error_message)

        assert "Your username is invalid!" in error_message
