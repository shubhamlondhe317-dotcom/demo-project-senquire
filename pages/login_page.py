from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MSG = (By.CSS_SELECTOR, "div.flash.success")
    ERROR_MSG = (By.CSS_SELECTOR, "div.flash.error")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SUCCESS_MSG)
        ).text

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ERROR_MSG)
        ).text

    # 🔹 New method to handle change password popup
    def handle_change_password_popup(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(),'Change Password') or contains(@class,'change-password')]")
                )
            )
            print("Change Password popup detected — closing it.")
            # Try clicking close/cancel/skip
            close_btn = self.driver.find_element(
                By.XPATH, "//button[contains(text(),'Cancel') or contains(text(),'Skip') or contains(text(),'Close')]"
            )
            close_btn.click()
        except TimeoutException:
            print("No change password popup appeared.")
