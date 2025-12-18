from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    my_account_link_text = "My Account"
    login_link_text = "Login"
    email_entry_xpath = "//input[@id='input-email']"
    password_entry_xpath = "//input[@id='input-password']"
    login_button_xpath = "//input[@value='Login']"




    def login_page_valid_credentials(self, email, password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.my_account_link_text))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.login_link_text))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.email_entry_xpath))
        ).send_keys(email)

        self.driver.find_element(By.XPATH, self.password_entry_xpath).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button_xpath))
        ).click()

    def login_page_invalid_credentials(self, email, password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.my_account_link_text))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.login_link_text))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.email_entry_xpath))
        ).send_keys(email)

        self.driver.find_element(By.XPATH, self.password_entry_xpath).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button_xpath))
        ).click()

    def login_page_valid_email_invalid_password(self,email, password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.my_account_link_text))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.login_link_text))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.email_entry_xpath))
        ).send_keys(email)

        self.driver.find_element(By.XPATH, self.password_entry_xpath).send_keys(password)

    def login_page_invalid_email_valid_password(self, email, password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.my_account_link_text))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, self.login_link_text))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.email_entry_xpath))
        ).send_keys(email)

        self.driver.find_element(By.XPATH, self.password_entry_xpath).send_keys(password)





