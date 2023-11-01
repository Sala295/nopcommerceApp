from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@class='button-1 login-button']"
    button_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.textbox_username_id))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.textbox_username_id))).send_keys(username)

    def setPassword(self, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.textbox_password_id))).clear()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.textbox_password_id))).send_keys(password)

    def clickLogin(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))).click()

    def clickLogout(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, self.button_logout_linktext))).click()
